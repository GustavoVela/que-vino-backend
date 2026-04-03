#!/usr/bin/env python3
"""
Test completo de Knowledge Stores API en producción.
Genera knowledge_api_test_results.txt con todos los llamados HTTP y sus respuestas.
"""
import urllib.request
import urllib.error
import json
import os
from datetime import datetime

# ─── Config ────────────────────────────────────────────────────────────────────
FIREBASE_API_KEY     = "AIzaSyA6zvvvfV9DhKdrrBTSM0iuqDsH9dHpvyA"
TEST_USER_EMAIL      = "que-vino-bakend-test@v3l4.com"
TEST_USER_PASSWORD   = "0X3S5q3b7jxWPzU4p8R1C4DnEO6QhN"
BASE_URL             = "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app"
OUTPUT_FILE          = "knowledge_api_test_results.txt"

# ─── HTTP helper (sin dependencias externas) ──────────────────────────────────
log_lines = []

def http_request(method, url, token=None, body=None, timeout=25):
    """Hace una petición HTTP usando stdlib. Devuelve (status_code, body_dict_or_str)."""
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    data = json.dumps(body).encode("utf-8") if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read().decode("utf-8")
            try:
                return r.status, json.loads(raw)
            except Exception:
                return r.status, raw
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8")
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, raw
    except Exception as ex:
        return None, str(ex)


def call(label, method, path, token=None, body=None, timeout=25):
    """Ejecuta y loguea un llamado al API."""
    url = f"{BASE_URL}{path}"
    status, resp = http_request(method, url, token=token, body=body, timeout=timeout)

    lines = [
        f"{'─'*70}",
        f"  {label}",
        f"{'─'*70}",
        f"  REQUEST:",
        f"    {method} {url}",
    ]
    if body:
        lines.append(f"    Body: {json.dumps(body, ensure_ascii=False, indent=6)}")

    lines += [
        f"",
        f"  RESPONSE:",
        f"    HTTP {status}",
        f"    {json.dumps(resp, indent=6, ensure_ascii=False) if isinstance(resp, (dict, list)) else resp}",
        f"",
    ]
    log_lines.append("\n".join(lines))
    status_label = f"HTTP {status}" if status else "ERROR"
    print(f"  [{status_label}] {method} {path}")
    return status, resp


# ─── Auth ──────────────────────────────────────────────────────────────────────
def get_firebase_token():
    auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
    status, resp = http_request("POST", auth_url, body={
        "email": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD,
        "returnSecureToken": True
    })
    if status == 200 and isinstance(resp, dict):
        token = resp["idToken"]
        log_lines.append(
            f"{'─'*70}\n"
            f"  AUTH — Firebase signInWithPassword\n"
            f"{'─'*70}\n"
            f"  REQUEST:\n"
            f"    POST https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword\n"
            f"    Body: {{\"email\": \"{TEST_USER_EMAIL}\", \"password\": \"*****\", \"returnSecureToken\": true}}\n\n"
            f"  RESPONSE:\n"
            f"    HTTP 200\n"
            f"    idToken: {token[:50]}...[truncado por seguridad]\n"
            f"    localId: {resp.get('localId')}\n"
            f"    email: {resp.get('email')}\n\n"
        )
        print(f"  [HTTP 200] Token obtenido para {resp.get('email')}")
        return token
    else:
        raise Exception(f"Auth failed {status}: {resp}")


# ─── Main ──────────────────────────────────────────────────────────────────────
def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_lines.append(
        f"{'═'*70}\n"
        f"  KNOWLEDGE STORES API — PRUEBA COMPLETA EN PRODUCCIÓN\n"
        f"{'═'*70}\n"
        f"  Base URL : {BASE_URL}\n"
        f"  Fecha    : {now}\n\n"
    )

    # ── 1. Health Check (público) ──────────────────────────────────────────────
    print("\n[1/6] GET /health (sin token)")
    call("1. GET /health — Endpoint público (sin autenticación)", "GET", "/health", timeout=10)

    # ── 2. Firebase Auth ───────────────────────────────────────────────────────
    print("\n[2/6] Autenticación Firebase")
    try:
        token = get_firebase_token()
    except Exception as e:
        log_lines.append(f"  ERROR CRÍTICO: No se pudo obtener token — {e}\n")
        print(f"  ERROR: {e}")
        write_results()
        return

    # ── 3. Listar stores (con token) ──────────────────────────────────────────
    print("\n[3/6] GET /knowledge-stores")
    status, stores_resp = call(
        "3. GET /knowledge-stores — Listar todos los stores (con token)",
        "GET", "/knowledge-stores", token=token
    )

    # ── 4. Listar archivos del primer store ───────────────────────────────────
    store_id = None
    if status == 200:
        stores = stores_resp if isinstance(stores_resp, list) else (
            stores_resp.get("corpora") or stores_resp.get("stores") or []
            if isinstance(stores_resp, dict) else []
        )
        if stores:
            first = stores[0]
            raw_id = (first.get("name") or first.get("id") or first.get("store_id") or "")
            store_id = raw_id.split("/")[-1] if "/" in raw_id else raw_id
            print(f"\n[4/6] GET /knowledge-stores/{store_id}/files")
            call(
                f"4. GET /knowledge-stores/{store_id}/files — Listar archivos del store",
                "GET", f"/knowledge-stores/{store_id}/files", token=token
            )
        else:
            log_lines.append("  [INFO] No hay stores disponibles — se omite el test de archivos.\n")
            print("\n[4/6] Sin stores disponibles — omitido")
    else:
        print(f"\n[4/6] Omitido por error en paso 3 (HTTP {status})")

    # ── 5. POST /sync (payload mínimo de prueba) ──────────────────────────────
    print("\n[5/6] POST /knowledge-stores/sync")
    sync_body = {
        "bucket_name": "que-vino-23032025-audios",
        "prefix": "test/",
        "store_name": "test-sync-prueba"
    }
    call(
        "5. POST /knowledge-stores/sync — Sincronizar bucket GCS con Gemini",
        "POST", "/knowledge-stores/sync", token=token, body=sync_body, timeout=60
    )

    # ── 6. GET /knowledge-stores SIN token → esperado 401 ────────────────────
    print("\n[6/6] GET /knowledge-stores SIN token (esperado: 401)")
    call(
        "6. GET /knowledge-stores SIN token — Verificar que retorna 401",
        "GET", "/knowledge-stores"
    )

    # ── Fin ────────────────────────────────────────────────────────────────────
    log_lines.append(
        f"{'═'*70}\n"
        f"  FIN DE PRUEBA — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"{'═'*70}\n"
    )
    write_results()

def write_results():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))
    print(f"\n✅ Resultados guardados en: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
