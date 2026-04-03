#!/usr/bin/env python3
"""
Test de integración en producción para quevino-audio.
Ejecutar desde la raíz del repositorio:
    python3 apis/audio/tests/test_production.py
Genera: apis/audio/tests/TEST_RESULTS.md
"""
import urllib.request
import urllib.error
import json
import sys
from datetime import datetime
from pathlib import Path

# ── Constantes ─────────────────────────────────────────────────────────────────
BASE_URL    = "https://quevino-audio-2lkhisz2aa-uc.a.run.app"
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
            raw = r.read()
            content_type = r.headers.get("Content-Type", "")
            if "audio" in content_type:
                # Respuesta binaria — el endpoint de generación devuelve audio
                return r.status, {
                    "__binary__": True,
                    "content_type": content_type,
                    "size_bytes": len(raw),
                    "x_generation_id": r.headers.get("X-Generation-ID"),
                    "x_enrichment_status": r.headers.get("X-Enrichment-Status"),
                }
            return r.status, json.loads(raw.decode()) if raw else {}
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
        "email":           env.get("FIREBASE_TEST_USER_EMAIL"),
        "password":        env.get("FIREBASE_TEST_USER_PASSWORD"),
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
        f"# Test Results — quevino-audio",
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

        if isinstance(r["response"], dict) and r["response"].get("__binary__"):
            resp_str = json.dumps({
                "content_type":        r["response"]["content_type"],
                "size_bytes":          r["response"]["size_bytes"],
                "X-Generation-ID":     r["response"]["x_generation_id"],
                "X-Enrichment-Status": r["response"]["x_enrichment_status"],
            }, indent=2)
        elif isinstance(r["response"], (dict, list)):
            resp_str = json.dumps(r["response"], indent=2, ensure_ascii=False)
        else:
            resp_str = str(r["response"])

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
    print(f"\n🔍 Testing quevino-audio @ {BASE_URL}\n")

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

    # 3. Listar voces (con token)
    test("GET /audio/providers/voices — Listar voces disponibles",
         "GET", "/audio/providers/voices", token=token)

    # 4. Listar modelos (con token)
    test("GET /audio/providers/models — Listar modelos disponibles",
         "GET", "/audio/providers/models", token=token)

    # 5. Generar audio con ElevenLabs (con token)
    _, voices_resp = http("GET", f"{BASE_URL}/audio/providers/voices",
                          token=token, timeout=15)
    elevenlabs_voices = [
        v for v in (voices_resp if isinstance(voices_resp, list) else [])
        if v.get("provider") == "ELEVENLABS"
    ]
    voice_id = elevenlabs_voices[0]["voice_id"] if elevenlabs_voices else "CwhRBWXzGAHq8TQ4Fs17"

    test(
        "POST /audio/generate — Generación ElevenLabs (eleven_multilingual_v2)",
        "POST", "/audio/generate",
        token=token,
        body={
            "text":          "Hola, este es un test de integración de la API de audio de Que Vino.",
            "provider":      "ELEVENLABS",
            "voice_id":      voice_id,
            "model_id":      "eleven_multilingual_v2",
            "output_format": "mp3",
            "enrich_audio":  False
        },
        expected_status=201,
        timeout=90
    )

    # 6. Generar audio — sin token → 401
    test(
        "POST /audio/generate — Sin token (esperado: 401)",
        "POST", "/audio/generate",
        body={"text": "test", "provider": "ELEVENLABS", "voice_id": voice_id},
        expected_status=401
    )

    # 7. Generar audio — payload incompleto → 422
    test(
        "POST /audio/generate — Payload incompleto sin voice_id (esperado: 422)",
        "POST", "/audio/generate",
        token=token,
        body={"text": "test", "provider": "ELEVENLABS"},
        expected_status=422
    )

    write_report()
    passed = sum(1 for r in results if r["passed"])
    print(f"\n{'✅ Todas las pruebas pasaron.' if passed == len(results) else f'❌ {len(results)-passed} prueba(s) fallaron.'}")
    sys.exit(0 if passed == len(results) else 1)


if __name__ == "__main__":
    main()
