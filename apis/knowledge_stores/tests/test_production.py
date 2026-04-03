#!/usr/bin/env python3
"""
Test de integración en producción para quevino-knowledge-stores.
Ejecutar desde la raíz del repositorio:
    python3 apis/knowledge_stores/tests/test_production.py
Genera: apis/knowledge_stores/tests/TEST_RESULTS.md
"""
import urllib.request
import urllib.error
import json
import sys
from datetime import datetime
from pathlib import Path

# ── Constantes ─────────────────────────────────────────────────────────────────
BASE_URL    = "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app"
ENV_FILE    = Path(__file__).parents[3] / ".env"
OUTPUT_FILE = Path(__file__).parent / "TEST_RESULTS.md"

# ── Helpers ────────────────────────────────────────────────────────────────────
def load_env(path: Path) -> dict:
    """Carga variables del .env del repositorio sin dependencias externas."""
    env = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"')
    return env


def http(method: str, url: str, token: str = None, body: dict = None,
         timeout: int = 30):
    """
    Realiza una petición HTTP usando exclusivamente la stdlib de Python.
    Devuelve (status_code, dict|str). No requiere librerías externas.
    """
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(body).encode("utf-8") if body else None
    req  = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read().decode()
            return r.status, json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:    return e.code, json.loads(raw)
        except: return e.code, raw
    except Exception as ex:
        return None, str(ex)


def get_token(env: dict) -> str:
    """Obtiene un Firebase ID Token real usando las credenciales del .env."""
    api_key = env.get("FIREBASE_API_KEY", "")
    url     = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
    status, resp = http("POST", url, body={
        "email":             env.get("FIREBASE_TEST_USER_EMAIL"),
        "password":          env.get("FIREBASE_TEST_USER_PASSWORD"),
        "returnSecureToken": True
    })
    if status == 200 and isinstance(resp, dict):
        return resp["idToken"]
    raise RuntimeError(f"Autenticación fallida ({status}): {resp}")


# ── Runner ─────────────────────────────────────────────────────────────────────
results: list = []


def test(label: str, method: str, path: str, token: str = None,
         body: dict = None, expected_status: int = 200, timeout: int = 60):
    """Ejecuta y registra una prueba individual de integración."""
    url = f"{BASE_URL}{path}"
    status, resp = http(method, url, token=token, body=body, timeout=timeout)
    passed = status == expected_status
    results.append({
        "label": label, "method": method, "url": url, "body": body,
        "status": status, "expected": expected_status,
        "passed": passed, "response": resp
    })
    icon = "✅" if passed else "❌"
    print(f"  {icon} [HTTP {status}] {method} {path}")
    return status, resp


# ── Reporte ────────────────────────────────────────────────────────────────────
def write_report():
    """Genera TEST_RESULTS.md con el detalle completo de cada prueba."""
    passed_count = sum(1 for r in results if r["passed"])
    total        = len(results)
    now          = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        f"# Test Results — quevino-knowledge-stores",
        f"",
        f"**Entorno:** Producción (Cloud Run)  ",
        f"**URL Base:** `{BASE_URL}`  ",
        f"**Fecha:** {now}  ",
        f"**Resultado:** `{passed_count}/{total}` pruebas exitosas  ",
        f"",
        f"---",
        f"",
    ]

    for r in results:
        icon = "✅ PASS" if r["passed"] else "❌ FAIL"
        request_block = [f"{r['method']} {r['url']}"]
        if r["body"]:
            request_block.append(json.dumps(r["body"], indent=2, ensure_ascii=False))

        resp_str = (
            json.dumps(r["response"], indent=2, ensure_ascii=False)
            if isinstance(r["response"], (dict, list)) else str(r["response"])
        )

        lines += [
            f"## {icon} — {r['label']}",
            f"",
            f"**Request:**",
            f"```",
            "\n".join(request_block),
            f"```",
            f"",
            f"**Response:** HTTP `{r['status']}` (esperado: `{r['expected']}`)",
            f"```json",
            resp_str,
            f"```",
            f"",
            f"---",
            f"",
        ]

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n📄 Reporte generado: {OUTPUT_FILE}")


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    env = load_env(ENV_FILE)
    print(f"\n🔍 Testing quevino-knowledge-stores @ {BASE_URL}\n")

    # 1. Health (público, sin token)
    test("GET /health — Endpoint público (sin autenticación)",
         "GET", "/health", expected_status=200)

    # 2. Obtener token Firebase
    try:
        token = get_token(env)
        print(f"  🔑 Token obtenido para {env.get('FIREBASE_TEST_USER_EMAIL')}")
    except Exception as e:
        print(f"  💥 Auth fallida: {e}")
        write_report()
        sys.exit(1)

    # 3. Listar stores (con token)
    status, stores_resp = test(
        "GET /knowledge-stores — Listar todos los stores",
        "GET", "/knowledge-stores", token=token
    )

    # 4. Listar archivos del primer store (si existe)
    store_id = None
    if status == 200 and isinstance(stores_resp, list) and stores_resp:
        first   = stores_resp[0]
        raw_id  = first.get("id") or first.get("name") or ""
        store_id = raw_id.split("/")[-1] if "/" in raw_id else raw_id

    if store_id:
        test(
            f"GET /knowledge-stores/{store_id}/files — Listar archivos del store",
            "GET", f"/knowledge-stores/{store_id}/files", token=token
        )
    else:
        print("  ⚠️  Sin stores disponibles — test de archivos omitido")

    # 5. Sync con bucket inexistente → estructura de respuesta correcta
    test(
        "POST /knowledge-stores/sync — Sincronizar bucket (bucket vacío)",
        "POST", "/knowledge-stores/sync",
        token=token,
        body={
            "bucket_name": "que-vino-23032025-audios",
            "prefix":      "test-integration/",
            "store_name":  "test-integration-store"
        },
        expected_status=200,
        timeout=60
    )

    # 6. Sin token → 401
    test(
        "GET /knowledge-stores — Sin token (esperado: 401)",
        "GET", "/knowledge-stores",
        expected_status=401
    )

    # 7. Token inválido → 401
    test(
        "GET /knowledge-stores — Token inválido (esperado: 401)",
        "GET", "/knowledge-stores",
        token="token.invalido.jwt",
        expected_status=401
    )

    write_report()
    passed = sum(1 for r in results if r["passed"])
    print(f"\n{'✅ Todas las pruebas pasaron.' if passed == len(results) else f'❌ {len(results)-passed} prueba(s) fallaron.'}")
    sys.exit(0 if passed == len(results) else 1)


if __name__ == "__main__":
    main()
