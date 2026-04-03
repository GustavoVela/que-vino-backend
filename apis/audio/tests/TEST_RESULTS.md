# Test Results — quevino-audio

**Entorno:** Producción (Cloud Run)  
**URL Base:** `https://quevino-audio-2lkhisz2aa-uc.a.run.app`  
**Fecha:** 2026-04-02 18:32:13  
**Resultado:** `6/6` pruebas exitosas  

---

## ✅ PASS — GET /health — Endpoint público (sin autenticación)

**Request:**
```
GET https://quevino-audio-2lkhisz2aa-uc.a.run.app/health
```

**Response:** HTTP `200` (esperado: `200`)
```json
{
  "status": "ok",
  "service": "que-vino-audio-api"
}
```

---

## ✅ PASS — GET /audio/providers/voices — Listar voces disponibles

**Request:**
```
GET https://quevino-audio-2lkhisz2aa-uc.a.run.app/audio/providers/voices
```

**Response:** HTTP `200` (esperado: `200`)
```json
[
  {
    "provider": "GOOGLE",
    "voice_id": "Achernar",
    "name": "Achernar",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Achird",
    "name": "Achird",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Algenib",
    "name": "Algenib",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Algieba",
    "name": "Algieba",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Alnilam",
    "name": "Alnilam",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Aoede",
    "name": "Aoede",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Autonoe",
    "name": "Autonoe",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Callirrhoe",
    "name": "Callirrhoe",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Charon",
    "name": "Charon",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Despina",
    "name": "Despina",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Enceladus",
    "name": "Enceladus",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Erinome",
    "name": "Erinome",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Fenrir",
    "name": "Fenrir",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Gacrux",
    "name": "Gacrux",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Iapetus",
    "name": "Iapetus",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Kore",
    "name": "Kore",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Laomedeia",
    "name": "Laomedeia",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Leda",
    "name": "Leda",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Orus",
    "name": "Orus",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Puck",
    "name": "Puck",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Pulcherrima",
    "name": "Pulcherrima",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Rasalgethi",
    "name": "Rasalgethi",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Sadachbia",
    "name": "Sadachbia",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Sadaltager",
    "name": "Sadaltager",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Schedar",
    "name": "Schedar",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Sulafat",
    "name": "Sulafat",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Umbriel",
    "name": "Umbriel",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Vindemiatrix",
    "name": "Vindemiatrix",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Zephyr",
    "name": "Zephyr",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "Zubenelgenubi",
    "name": "Zubenelgenubi",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "af-ZA-Standard-A",
    "name": "af-ZA-Standard-A",
    "languages": [
      "af-ZA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "am-ET-Standard-A",
    "name": "am-ET-Standard-A",
    "languages": [
      "am-ET"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "am-ET-Standard-B",
    "name": "am-ET-Standard-B",
    "languages": [
      "am-ET"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "am-ET-Wavenet-A",
    "name": "am-ET-Wavenet-A",
    "languages": [
      "am-ET"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "am-ET-Wavenet-B",
    "name": "am-ET-Wavenet-B",
    "languages": [
      "am-ET"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Achernar",
    "name": "ar-XA-Chirp3-HD-Achernar",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Achird",
    "name": "ar-XA-Chirp3-HD-Achird",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Algenib",
    "name": "ar-XA-Chirp3-HD-Algenib",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Algieba",
    "name": "ar-XA-Chirp3-HD-Algieba",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Alnilam",
    "name": "ar-XA-Chirp3-HD-Alnilam",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Aoede",
    "name": "ar-XA-Chirp3-HD-Aoede",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Autonoe",
    "name": "ar-XA-Chirp3-HD-Autonoe",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Callirrhoe",
    "name": "ar-XA-Chirp3-HD-Callirrhoe",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Charon",
    "name": "ar-XA-Chirp3-HD-Charon",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Despina",
    "name": "ar-XA-Chirp3-HD-Despina",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Enceladus",
    "name": "ar-XA-Chirp3-HD-Enceladus",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Erinome",
    "name": "ar-XA-Chirp3-HD-Erinome",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Fenrir",
    "name": "ar-XA-Chirp3-HD-Fenrir",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Gacrux",
    "name": "ar-XA-Chirp3-HD-Gacrux",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Iapetus",
    "name": "ar-XA-Chirp3-HD-Iapetus",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Kore",
    "name": "ar-XA-Chirp3-HD-Kore",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Laomedeia",
    "name": "ar-XA-Chirp3-HD-Laomedeia",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Leda",
    "name": "ar-XA-Chirp3-HD-Leda",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Orus",
    "name": "ar-XA-Chirp3-HD-Orus",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Puck",
    "name": "ar-XA-Chirp3-HD-Puck",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Pulcherrima",
    "name": "ar-XA-Chirp3-HD-Pulcherrima",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Rasalgethi",
    "name": "ar-XA-Chirp3-HD-Rasalgethi",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Sadachbia",
    "name": "ar-XA-Chirp3-HD-Sadachbia",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Sadaltager",
    "name": "ar-XA-Chirp3-HD-Sadaltager",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Schedar",
    "name": "ar-XA-Chirp3-HD-Schedar",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Sulafat",
    "name": "ar-XA-Chirp3-HD-Sulafat",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Umbriel",
    "name": "ar-XA-Chirp3-HD-Umbriel",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Vindemiatrix",
    "name": "ar-XA-Chirp3-HD-Vindemiatrix",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Zephyr",
    "name": "ar-XA-Chirp3-HD-Zephyr",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Chirp3-HD-Zubenelgenubi",
    "name": "ar-XA-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Standard-A",
    "name": "ar-XA-Standard-A",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Standard-B",
    "name": "ar-XA-Standard-B",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Standard-C",
    "name": "ar-XA-Standard-C",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Standard-D",
    "name": "ar-XA-Standard-D",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Wavenet-A",
    "name": "ar-XA-Wavenet-A",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Wavenet-B",
    "name": "ar-XA-Wavenet-B",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Wavenet-C",
    "name": "ar-XA-Wavenet-C",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ar-XA-Wavenet-D",
    "name": "ar-XA-Wavenet-D",
    "languages": [
      "ar-XA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Achernar",
    "name": "bg-BG-Chirp3-HD-Achernar",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Achird",
    "name": "bg-BG-Chirp3-HD-Achird",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Algenib",
    "name": "bg-BG-Chirp3-HD-Algenib",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Algieba",
    "name": "bg-BG-Chirp3-HD-Algieba",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Alnilam",
    "name": "bg-BG-Chirp3-HD-Alnilam",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Aoede",
    "name": "bg-BG-Chirp3-HD-Aoede",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Autonoe",
    "name": "bg-BG-Chirp3-HD-Autonoe",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Callirrhoe",
    "name": "bg-BG-Chirp3-HD-Callirrhoe",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Charon",
    "name": "bg-BG-Chirp3-HD-Charon",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Despina",
    "name": "bg-BG-Chirp3-HD-Despina",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Enceladus",
    "name": "bg-BG-Chirp3-HD-Enceladus",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Erinome",
    "name": "bg-BG-Chirp3-HD-Erinome",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Fenrir",
    "name": "bg-BG-Chirp3-HD-Fenrir",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Gacrux",
    "name": "bg-BG-Chirp3-HD-Gacrux",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Iapetus",
    "name": "bg-BG-Chirp3-HD-Iapetus",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Kore",
    "name": "bg-BG-Chirp3-HD-Kore",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Laomedeia",
    "name": "bg-BG-Chirp3-HD-Laomedeia",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Leda",
    "name": "bg-BG-Chirp3-HD-Leda",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Orus",
    "name": "bg-BG-Chirp3-HD-Orus",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Puck",
    "name": "bg-BG-Chirp3-HD-Puck",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Pulcherrima",
    "name": "bg-BG-Chirp3-HD-Pulcherrima",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Rasalgethi",
    "name": "bg-BG-Chirp3-HD-Rasalgethi",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Sadachbia",
    "name": "bg-BG-Chirp3-HD-Sadachbia",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Sadaltager",
    "name": "bg-BG-Chirp3-HD-Sadaltager",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Schedar",
    "name": "bg-BG-Chirp3-HD-Schedar",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Sulafat",
    "name": "bg-BG-Chirp3-HD-Sulafat",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Umbriel",
    "name": "bg-BG-Chirp3-HD-Umbriel",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Vindemiatrix",
    "name": "bg-BG-Chirp3-HD-Vindemiatrix",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Zephyr",
    "name": "bg-BG-Chirp3-HD-Zephyr",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Chirp3-HD-Zubenelgenubi",
    "name": "bg-BG-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bg-BG-Standard-B",
    "name": "bg-BG-Standard-B",
    "languages": [
      "bg-BG"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Achernar",
    "name": "bn-IN-Chirp3-HD-Achernar",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Achird",
    "name": "bn-IN-Chirp3-HD-Achird",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Algenib",
    "name": "bn-IN-Chirp3-HD-Algenib",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Algieba",
    "name": "bn-IN-Chirp3-HD-Algieba",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Alnilam",
    "name": "bn-IN-Chirp3-HD-Alnilam",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Aoede",
    "name": "bn-IN-Chirp3-HD-Aoede",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Autonoe",
    "name": "bn-IN-Chirp3-HD-Autonoe",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Callirrhoe",
    "name": "bn-IN-Chirp3-HD-Callirrhoe",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Charon",
    "name": "bn-IN-Chirp3-HD-Charon",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Despina",
    "name": "bn-IN-Chirp3-HD-Despina",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Enceladus",
    "name": "bn-IN-Chirp3-HD-Enceladus",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Erinome",
    "name": "bn-IN-Chirp3-HD-Erinome",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Fenrir",
    "name": "bn-IN-Chirp3-HD-Fenrir",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Gacrux",
    "name": "bn-IN-Chirp3-HD-Gacrux",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Iapetus",
    "name": "bn-IN-Chirp3-HD-Iapetus",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Kore",
    "name": "bn-IN-Chirp3-HD-Kore",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Laomedeia",
    "name": "bn-IN-Chirp3-HD-Laomedeia",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Leda",
    "name": "bn-IN-Chirp3-HD-Leda",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Orus",
    "name": "bn-IN-Chirp3-HD-Orus",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Puck",
    "name": "bn-IN-Chirp3-HD-Puck",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Pulcherrima",
    "name": "bn-IN-Chirp3-HD-Pulcherrima",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Rasalgethi",
    "name": "bn-IN-Chirp3-HD-Rasalgethi",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Sadachbia",
    "name": "bn-IN-Chirp3-HD-Sadachbia",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Sadaltager",
    "name": "bn-IN-Chirp3-HD-Sadaltager",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Schedar",
    "name": "bn-IN-Chirp3-HD-Schedar",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Sulafat",
    "name": "bn-IN-Chirp3-HD-Sulafat",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Umbriel",
    "name": "bn-IN-Chirp3-HD-Umbriel",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Vindemiatrix",
    "name": "bn-IN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Zephyr",
    "name": "bn-IN-Chirp3-HD-Zephyr",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Chirp3-HD-Zubenelgenubi",
    "name": "bn-IN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Standard-A",
    "name": "bn-IN-Standard-A",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Standard-B",
    "name": "bn-IN-Standard-B",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Standard-C",
    "name": "bn-IN-Standard-C",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Standard-D",
    "name": "bn-IN-Standard-D",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Wavenet-A",
    "name": "bn-IN-Wavenet-A",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Wavenet-B",
    "name": "bn-IN-Wavenet-B",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Wavenet-C",
    "name": "bn-IN-Wavenet-C",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "bn-IN-Wavenet-D",
    "name": "bn-IN-Wavenet-D",
    "languages": [
      "bn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ca-ES-Standard-B",
    "name": "ca-ES-Standard-B",
    "languages": [
      "ca-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Achernar",
    "name": "cmn-CN-Chirp3-HD-Achernar",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Achird",
    "name": "cmn-CN-Chirp3-HD-Achird",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Algenib",
    "name": "cmn-CN-Chirp3-HD-Algenib",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Algieba",
    "name": "cmn-CN-Chirp3-HD-Algieba",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Alnilam",
    "name": "cmn-CN-Chirp3-HD-Alnilam",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Aoede",
    "name": "cmn-CN-Chirp3-HD-Aoede",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Autonoe",
    "name": "cmn-CN-Chirp3-HD-Autonoe",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Callirrhoe",
    "name": "cmn-CN-Chirp3-HD-Callirrhoe",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Charon",
    "name": "cmn-CN-Chirp3-HD-Charon",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Despina",
    "name": "cmn-CN-Chirp3-HD-Despina",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Enceladus",
    "name": "cmn-CN-Chirp3-HD-Enceladus",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Erinome",
    "name": "cmn-CN-Chirp3-HD-Erinome",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Fenrir",
    "name": "cmn-CN-Chirp3-HD-Fenrir",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Gacrux",
    "name": "cmn-CN-Chirp3-HD-Gacrux",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Iapetus",
    "name": "cmn-CN-Chirp3-HD-Iapetus",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Kore",
    "name": "cmn-CN-Chirp3-HD-Kore",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Laomedeia",
    "name": "cmn-CN-Chirp3-HD-Laomedeia",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Leda",
    "name": "cmn-CN-Chirp3-HD-Leda",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Orus",
    "name": "cmn-CN-Chirp3-HD-Orus",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Puck",
    "name": "cmn-CN-Chirp3-HD-Puck",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Pulcherrima",
    "name": "cmn-CN-Chirp3-HD-Pulcherrima",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Rasalgethi",
    "name": "cmn-CN-Chirp3-HD-Rasalgethi",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Sadachbia",
    "name": "cmn-CN-Chirp3-HD-Sadachbia",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Sadaltager",
    "name": "cmn-CN-Chirp3-HD-Sadaltager",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Schedar",
    "name": "cmn-CN-Chirp3-HD-Schedar",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Sulafat",
    "name": "cmn-CN-Chirp3-HD-Sulafat",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Umbriel",
    "name": "cmn-CN-Chirp3-HD-Umbriel",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Vindemiatrix",
    "name": "cmn-CN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Zephyr",
    "name": "cmn-CN-Chirp3-HD-Zephyr",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Chirp3-HD-Zubenelgenubi",
    "name": "cmn-CN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Standard-A",
    "name": "cmn-CN-Standard-A",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Standard-B",
    "name": "cmn-CN-Standard-B",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Standard-C",
    "name": "cmn-CN-Standard-C",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Standard-D",
    "name": "cmn-CN-Standard-D",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Wavenet-A",
    "name": "cmn-CN-Wavenet-A",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Wavenet-B",
    "name": "cmn-CN-Wavenet-B",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Wavenet-C",
    "name": "cmn-CN-Wavenet-C",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-CN-Wavenet-D",
    "name": "cmn-CN-Wavenet-D",
    "languages": [
      "cmn-CN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-TW-Standard-A",
    "name": "cmn-TW-Standard-A",
    "languages": [
      "cmn-TW"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-TW-Standard-B",
    "name": "cmn-TW-Standard-B",
    "languages": [
      "cmn-TW"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-TW-Standard-C",
    "name": "cmn-TW-Standard-C",
    "languages": [
      "cmn-TW"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-TW-Wavenet-A",
    "name": "cmn-TW-Wavenet-A",
    "languages": [
      "cmn-TW"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-TW-Wavenet-B",
    "name": "cmn-TW-Wavenet-B",
    "languages": [
      "cmn-TW"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cmn-TW-Wavenet-C",
    "name": "cmn-TW-Wavenet-C",
    "languages": [
      "cmn-TW"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Achernar",
    "name": "cs-CZ-Chirp3-HD-Achernar",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Achird",
    "name": "cs-CZ-Chirp3-HD-Achird",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Algenib",
    "name": "cs-CZ-Chirp3-HD-Algenib",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Algieba",
    "name": "cs-CZ-Chirp3-HD-Algieba",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Alnilam",
    "name": "cs-CZ-Chirp3-HD-Alnilam",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Aoede",
    "name": "cs-CZ-Chirp3-HD-Aoede",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Autonoe",
    "name": "cs-CZ-Chirp3-HD-Autonoe",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Callirrhoe",
    "name": "cs-CZ-Chirp3-HD-Callirrhoe",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Charon",
    "name": "cs-CZ-Chirp3-HD-Charon",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Despina",
    "name": "cs-CZ-Chirp3-HD-Despina",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Enceladus",
    "name": "cs-CZ-Chirp3-HD-Enceladus",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Erinome",
    "name": "cs-CZ-Chirp3-HD-Erinome",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Fenrir",
    "name": "cs-CZ-Chirp3-HD-Fenrir",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Gacrux",
    "name": "cs-CZ-Chirp3-HD-Gacrux",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Iapetus",
    "name": "cs-CZ-Chirp3-HD-Iapetus",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Kore",
    "name": "cs-CZ-Chirp3-HD-Kore",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Laomedeia",
    "name": "cs-CZ-Chirp3-HD-Laomedeia",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Leda",
    "name": "cs-CZ-Chirp3-HD-Leda",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Orus",
    "name": "cs-CZ-Chirp3-HD-Orus",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Puck",
    "name": "cs-CZ-Chirp3-HD-Puck",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Pulcherrima",
    "name": "cs-CZ-Chirp3-HD-Pulcherrima",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Rasalgethi",
    "name": "cs-CZ-Chirp3-HD-Rasalgethi",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Sadachbia",
    "name": "cs-CZ-Chirp3-HD-Sadachbia",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Sadaltager",
    "name": "cs-CZ-Chirp3-HD-Sadaltager",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Schedar",
    "name": "cs-CZ-Chirp3-HD-Schedar",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Sulafat",
    "name": "cs-CZ-Chirp3-HD-Sulafat",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Umbriel",
    "name": "cs-CZ-Chirp3-HD-Umbriel",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Vindemiatrix",
    "name": "cs-CZ-Chirp3-HD-Vindemiatrix",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Zephyr",
    "name": "cs-CZ-Chirp3-HD-Zephyr",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Chirp3-HD-Zubenelgenubi",
    "name": "cs-CZ-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Standard-B",
    "name": "cs-CZ-Standard-B",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "cs-CZ-Wavenet-B",
    "name": "cs-CZ-Wavenet-B",
    "languages": [
      "cs-CZ"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Achernar",
    "name": "da-DK-Chirp3-HD-Achernar",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Achird",
    "name": "da-DK-Chirp3-HD-Achird",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Algenib",
    "name": "da-DK-Chirp3-HD-Algenib",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Algieba",
    "name": "da-DK-Chirp3-HD-Algieba",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Alnilam",
    "name": "da-DK-Chirp3-HD-Alnilam",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Aoede",
    "name": "da-DK-Chirp3-HD-Aoede",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Autonoe",
    "name": "da-DK-Chirp3-HD-Autonoe",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Callirrhoe",
    "name": "da-DK-Chirp3-HD-Callirrhoe",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Charon",
    "name": "da-DK-Chirp3-HD-Charon",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Despina",
    "name": "da-DK-Chirp3-HD-Despina",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Enceladus",
    "name": "da-DK-Chirp3-HD-Enceladus",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Erinome",
    "name": "da-DK-Chirp3-HD-Erinome",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Fenrir",
    "name": "da-DK-Chirp3-HD-Fenrir",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Gacrux",
    "name": "da-DK-Chirp3-HD-Gacrux",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Iapetus",
    "name": "da-DK-Chirp3-HD-Iapetus",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Kore",
    "name": "da-DK-Chirp3-HD-Kore",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Laomedeia",
    "name": "da-DK-Chirp3-HD-Laomedeia",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Leda",
    "name": "da-DK-Chirp3-HD-Leda",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Orus",
    "name": "da-DK-Chirp3-HD-Orus",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Puck",
    "name": "da-DK-Chirp3-HD-Puck",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Pulcherrima",
    "name": "da-DK-Chirp3-HD-Pulcherrima",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Rasalgethi",
    "name": "da-DK-Chirp3-HD-Rasalgethi",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Sadachbia",
    "name": "da-DK-Chirp3-HD-Sadachbia",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Sadaltager",
    "name": "da-DK-Chirp3-HD-Sadaltager",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Schedar",
    "name": "da-DK-Chirp3-HD-Schedar",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Sulafat",
    "name": "da-DK-Chirp3-HD-Sulafat",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Umbriel",
    "name": "da-DK-Chirp3-HD-Umbriel",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Vindemiatrix",
    "name": "da-DK-Chirp3-HD-Vindemiatrix",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Zephyr",
    "name": "da-DK-Chirp3-HD-Zephyr",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Chirp3-HD-Zubenelgenubi",
    "name": "da-DK-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Neural2-F",
    "name": "da-DK-Neural2-F",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Standard-F",
    "name": "da-DK-Standard-F",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Standard-G",
    "name": "da-DK-Standard-G",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Wavenet-F",
    "name": "da-DK-Wavenet-F",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "da-DK-Wavenet-G",
    "name": "da-DK-Wavenet-G",
    "languages": [
      "da-DK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp-HD-D",
    "name": "de-DE-Chirp-HD-D",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp-HD-F",
    "name": "de-DE-Chirp-HD-F",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp-HD-O",
    "name": "de-DE-Chirp-HD-O",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Achernar",
    "name": "de-DE-Chirp3-HD-Achernar",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Achird",
    "name": "de-DE-Chirp3-HD-Achird",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Algenib",
    "name": "de-DE-Chirp3-HD-Algenib",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Algieba",
    "name": "de-DE-Chirp3-HD-Algieba",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Alnilam",
    "name": "de-DE-Chirp3-HD-Alnilam",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Aoede",
    "name": "de-DE-Chirp3-HD-Aoede",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Autonoe",
    "name": "de-DE-Chirp3-HD-Autonoe",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Callirrhoe",
    "name": "de-DE-Chirp3-HD-Callirrhoe",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Charon",
    "name": "de-DE-Chirp3-HD-Charon",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Despina",
    "name": "de-DE-Chirp3-HD-Despina",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Enceladus",
    "name": "de-DE-Chirp3-HD-Enceladus",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Erinome",
    "name": "de-DE-Chirp3-HD-Erinome",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Fenrir",
    "name": "de-DE-Chirp3-HD-Fenrir",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Gacrux",
    "name": "de-DE-Chirp3-HD-Gacrux",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Iapetus",
    "name": "de-DE-Chirp3-HD-Iapetus",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Kore",
    "name": "de-DE-Chirp3-HD-Kore",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Laomedeia",
    "name": "de-DE-Chirp3-HD-Laomedeia",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Leda",
    "name": "de-DE-Chirp3-HD-Leda",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Orus",
    "name": "de-DE-Chirp3-HD-Orus",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Puck",
    "name": "de-DE-Chirp3-HD-Puck",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Pulcherrima",
    "name": "de-DE-Chirp3-HD-Pulcherrima",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Rasalgethi",
    "name": "de-DE-Chirp3-HD-Rasalgethi",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Sadachbia",
    "name": "de-DE-Chirp3-HD-Sadachbia",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Sadaltager",
    "name": "de-DE-Chirp3-HD-Sadaltager",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Schedar",
    "name": "de-DE-Chirp3-HD-Schedar",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Sulafat",
    "name": "de-DE-Chirp3-HD-Sulafat",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Umbriel",
    "name": "de-DE-Chirp3-HD-Umbriel",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Vindemiatrix",
    "name": "de-DE-Chirp3-HD-Vindemiatrix",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Zephyr",
    "name": "de-DE-Chirp3-HD-Zephyr",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Chirp3-HD-Zubenelgenubi",
    "name": "de-DE-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Neural2-G",
    "name": "de-DE-Neural2-G",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Neural2-H",
    "name": "de-DE-Neural2-H",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Polyglot-1",
    "name": "de-DE-Polyglot-1",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Standard-G",
    "name": "de-DE-Standard-G",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Standard-H",
    "name": "de-DE-Standard-H",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Studio-B",
    "name": "de-DE-Studio-B",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Studio-C",
    "name": "de-DE-Studio-C",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Wavenet-G",
    "name": "de-DE-Wavenet-G",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "de-DE-Wavenet-H",
    "name": "de-DE-Wavenet-H",
    "languages": [
      "de-DE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Achernar",
    "name": "el-GR-Chirp3-HD-Achernar",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Achird",
    "name": "el-GR-Chirp3-HD-Achird",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Algenib",
    "name": "el-GR-Chirp3-HD-Algenib",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Algieba",
    "name": "el-GR-Chirp3-HD-Algieba",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Alnilam",
    "name": "el-GR-Chirp3-HD-Alnilam",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Aoede",
    "name": "el-GR-Chirp3-HD-Aoede",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Autonoe",
    "name": "el-GR-Chirp3-HD-Autonoe",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Callirrhoe",
    "name": "el-GR-Chirp3-HD-Callirrhoe",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Charon",
    "name": "el-GR-Chirp3-HD-Charon",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Despina",
    "name": "el-GR-Chirp3-HD-Despina",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Enceladus",
    "name": "el-GR-Chirp3-HD-Enceladus",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Erinome",
    "name": "el-GR-Chirp3-HD-Erinome",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Fenrir",
    "name": "el-GR-Chirp3-HD-Fenrir",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Gacrux",
    "name": "el-GR-Chirp3-HD-Gacrux",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Iapetus",
    "name": "el-GR-Chirp3-HD-Iapetus",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Kore",
    "name": "el-GR-Chirp3-HD-Kore",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Laomedeia",
    "name": "el-GR-Chirp3-HD-Laomedeia",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Leda",
    "name": "el-GR-Chirp3-HD-Leda",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Orus",
    "name": "el-GR-Chirp3-HD-Orus",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Puck",
    "name": "el-GR-Chirp3-HD-Puck",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Pulcherrima",
    "name": "el-GR-Chirp3-HD-Pulcherrima",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Rasalgethi",
    "name": "el-GR-Chirp3-HD-Rasalgethi",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Sadachbia",
    "name": "el-GR-Chirp3-HD-Sadachbia",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Sadaltager",
    "name": "el-GR-Chirp3-HD-Sadaltager",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Schedar",
    "name": "el-GR-Chirp3-HD-Schedar",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Sulafat",
    "name": "el-GR-Chirp3-HD-Sulafat",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Umbriel",
    "name": "el-GR-Chirp3-HD-Umbriel",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Vindemiatrix",
    "name": "el-GR-Chirp3-HD-Vindemiatrix",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Zephyr",
    "name": "el-GR-Chirp3-HD-Zephyr",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Chirp3-HD-Zubenelgenubi",
    "name": "el-GR-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Standard-B",
    "name": "el-GR-Standard-B",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "el-GR-Wavenet-B",
    "name": "el-GR-Wavenet-B",
    "languages": [
      "el-GR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp-HD-D",
    "name": "en-AU-Chirp-HD-D",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp-HD-F",
    "name": "en-AU-Chirp-HD-F",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp-HD-O",
    "name": "en-AU-Chirp-HD-O",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Achernar",
    "name": "en-AU-Chirp3-HD-Achernar",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Achird",
    "name": "en-AU-Chirp3-HD-Achird",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Algenib",
    "name": "en-AU-Chirp3-HD-Algenib",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Algieba",
    "name": "en-AU-Chirp3-HD-Algieba",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Alnilam",
    "name": "en-AU-Chirp3-HD-Alnilam",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Aoede",
    "name": "en-AU-Chirp3-HD-Aoede",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Autonoe",
    "name": "en-AU-Chirp3-HD-Autonoe",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Callirrhoe",
    "name": "en-AU-Chirp3-HD-Callirrhoe",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Charon",
    "name": "en-AU-Chirp3-HD-Charon",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Despina",
    "name": "en-AU-Chirp3-HD-Despina",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Enceladus",
    "name": "en-AU-Chirp3-HD-Enceladus",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Erinome",
    "name": "en-AU-Chirp3-HD-Erinome",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Fenrir",
    "name": "en-AU-Chirp3-HD-Fenrir",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Gacrux",
    "name": "en-AU-Chirp3-HD-Gacrux",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Iapetus",
    "name": "en-AU-Chirp3-HD-Iapetus",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Kore",
    "name": "en-AU-Chirp3-HD-Kore",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Laomedeia",
    "name": "en-AU-Chirp3-HD-Laomedeia",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Leda",
    "name": "en-AU-Chirp3-HD-Leda",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Orus",
    "name": "en-AU-Chirp3-HD-Orus",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Puck",
    "name": "en-AU-Chirp3-HD-Puck",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Pulcherrima",
    "name": "en-AU-Chirp3-HD-Pulcherrima",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Rasalgethi",
    "name": "en-AU-Chirp3-HD-Rasalgethi",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Sadachbia",
    "name": "en-AU-Chirp3-HD-Sadachbia",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Sadaltager",
    "name": "en-AU-Chirp3-HD-Sadaltager",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Schedar",
    "name": "en-AU-Chirp3-HD-Schedar",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Sulafat",
    "name": "en-AU-Chirp3-HD-Sulafat",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Umbriel",
    "name": "en-AU-Chirp3-HD-Umbriel",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Vindemiatrix",
    "name": "en-AU-Chirp3-HD-Vindemiatrix",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Zephyr",
    "name": "en-AU-Chirp3-HD-Zephyr",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Chirp3-HD-Zubenelgenubi",
    "name": "en-AU-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Neural2-A",
    "name": "en-AU-Neural2-A",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Neural2-B",
    "name": "en-AU-Neural2-B",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Neural2-C",
    "name": "en-AU-Neural2-C",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Neural2-D",
    "name": "en-AU-Neural2-D",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-News-E",
    "name": "en-AU-News-E",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-News-F",
    "name": "en-AU-News-F",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-News-G",
    "name": "en-AU-News-G",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Polyglot-1",
    "name": "en-AU-Polyglot-1",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Standard-A",
    "name": "en-AU-Standard-A",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Standard-B",
    "name": "en-AU-Standard-B",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Standard-C",
    "name": "en-AU-Standard-C",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Standard-D",
    "name": "en-AU-Standard-D",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Wavenet-A",
    "name": "en-AU-Wavenet-A",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Wavenet-B",
    "name": "en-AU-Wavenet-B",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Wavenet-C",
    "name": "en-AU-Wavenet-C",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-AU-Wavenet-D",
    "name": "en-AU-Wavenet-D",
    "languages": [
      "en-AU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp-HD-D",
    "name": "en-GB-Chirp-HD-D",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp-HD-F",
    "name": "en-GB-Chirp-HD-F",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp-HD-O",
    "name": "en-GB-Chirp-HD-O",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Achernar",
    "name": "en-GB-Chirp3-HD-Achernar",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Achird",
    "name": "en-GB-Chirp3-HD-Achird",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Algenib",
    "name": "en-GB-Chirp3-HD-Algenib",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Algieba",
    "name": "en-GB-Chirp3-HD-Algieba",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Alnilam",
    "name": "en-GB-Chirp3-HD-Alnilam",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Aoede",
    "name": "en-GB-Chirp3-HD-Aoede",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Autonoe",
    "name": "en-GB-Chirp3-HD-Autonoe",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Callirrhoe",
    "name": "en-GB-Chirp3-HD-Callirrhoe",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Charon",
    "name": "en-GB-Chirp3-HD-Charon",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Despina",
    "name": "en-GB-Chirp3-HD-Despina",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Enceladus",
    "name": "en-GB-Chirp3-HD-Enceladus",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Erinome",
    "name": "en-GB-Chirp3-HD-Erinome",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Fenrir",
    "name": "en-GB-Chirp3-HD-Fenrir",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Gacrux",
    "name": "en-GB-Chirp3-HD-Gacrux",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Iapetus",
    "name": "en-GB-Chirp3-HD-Iapetus",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Kore",
    "name": "en-GB-Chirp3-HD-Kore",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Laomedeia",
    "name": "en-GB-Chirp3-HD-Laomedeia",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Leda",
    "name": "en-GB-Chirp3-HD-Leda",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Orus",
    "name": "en-GB-Chirp3-HD-Orus",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Puck",
    "name": "en-GB-Chirp3-HD-Puck",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Pulcherrima",
    "name": "en-GB-Chirp3-HD-Pulcherrima",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Rasalgethi",
    "name": "en-GB-Chirp3-HD-Rasalgethi",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Sadachbia",
    "name": "en-GB-Chirp3-HD-Sadachbia",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Sadaltager",
    "name": "en-GB-Chirp3-HD-Sadaltager",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Schedar",
    "name": "en-GB-Chirp3-HD-Schedar",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Sulafat",
    "name": "en-GB-Chirp3-HD-Sulafat",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Umbriel",
    "name": "en-GB-Chirp3-HD-Umbriel",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Vindemiatrix",
    "name": "en-GB-Chirp3-HD-Vindemiatrix",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Zephyr",
    "name": "en-GB-Chirp3-HD-Zephyr",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Chirp3-HD-Zubenelgenubi",
    "name": "en-GB-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Neural2-A",
    "name": "en-GB-Neural2-A",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Neural2-B",
    "name": "en-GB-Neural2-B",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Neural2-C",
    "name": "en-GB-Neural2-C",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Neural2-D",
    "name": "en-GB-Neural2-D",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Neural2-F",
    "name": "en-GB-Neural2-F",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Neural2-N",
    "name": "en-GB-Neural2-N",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Neural2-O",
    "name": "en-GB-Neural2-O",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-News-G",
    "name": "en-GB-News-G",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-News-H",
    "name": "en-GB-News-H",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-News-I",
    "name": "en-GB-News-I",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-News-J",
    "name": "en-GB-News-J",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-News-K",
    "name": "en-GB-News-K",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-News-L",
    "name": "en-GB-News-L",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-News-M",
    "name": "en-GB-News-M",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Standard-A",
    "name": "en-GB-Standard-A",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Standard-B",
    "name": "en-GB-Standard-B",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Standard-C",
    "name": "en-GB-Standard-C",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Standard-D",
    "name": "en-GB-Standard-D",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Standard-F",
    "name": "en-GB-Standard-F",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Standard-N",
    "name": "en-GB-Standard-N",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Standard-O",
    "name": "en-GB-Standard-O",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Studio-B",
    "name": "en-GB-Studio-B",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Studio-C",
    "name": "en-GB-Studio-C",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Wavenet-A",
    "name": "en-GB-Wavenet-A",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Wavenet-B",
    "name": "en-GB-Wavenet-B",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Wavenet-C",
    "name": "en-GB-Wavenet-C",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Wavenet-D",
    "name": "en-GB-Wavenet-D",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Wavenet-F",
    "name": "en-GB-Wavenet-F",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Wavenet-N",
    "name": "en-GB-Wavenet-N",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-GB-Wavenet-O",
    "name": "en-GB-Wavenet-O",
    "languages": [
      "en-GB"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp-HD-D",
    "name": "en-IN-Chirp-HD-D",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp-HD-F",
    "name": "en-IN-Chirp-HD-F",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp-HD-O",
    "name": "en-IN-Chirp-HD-O",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Achernar",
    "name": "en-IN-Chirp3-HD-Achernar",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Achird",
    "name": "en-IN-Chirp3-HD-Achird",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Algenib",
    "name": "en-IN-Chirp3-HD-Algenib",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Algieba",
    "name": "en-IN-Chirp3-HD-Algieba",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Alnilam",
    "name": "en-IN-Chirp3-HD-Alnilam",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Aoede",
    "name": "en-IN-Chirp3-HD-Aoede",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Autonoe",
    "name": "en-IN-Chirp3-HD-Autonoe",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Callirrhoe",
    "name": "en-IN-Chirp3-HD-Callirrhoe",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Charon",
    "name": "en-IN-Chirp3-HD-Charon",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Despina",
    "name": "en-IN-Chirp3-HD-Despina",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Enceladus",
    "name": "en-IN-Chirp3-HD-Enceladus",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Erinome",
    "name": "en-IN-Chirp3-HD-Erinome",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Fenrir",
    "name": "en-IN-Chirp3-HD-Fenrir",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Gacrux",
    "name": "en-IN-Chirp3-HD-Gacrux",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Iapetus",
    "name": "en-IN-Chirp3-HD-Iapetus",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Kore",
    "name": "en-IN-Chirp3-HD-Kore",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Laomedeia",
    "name": "en-IN-Chirp3-HD-Laomedeia",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Leda",
    "name": "en-IN-Chirp3-HD-Leda",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Orus",
    "name": "en-IN-Chirp3-HD-Orus",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Puck",
    "name": "en-IN-Chirp3-HD-Puck",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Pulcherrima",
    "name": "en-IN-Chirp3-HD-Pulcherrima",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Rasalgethi",
    "name": "en-IN-Chirp3-HD-Rasalgethi",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Sadachbia",
    "name": "en-IN-Chirp3-HD-Sadachbia",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Sadaltager",
    "name": "en-IN-Chirp3-HD-Sadaltager",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Schedar",
    "name": "en-IN-Chirp3-HD-Schedar",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Sulafat",
    "name": "en-IN-Chirp3-HD-Sulafat",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Umbriel",
    "name": "en-IN-Chirp3-HD-Umbriel",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Vindemiatrix",
    "name": "en-IN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Zephyr",
    "name": "en-IN-Chirp3-HD-Zephyr",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Chirp3-HD-Zubenelgenubi",
    "name": "en-IN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Neural2-A",
    "name": "en-IN-Neural2-A",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Neural2-B",
    "name": "en-IN-Neural2-B",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Neural2-C",
    "name": "en-IN-Neural2-C",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Neural2-D",
    "name": "en-IN-Neural2-D",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Standard-A",
    "name": "en-IN-Standard-A",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Standard-B",
    "name": "en-IN-Standard-B",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Standard-C",
    "name": "en-IN-Standard-C",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Standard-D",
    "name": "en-IN-Standard-D",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Standard-E",
    "name": "en-IN-Standard-E",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Standard-F",
    "name": "en-IN-Standard-F",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Wavenet-A",
    "name": "en-IN-Wavenet-A",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Wavenet-B",
    "name": "en-IN-Wavenet-B",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Wavenet-C",
    "name": "en-IN-Wavenet-C",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Wavenet-D",
    "name": "en-IN-Wavenet-D",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Wavenet-E",
    "name": "en-IN-Wavenet-E",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-IN-Wavenet-F",
    "name": "en-IN-Wavenet-F",
    "languages": [
      "en-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Casual-K",
    "name": "en-US-Casual-K",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp-HD-D",
    "name": "en-US-Chirp-HD-D",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp-HD-F",
    "name": "en-US-Chirp-HD-F",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp-HD-O",
    "name": "en-US-Chirp-HD-O",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Achernar",
    "name": "en-US-Chirp3-HD-Achernar",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Achird",
    "name": "en-US-Chirp3-HD-Achird",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Algenib",
    "name": "en-US-Chirp3-HD-Algenib",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Algieba",
    "name": "en-US-Chirp3-HD-Algieba",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Alnilam",
    "name": "en-US-Chirp3-HD-Alnilam",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Aoede",
    "name": "en-US-Chirp3-HD-Aoede",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Autonoe",
    "name": "en-US-Chirp3-HD-Autonoe",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Callirrhoe",
    "name": "en-US-Chirp3-HD-Callirrhoe",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Charon",
    "name": "en-US-Chirp3-HD-Charon",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Despina",
    "name": "en-US-Chirp3-HD-Despina",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Enceladus",
    "name": "en-US-Chirp3-HD-Enceladus",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Erinome",
    "name": "en-US-Chirp3-HD-Erinome",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Fenrir",
    "name": "en-US-Chirp3-HD-Fenrir",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Gacrux",
    "name": "en-US-Chirp3-HD-Gacrux",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Iapetus",
    "name": "en-US-Chirp3-HD-Iapetus",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Kore",
    "name": "en-US-Chirp3-HD-Kore",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Laomedeia",
    "name": "en-US-Chirp3-HD-Laomedeia",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Leda",
    "name": "en-US-Chirp3-HD-Leda",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Orus",
    "name": "en-US-Chirp3-HD-Orus",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Puck",
    "name": "en-US-Chirp3-HD-Puck",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Pulcherrima",
    "name": "en-US-Chirp3-HD-Pulcherrima",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Rasalgethi",
    "name": "en-US-Chirp3-HD-Rasalgethi",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Sadachbia",
    "name": "en-US-Chirp3-HD-Sadachbia",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Sadaltager",
    "name": "en-US-Chirp3-HD-Sadaltager",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Schedar",
    "name": "en-US-Chirp3-HD-Schedar",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Sulafat",
    "name": "en-US-Chirp3-HD-Sulafat",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Umbriel",
    "name": "en-US-Chirp3-HD-Umbriel",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Vindemiatrix",
    "name": "en-US-Chirp3-HD-Vindemiatrix",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Zephyr",
    "name": "en-US-Chirp3-HD-Zephyr",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Chirp3-HD-Zubenelgenubi",
    "name": "en-US-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Neural2-A",
    "name": "en-US-Neural2-A",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Neural2-C",
    "name": "en-US-Neural2-C",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Neural2-D",
    "name": "en-US-Neural2-D",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Neural2-E",
    "name": "en-US-Neural2-E",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Neural2-F",
    "name": "en-US-Neural2-F",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Neural2-G",
    "name": "en-US-Neural2-G",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Neural2-H",
    "name": "en-US-Neural2-H",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Neural2-I",
    "name": "en-US-Neural2-I",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Neural2-J",
    "name": "en-US-Neural2-J",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-News-K",
    "name": "en-US-News-K",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-News-L",
    "name": "en-US-News-L",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-News-N",
    "name": "en-US-News-N",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Polyglot-1",
    "name": "en-US-Polyglot-1",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Standard-A",
    "name": "en-US-Standard-A",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Standard-B",
    "name": "en-US-Standard-B",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Standard-C",
    "name": "en-US-Standard-C",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Standard-D",
    "name": "en-US-Standard-D",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Standard-E",
    "name": "en-US-Standard-E",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Standard-F",
    "name": "en-US-Standard-F",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Standard-G",
    "name": "en-US-Standard-G",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Standard-H",
    "name": "en-US-Standard-H",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Standard-I",
    "name": "en-US-Standard-I",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Standard-J",
    "name": "en-US-Standard-J",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Studio-O",
    "name": "en-US-Studio-O",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Studio-Q",
    "name": "en-US-Studio-Q",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Wavenet-A",
    "name": "en-US-Wavenet-A",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Wavenet-B",
    "name": "en-US-Wavenet-B",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Wavenet-C",
    "name": "en-US-Wavenet-C",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Wavenet-D",
    "name": "en-US-Wavenet-D",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Wavenet-E",
    "name": "en-US-Wavenet-E",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Wavenet-F",
    "name": "en-US-Wavenet-F",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Wavenet-G",
    "name": "en-US-Wavenet-G",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Wavenet-H",
    "name": "en-US-Wavenet-H",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Wavenet-I",
    "name": "en-US-Wavenet-I",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "en-US-Wavenet-J",
    "name": "en-US-Wavenet-J",
    "languages": [
      "en-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp-HD-D",
    "name": "es-ES-Chirp-HD-D",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp-HD-F",
    "name": "es-ES-Chirp-HD-F",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp-HD-O",
    "name": "es-ES-Chirp-HD-O",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Achernar",
    "name": "es-ES-Chirp3-HD-Achernar",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Achird",
    "name": "es-ES-Chirp3-HD-Achird",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Algenib",
    "name": "es-ES-Chirp3-HD-Algenib",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Algieba",
    "name": "es-ES-Chirp3-HD-Algieba",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Alnilam",
    "name": "es-ES-Chirp3-HD-Alnilam",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Aoede",
    "name": "es-ES-Chirp3-HD-Aoede",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Autonoe",
    "name": "es-ES-Chirp3-HD-Autonoe",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Callirrhoe",
    "name": "es-ES-Chirp3-HD-Callirrhoe",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Charon",
    "name": "es-ES-Chirp3-HD-Charon",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Despina",
    "name": "es-ES-Chirp3-HD-Despina",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Enceladus",
    "name": "es-ES-Chirp3-HD-Enceladus",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Erinome",
    "name": "es-ES-Chirp3-HD-Erinome",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Fenrir",
    "name": "es-ES-Chirp3-HD-Fenrir",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Gacrux",
    "name": "es-ES-Chirp3-HD-Gacrux",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Iapetus",
    "name": "es-ES-Chirp3-HD-Iapetus",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Kore",
    "name": "es-ES-Chirp3-HD-Kore",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Laomedeia",
    "name": "es-ES-Chirp3-HD-Laomedeia",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Leda",
    "name": "es-ES-Chirp3-HD-Leda",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Orus",
    "name": "es-ES-Chirp3-HD-Orus",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Puck",
    "name": "es-ES-Chirp3-HD-Puck",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Pulcherrima",
    "name": "es-ES-Chirp3-HD-Pulcherrima",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Rasalgethi",
    "name": "es-ES-Chirp3-HD-Rasalgethi",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Sadachbia",
    "name": "es-ES-Chirp3-HD-Sadachbia",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Sadaltager",
    "name": "es-ES-Chirp3-HD-Sadaltager",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Schedar",
    "name": "es-ES-Chirp3-HD-Schedar",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Sulafat",
    "name": "es-ES-Chirp3-HD-Sulafat",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Umbriel",
    "name": "es-ES-Chirp3-HD-Umbriel",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Vindemiatrix",
    "name": "es-ES-Chirp3-HD-Vindemiatrix",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Zephyr",
    "name": "es-ES-Chirp3-HD-Zephyr",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Chirp3-HD-Zubenelgenubi",
    "name": "es-ES-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Neural2-A",
    "name": "es-ES-Neural2-A",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Neural2-E",
    "name": "es-ES-Neural2-E",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Neural2-F",
    "name": "es-ES-Neural2-F",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Neural2-G",
    "name": "es-ES-Neural2-G",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Neural2-H",
    "name": "es-ES-Neural2-H",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Polyglot-1",
    "name": "es-ES-Polyglot-1",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Standard-E",
    "name": "es-ES-Standard-E",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Standard-F",
    "name": "es-ES-Standard-F",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Standard-G",
    "name": "es-ES-Standard-G",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Standard-H",
    "name": "es-ES-Standard-H",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Studio-C",
    "name": "es-ES-Studio-C",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Studio-F",
    "name": "es-ES-Studio-F",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Wavenet-E",
    "name": "es-ES-Wavenet-E",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Wavenet-F",
    "name": "es-ES-Wavenet-F",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Wavenet-G",
    "name": "es-ES-Wavenet-G",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-ES-Wavenet-H",
    "name": "es-ES-Wavenet-H",
    "languages": [
      "es-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp-HD-D",
    "name": "es-US-Chirp-HD-D",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp-HD-F",
    "name": "es-US-Chirp-HD-F",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp-HD-O",
    "name": "es-US-Chirp-HD-O",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Achernar",
    "name": "es-US-Chirp3-HD-Achernar",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Achird",
    "name": "es-US-Chirp3-HD-Achird",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Algenib",
    "name": "es-US-Chirp3-HD-Algenib",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Algieba",
    "name": "es-US-Chirp3-HD-Algieba",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Alnilam",
    "name": "es-US-Chirp3-HD-Alnilam",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Aoede",
    "name": "es-US-Chirp3-HD-Aoede",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Autonoe",
    "name": "es-US-Chirp3-HD-Autonoe",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Callirrhoe",
    "name": "es-US-Chirp3-HD-Callirrhoe",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Charon",
    "name": "es-US-Chirp3-HD-Charon",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Despina",
    "name": "es-US-Chirp3-HD-Despina",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Enceladus",
    "name": "es-US-Chirp3-HD-Enceladus",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Erinome",
    "name": "es-US-Chirp3-HD-Erinome",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Fenrir",
    "name": "es-US-Chirp3-HD-Fenrir",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Gacrux",
    "name": "es-US-Chirp3-HD-Gacrux",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Iapetus",
    "name": "es-US-Chirp3-HD-Iapetus",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Kore",
    "name": "es-US-Chirp3-HD-Kore",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Laomedeia",
    "name": "es-US-Chirp3-HD-Laomedeia",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Leda",
    "name": "es-US-Chirp3-HD-Leda",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Orus",
    "name": "es-US-Chirp3-HD-Orus",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Puck",
    "name": "es-US-Chirp3-HD-Puck",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Pulcherrima",
    "name": "es-US-Chirp3-HD-Pulcherrima",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Rasalgethi",
    "name": "es-US-Chirp3-HD-Rasalgethi",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Sadachbia",
    "name": "es-US-Chirp3-HD-Sadachbia",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Sadaltager",
    "name": "es-US-Chirp3-HD-Sadaltager",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Schedar",
    "name": "es-US-Chirp3-HD-Schedar",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Sulafat",
    "name": "es-US-Chirp3-HD-Sulafat",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Umbriel",
    "name": "es-US-Chirp3-HD-Umbriel",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Vindemiatrix",
    "name": "es-US-Chirp3-HD-Vindemiatrix",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Zephyr",
    "name": "es-US-Chirp3-HD-Zephyr",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Chirp3-HD-Zubenelgenubi",
    "name": "es-US-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Neural2-A",
    "name": "es-US-Neural2-A",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Neural2-B",
    "name": "es-US-Neural2-B",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Neural2-C",
    "name": "es-US-Neural2-C",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-News-D",
    "name": "es-US-News-D",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-News-E",
    "name": "es-US-News-E",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-News-F",
    "name": "es-US-News-F",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-News-G",
    "name": "es-US-News-G",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Polyglot-1",
    "name": "es-US-Polyglot-1",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Standard-A",
    "name": "es-US-Standard-A",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Standard-B",
    "name": "es-US-Standard-B",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Standard-C",
    "name": "es-US-Standard-C",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Studio-B",
    "name": "es-US-Studio-B",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Wavenet-A",
    "name": "es-US-Wavenet-A",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Wavenet-B",
    "name": "es-US-Wavenet-B",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "es-US-Wavenet-C",
    "name": "es-US-Wavenet-C",
    "languages": [
      "es-US"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Achernar",
    "name": "et-EE-Chirp3-HD-Achernar",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Achird",
    "name": "et-EE-Chirp3-HD-Achird",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Algenib",
    "name": "et-EE-Chirp3-HD-Algenib",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Algieba",
    "name": "et-EE-Chirp3-HD-Algieba",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Alnilam",
    "name": "et-EE-Chirp3-HD-Alnilam",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Aoede",
    "name": "et-EE-Chirp3-HD-Aoede",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Autonoe",
    "name": "et-EE-Chirp3-HD-Autonoe",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Callirrhoe",
    "name": "et-EE-Chirp3-HD-Callirrhoe",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Charon",
    "name": "et-EE-Chirp3-HD-Charon",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Despina",
    "name": "et-EE-Chirp3-HD-Despina",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Enceladus",
    "name": "et-EE-Chirp3-HD-Enceladus",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Erinome",
    "name": "et-EE-Chirp3-HD-Erinome",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Fenrir",
    "name": "et-EE-Chirp3-HD-Fenrir",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Gacrux",
    "name": "et-EE-Chirp3-HD-Gacrux",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Iapetus",
    "name": "et-EE-Chirp3-HD-Iapetus",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Kore",
    "name": "et-EE-Chirp3-HD-Kore",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Laomedeia",
    "name": "et-EE-Chirp3-HD-Laomedeia",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Leda",
    "name": "et-EE-Chirp3-HD-Leda",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Orus",
    "name": "et-EE-Chirp3-HD-Orus",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Puck",
    "name": "et-EE-Chirp3-HD-Puck",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Pulcherrima",
    "name": "et-EE-Chirp3-HD-Pulcherrima",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Rasalgethi",
    "name": "et-EE-Chirp3-HD-Rasalgethi",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Sadachbia",
    "name": "et-EE-Chirp3-HD-Sadachbia",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Sadaltager",
    "name": "et-EE-Chirp3-HD-Sadaltager",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Schedar",
    "name": "et-EE-Chirp3-HD-Schedar",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Sulafat",
    "name": "et-EE-Chirp3-HD-Sulafat",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Umbriel",
    "name": "et-EE-Chirp3-HD-Umbriel",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Vindemiatrix",
    "name": "et-EE-Chirp3-HD-Vindemiatrix",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Zephyr",
    "name": "et-EE-Chirp3-HD-Zephyr",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Chirp3-HD-Zubenelgenubi",
    "name": "et-EE-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "et-EE-Standard-A",
    "name": "et-EE-Standard-A",
    "languages": [
      "et-EE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "eu-ES-Standard-B",
    "name": "eu-ES-Standard-B",
    "languages": [
      "eu-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Achernar",
    "name": "fi-FI-Chirp3-HD-Achernar",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Achird",
    "name": "fi-FI-Chirp3-HD-Achird",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Algenib",
    "name": "fi-FI-Chirp3-HD-Algenib",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Algieba",
    "name": "fi-FI-Chirp3-HD-Algieba",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Alnilam",
    "name": "fi-FI-Chirp3-HD-Alnilam",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Aoede",
    "name": "fi-FI-Chirp3-HD-Aoede",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Autonoe",
    "name": "fi-FI-Chirp3-HD-Autonoe",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Callirrhoe",
    "name": "fi-FI-Chirp3-HD-Callirrhoe",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Charon",
    "name": "fi-FI-Chirp3-HD-Charon",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Despina",
    "name": "fi-FI-Chirp3-HD-Despina",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Enceladus",
    "name": "fi-FI-Chirp3-HD-Enceladus",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Erinome",
    "name": "fi-FI-Chirp3-HD-Erinome",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Fenrir",
    "name": "fi-FI-Chirp3-HD-Fenrir",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Gacrux",
    "name": "fi-FI-Chirp3-HD-Gacrux",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Iapetus",
    "name": "fi-FI-Chirp3-HD-Iapetus",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Kore",
    "name": "fi-FI-Chirp3-HD-Kore",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Laomedeia",
    "name": "fi-FI-Chirp3-HD-Laomedeia",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Leda",
    "name": "fi-FI-Chirp3-HD-Leda",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Orus",
    "name": "fi-FI-Chirp3-HD-Orus",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Puck",
    "name": "fi-FI-Chirp3-HD-Puck",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Pulcherrima",
    "name": "fi-FI-Chirp3-HD-Pulcherrima",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Rasalgethi",
    "name": "fi-FI-Chirp3-HD-Rasalgethi",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Sadachbia",
    "name": "fi-FI-Chirp3-HD-Sadachbia",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Sadaltager",
    "name": "fi-FI-Chirp3-HD-Sadaltager",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Schedar",
    "name": "fi-FI-Chirp3-HD-Schedar",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Sulafat",
    "name": "fi-FI-Chirp3-HD-Sulafat",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Umbriel",
    "name": "fi-FI-Chirp3-HD-Umbriel",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Vindemiatrix",
    "name": "fi-FI-Chirp3-HD-Vindemiatrix",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Zephyr",
    "name": "fi-FI-Chirp3-HD-Zephyr",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Chirp3-HD-Zubenelgenubi",
    "name": "fi-FI-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Standard-B",
    "name": "fi-FI-Standard-B",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fi-FI-Wavenet-B",
    "name": "fi-FI-Wavenet-B",
    "languages": [
      "fi-FI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fil-PH-Standard-A",
    "name": "fil-PH-Standard-A",
    "languages": [
      "fil-PH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fil-PH-Standard-B",
    "name": "fil-PH-Standard-B",
    "languages": [
      "fil-PH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fil-PH-Standard-C",
    "name": "fil-PH-Standard-C",
    "languages": [
      "fil-PH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fil-PH-Standard-D",
    "name": "fil-PH-Standard-D",
    "languages": [
      "fil-PH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fil-PH-Wavenet-A",
    "name": "fil-PH-Wavenet-A",
    "languages": [
      "fil-PH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fil-PH-Wavenet-B",
    "name": "fil-PH-Wavenet-B",
    "languages": [
      "fil-PH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fil-PH-Wavenet-C",
    "name": "fil-PH-Wavenet-C",
    "languages": [
      "fil-PH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fil-PH-Wavenet-D",
    "name": "fil-PH-Wavenet-D",
    "languages": [
      "fil-PH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fil-ph-Neural2-A",
    "name": "fil-ph-Neural2-A",
    "languages": [
      "fil-PH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fil-ph-Neural2-D",
    "name": "fil-ph-Neural2-D",
    "languages": [
      "fil-PH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp-HD-D",
    "name": "fr-CA-Chirp-HD-D",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp-HD-F",
    "name": "fr-CA-Chirp-HD-F",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp-HD-O",
    "name": "fr-CA-Chirp-HD-O",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Achernar",
    "name": "fr-CA-Chirp3-HD-Achernar",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Achird",
    "name": "fr-CA-Chirp3-HD-Achird",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Algenib",
    "name": "fr-CA-Chirp3-HD-Algenib",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Algieba",
    "name": "fr-CA-Chirp3-HD-Algieba",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Alnilam",
    "name": "fr-CA-Chirp3-HD-Alnilam",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Aoede",
    "name": "fr-CA-Chirp3-HD-Aoede",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Autonoe",
    "name": "fr-CA-Chirp3-HD-Autonoe",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Callirrhoe",
    "name": "fr-CA-Chirp3-HD-Callirrhoe",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Charon",
    "name": "fr-CA-Chirp3-HD-Charon",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Despina",
    "name": "fr-CA-Chirp3-HD-Despina",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Enceladus",
    "name": "fr-CA-Chirp3-HD-Enceladus",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Erinome",
    "name": "fr-CA-Chirp3-HD-Erinome",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Fenrir",
    "name": "fr-CA-Chirp3-HD-Fenrir",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Gacrux",
    "name": "fr-CA-Chirp3-HD-Gacrux",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Iapetus",
    "name": "fr-CA-Chirp3-HD-Iapetus",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Kore",
    "name": "fr-CA-Chirp3-HD-Kore",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Laomedeia",
    "name": "fr-CA-Chirp3-HD-Laomedeia",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Leda",
    "name": "fr-CA-Chirp3-HD-Leda",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Orus",
    "name": "fr-CA-Chirp3-HD-Orus",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Puck",
    "name": "fr-CA-Chirp3-HD-Puck",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Pulcherrima",
    "name": "fr-CA-Chirp3-HD-Pulcherrima",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Rasalgethi",
    "name": "fr-CA-Chirp3-HD-Rasalgethi",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Sadachbia",
    "name": "fr-CA-Chirp3-HD-Sadachbia",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Sadaltager",
    "name": "fr-CA-Chirp3-HD-Sadaltager",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Schedar",
    "name": "fr-CA-Chirp3-HD-Schedar",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Sulafat",
    "name": "fr-CA-Chirp3-HD-Sulafat",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Umbriel",
    "name": "fr-CA-Chirp3-HD-Umbriel",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Vindemiatrix",
    "name": "fr-CA-Chirp3-HD-Vindemiatrix",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Zephyr",
    "name": "fr-CA-Chirp3-HD-Zephyr",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Chirp3-HD-Zubenelgenubi",
    "name": "fr-CA-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Neural2-A",
    "name": "fr-CA-Neural2-A",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Neural2-B",
    "name": "fr-CA-Neural2-B",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Neural2-C",
    "name": "fr-CA-Neural2-C",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Neural2-D",
    "name": "fr-CA-Neural2-D",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Standard-A",
    "name": "fr-CA-Standard-A",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Standard-B",
    "name": "fr-CA-Standard-B",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Standard-C",
    "name": "fr-CA-Standard-C",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Standard-D",
    "name": "fr-CA-Standard-D",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Wavenet-A",
    "name": "fr-CA-Wavenet-A",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Wavenet-B",
    "name": "fr-CA-Wavenet-B",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Wavenet-C",
    "name": "fr-CA-Wavenet-C",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-CA-Wavenet-D",
    "name": "fr-CA-Wavenet-D",
    "languages": [
      "fr-CA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp-HD-D",
    "name": "fr-FR-Chirp-HD-D",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp-HD-F",
    "name": "fr-FR-Chirp-HD-F",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp-HD-O",
    "name": "fr-FR-Chirp-HD-O",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Achernar",
    "name": "fr-FR-Chirp3-HD-Achernar",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Achird",
    "name": "fr-FR-Chirp3-HD-Achird",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Algenib",
    "name": "fr-FR-Chirp3-HD-Algenib",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Algieba",
    "name": "fr-FR-Chirp3-HD-Algieba",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Alnilam",
    "name": "fr-FR-Chirp3-HD-Alnilam",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Aoede",
    "name": "fr-FR-Chirp3-HD-Aoede",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Autonoe",
    "name": "fr-FR-Chirp3-HD-Autonoe",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Callirrhoe",
    "name": "fr-FR-Chirp3-HD-Callirrhoe",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Charon",
    "name": "fr-FR-Chirp3-HD-Charon",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Despina",
    "name": "fr-FR-Chirp3-HD-Despina",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Enceladus",
    "name": "fr-FR-Chirp3-HD-Enceladus",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Erinome",
    "name": "fr-FR-Chirp3-HD-Erinome",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Fenrir",
    "name": "fr-FR-Chirp3-HD-Fenrir",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Gacrux",
    "name": "fr-FR-Chirp3-HD-Gacrux",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Iapetus",
    "name": "fr-FR-Chirp3-HD-Iapetus",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Kore",
    "name": "fr-FR-Chirp3-HD-Kore",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Laomedeia",
    "name": "fr-FR-Chirp3-HD-Laomedeia",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Leda",
    "name": "fr-FR-Chirp3-HD-Leda",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Orus",
    "name": "fr-FR-Chirp3-HD-Orus",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Puck",
    "name": "fr-FR-Chirp3-HD-Puck",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Pulcherrima",
    "name": "fr-FR-Chirp3-HD-Pulcherrima",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Rasalgethi",
    "name": "fr-FR-Chirp3-HD-Rasalgethi",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Sadachbia",
    "name": "fr-FR-Chirp3-HD-Sadachbia",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Sadaltager",
    "name": "fr-FR-Chirp3-HD-Sadaltager",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Schedar",
    "name": "fr-FR-Chirp3-HD-Schedar",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Sulafat",
    "name": "fr-FR-Chirp3-HD-Sulafat",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Umbriel",
    "name": "fr-FR-Chirp3-HD-Umbriel",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Vindemiatrix",
    "name": "fr-FR-Chirp3-HD-Vindemiatrix",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Zephyr",
    "name": "fr-FR-Chirp3-HD-Zephyr",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Chirp3-HD-Zubenelgenubi",
    "name": "fr-FR-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Neural2-F",
    "name": "fr-FR-Neural2-F",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Neural2-G",
    "name": "fr-FR-Neural2-G",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Polyglot-1",
    "name": "fr-FR-Polyglot-1",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Standard-F",
    "name": "fr-FR-Standard-F",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Standard-G",
    "name": "fr-FR-Standard-G",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Studio-A",
    "name": "fr-FR-Studio-A",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Studio-D",
    "name": "fr-FR-Studio-D",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Wavenet-F",
    "name": "fr-FR-Wavenet-F",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "fr-FR-Wavenet-G",
    "name": "fr-FR-Wavenet-G",
    "languages": [
      "fr-FR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gl-ES-Standard-B",
    "name": "gl-ES-Standard-B",
    "languages": [
      "gl-ES"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Achernar",
    "name": "gu-IN-Chirp3-HD-Achernar",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Achird",
    "name": "gu-IN-Chirp3-HD-Achird",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Algenib",
    "name": "gu-IN-Chirp3-HD-Algenib",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Algieba",
    "name": "gu-IN-Chirp3-HD-Algieba",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Alnilam",
    "name": "gu-IN-Chirp3-HD-Alnilam",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Aoede",
    "name": "gu-IN-Chirp3-HD-Aoede",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Autonoe",
    "name": "gu-IN-Chirp3-HD-Autonoe",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Callirrhoe",
    "name": "gu-IN-Chirp3-HD-Callirrhoe",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Charon",
    "name": "gu-IN-Chirp3-HD-Charon",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Despina",
    "name": "gu-IN-Chirp3-HD-Despina",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Enceladus",
    "name": "gu-IN-Chirp3-HD-Enceladus",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Erinome",
    "name": "gu-IN-Chirp3-HD-Erinome",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Fenrir",
    "name": "gu-IN-Chirp3-HD-Fenrir",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Gacrux",
    "name": "gu-IN-Chirp3-HD-Gacrux",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Iapetus",
    "name": "gu-IN-Chirp3-HD-Iapetus",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Kore",
    "name": "gu-IN-Chirp3-HD-Kore",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Laomedeia",
    "name": "gu-IN-Chirp3-HD-Laomedeia",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Leda",
    "name": "gu-IN-Chirp3-HD-Leda",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Orus",
    "name": "gu-IN-Chirp3-HD-Orus",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Puck",
    "name": "gu-IN-Chirp3-HD-Puck",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Pulcherrima",
    "name": "gu-IN-Chirp3-HD-Pulcherrima",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Rasalgethi",
    "name": "gu-IN-Chirp3-HD-Rasalgethi",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Sadachbia",
    "name": "gu-IN-Chirp3-HD-Sadachbia",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Sadaltager",
    "name": "gu-IN-Chirp3-HD-Sadaltager",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Schedar",
    "name": "gu-IN-Chirp3-HD-Schedar",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Sulafat",
    "name": "gu-IN-Chirp3-HD-Sulafat",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Umbriel",
    "name": "gu-IN-Chirp3-HD-Umbriel",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Vindemiatrix",
    "name": "gu-IN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Zephyr",
    "name": "gu-IN-Chirp3-HD-Zephyr",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Chirp3-HD-Zubenelgenubi",
    "name": "gu-IN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Standard-A",
    "name": "gu-IN-Standard-A",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Standard-B",
    "name": "gu-IN-Standard-B",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Standard-C",
    "name": "gu-IN-Standard-C",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Standard-D",
    "name": "gu-IN-Standard-D",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Wavenet-A",
    "name": "gu-IN-Wavenet-A",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Wavenet-B",
    "name": "gu-IN-Wavenet-B",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Wavenet-C",
    "name": "gu-IN-Wavenet-C",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "gu-IN-Wavenet-D",
    "name": "gu-IN-Wavenet-D",
    "languages": [
      "gu-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Achernar",
    "name": "he-IL-Chirp3-HD-Achernar",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Achird",
    "name": "he-IL-Chirp3-HD-Achird",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Algenib",
    "name": "he-IL-Chirp3-HD-Algenib",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Algieba",
    "name": "he-IL-Chirp3-HD-Algieba",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Alnilam",
    "name": "he-IL-Chirp3-HD-Alnilam",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Aoede",
    "name": "he-IL-Chirp3-HD-Aoede",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Autonoe",
    "name": "he-IL-Chirp3-HD-Autonoe",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Callirrhoe",
    "name": "he-IL-Chirp3-HD-Callirrhoe",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Charon",
    "name": "he-IL-Chirp3-HD-Charon",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Despina",
    "name": "he-IL-Chirp3-HD-Despina",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Enceladus",
    "name": "he-IL-Chirp3-HD-Enceladus",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Erinome",
    "name": "he-IL-Chirp3-HD-Erinome",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Fenrir",
    "name": "he-IL-Chirp3-HD-Fenrir",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Gacrux",
    "name": "he-IL-Chirp3-HD-Gacrux",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Iapetus",
    "name": "he-IL-Chirp3-HD-Iapetus",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Kore",
    "name": "he-IL-Chirp3-HD-Kore",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Laomedeia",
    "name": "he-IL-Chirp3-HD-Laomedeia",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Leda",
    "name": "he-IL-Chirp3-HD-Leda",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Orus",
    "name": "he-IL-Chirp3-HD-Orus",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Puck",
    "name": "he-IL-Chirp3-HD-Puck",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Pulcherrima",
    "name": "he-IL-Chirp3-HD-Pulcherrima",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Rasalgethi",
    "name": "he-IL-Chirp3-HD-Rasalgethi",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Sadachbia",
    "name": "he-IL-Chirp3-HD-Sadachbia",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Sadaltager",
    "name": "he-IL-Chirp3-HD-Sadaltager",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Schedar",
    "name": "he-IL-Chirp3-HD-Schedar",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Sulafat",
    "name": "he-IL-Chirp3-HD-Sulafat",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Umbriel",
    "name": "he-IL-Chirp3-HD-Umbriel",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Vindemiatrix",
    "name": "he-IL-Chirp3-HD-Vindemiatrix",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Zephyr",
    "name": "he-IL-Chirp3-HD-Zephyr",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Chirp3-HD-Zubenelgenubi",
    "name": "he-IL-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Standard-A",
    "name": "he-IL-Standard-A",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Standard-B",
    "name": "he-IL-Standard-B",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Standard-C",
    "name": "he-IL-Standard-C",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Standard-D",
    "name": "he-IL-Standard-D",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Wavenet-A",
    "name": "he-IL-Wavenet-A",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Wavenet-B",
    "name": "he-IL-Wavenet-B",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Wavenet-C",
    "name": "he-IL-Wavenet-C",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "he-IL-Wavenet-D",
    "name": "he-IL-Wavenet-D",
    "languages": [
      "he-IL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Achernar",
    "name": "hi-IN-Chirp3-HD-Achernar",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Achird",
    "name": "hi-IN-Chirp3-HD-Achird",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Algenib",
    "name": "hi-IN-Chirp3-HD-Algenib",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Algieba",
    "name": "hi-IN-Chirp3-HD-Algieba",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Alnilam",
    "name": "hi-IN-Chirp3-HD-Alnilam",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Aoede",
    "name": "hi-IN-Chirp3-HD-Aoede",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Autonoe",
    "name": "hi-IN-Chirp3-HD-Autonoe",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Callirrhoe",
    "name": "hi-IN-Chirp3-HD-Callirrhoe",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Charon",
    "name": "hi-IN-Chirp3-HD-Charon",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Despina",
    "name": "hi-IN-Chirp3-HD-Despina",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Enceladus",
    "name": "hi-IN-Chirp3-HD-Enceladus",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Erinome",
    "name": "hi-IN-Chirp3-HD-Erinome",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Fenrir",
    "name": "hi-IN-Chirp3-HD-Fenrir",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Gacrux",
    "name": "hi-IN-Chirp3-HD-Gacrux",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Iapetus",
    "name": "hi-IN-Chirp3-HD-Iapetus",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Kore",
    "name": "hi-IN-Chirp3-HD-Kore",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Laomedeia",
    "name": "hi-IN-Chirp3-HD-Laomedeia",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Leda",
    "name": "hi-IN-Chirp3-HD-Leda",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Orus",
    "name": "hi-IN-Chirp3-HD-Orus",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Puck",
    "name": "hi-IN-Chirp3-HD-Puck",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Pulcherrima",
    "name": "hi-IN-Chirp3-HD-Pulcherrima",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Rasalgethi",
    "name": "hi-IN-Chirp3-HD-Rasalgethi",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Sadachbia",
    "name": "hi-IN-Chirp3-HD-Sadachbia",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Sadaltager",
    "name": "hi-IN-Chirp3-HD-Sadaltager",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Schedar",
    "name": "hi-IN-Chirp3-HD-Schedar",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Sulafat",
    "name": "hi-IN-Chirp3-HD-Sulafat",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Umbriel",
    "name": "hi-IN-Chirp3-HD-Umbriel",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Vindemiatrix",
    "name": "hi-IN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Zephyr",
    "name": "hi-IN-Chirp3-HD-Zephyr",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Chirp3-HD-Zubenelgenubi",
    "name": "hi-IN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Neural2-A",
    "name": "hi-IN-Neural2-A",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Neural2-B",
    "name": "hi-IN-Neural2-B",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Neural2-C",
    "name": "hi-IN-Neural2-C",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Neural2-D",
    "name": "hi-IN-Neural2-D",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Standard-A",
    "name": "hi-IN-Standard-A",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Standard-B",
    "name": "hi-IN-Standard-B",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Standard-C",
    "name": "hi-IN-Standard-C",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Standard-D",
    "name": "hi-IN-Standard-D",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Standard-E",
    "name": "hi-IN-Standard-E",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Standard-F",
    "name": "hi-IN-Standard-F",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Wavenet-A",
    "name": "hi-IN-Wavenet-A",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Wavenet-B",
    "name": "hi-IN-Wavenet-B",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Wavenet-C",
    "name": "hi-IN-Wavenet-C",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Wavenet-D",
    "name": "hi-IN-Wavenet-D",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Wavenet-E",
    "name": "hi-IN-Wavenet-E",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hi-IN-Wavenet-F",
    "name": "hi-IN-Wavenet-F",
    "languages": [
      "hi-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Achernar",
    "name": "hr-HR-Chirp3-HD-Achernar",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Achird",
    "name": "hr-HR-Chirp3-HD-Achird",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Algenib",
    "name": "hr-HR-Chirp3-HD-Algenib",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Algieba",
    "name": "hr-HR-Chirp3-HD-Algieba",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Alnilam",
    "name": "hr-HR-Chirp3-HD-Alnilam",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Aoede",
    "name": "hr-HR-Chirp3-HD-Aoede",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Autonoe",
    "name": "hr-HR-Chirp3-HD-Autonoe",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Callirrhoe",
    "name": "hr-HR-Chirp3-HD-Callirrhoe",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Charon",
    "name": "hr-HR-Chirp3-HD-Charon",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Despina",
    "name": "hr-HR-Chirp3-HD-Despina",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Enceladus",
    "name": "hr-HR-Chirp3-HD-Enceladus",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Erinome",
    "name": "hr-HR-Chirp3-HD-Erinome",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Fenrir",
    "name": "hr-HR-Chirp3-HD-Fenrir",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Gacrux",
    "name": "hr-HR-Chirp3-HD-Gacrux",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Iapetus",
    "name": "hr-HR-Chirp3-HD-Iapetus",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Kore",
    "name": "hr-HR-Chirp3-HD-Kore",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Laomedeia",
    "name": "hr-HR-Chirp3-HD-Laomedeia",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Leda",
    "name": "hr-HR-Chirp3-HD-Leda",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Orus",
    "name": "hr-HR-Chirp3-HD-Orus",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Puck",
    "name": "hr-HR-Chirp3-HD-Puck",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Pulcherrima",
    "name": "hr-HR-Chirp3-HD-Pulcherrima",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Rasalgethi",
    "name": "hr-HR-Chirp3-HD-Rasalgethi",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Sadachbia",
    "name": "hr-HR-Chirp3-HD-Sadachbia",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Sadaltager",
    "name": "hr-HR-Chirp3-HD-Sadaltager",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Schedar",
    "name": "hr-HR-Chirp3-HD-Schedar",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Sulafat",
    "name": "hr-HR-Chirp3-HD-Sulafat",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Umbriel",
    "name": "hr-HR-Chirp3-HD-Umbriel",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Vindemiatrix",
    "name": "hr-HR-Chirp3-HD-Vindemiatrix",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Zephyr",
    "name": "hr-HR-Chirp3-HD-Zephyr",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hr-HR-Chirp3-HD-Zubenelgenubi",
    "name": "hr-HR-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "hr-HR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Achernar",
    "name": "hu-HU-Chirp3-HD-Achernar",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Achird",
    "name": "hu-HU-Chirp3-HD-Achird",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Algenib",
    "name": "hu-HU-Chirp3-HD-Algenib",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Algieba",
    "name": "hu-HU-Chirp3-HD-Algieba",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Alnilam",
    "name": "hu-HU-Chirp3-HD-Alnilam",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Aoede",
    "name": "hu-HU-Chirp3-HD-Aoede",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Autonoe",
    "name": "hu-HU-Chirp3-HD-Autonoe",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Callirrhoe",
    "name": "hu-HU-Chirp3-HD-Callirrhoe",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Charon",
    "name": "hu-HU-Chirp3-HD-Charon",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Despina",
    "name": "hu-HU-Chirp3-HD-Despina",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Enceladus",
    "name": "hu-HU-Chirp3-HD-Enceladus",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Erinome",
    "name": "hu-HU-Chirp3-HD-Erinome",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Fenrir",
    "name": "hu-HU-Chirp3-HD-Fenrir",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Gacrux",
    "name": "hu-HU-Chirp3-HD-Gacrux",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Iapetus",
    "name": "hu-HU-Chirp3-HD-Iapetus",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Kore",
    "name": "hu-HU-Chirp3-HD-Kore",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Laomedeia",
    "name": "hu-HU-Chirp3-HD-Laomedeia",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Leda",
    "name": "hu-HU-Chirp3-HD-Leda",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Orus",
    "name": "hu-HU-Chirp3-HD-Orus",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Puck",
    "name": "hu-HU-Chirp3-HD-Puck",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Pulcherrima",
    "name": "hu-HU-Chirp3-HD-Pulcherrima",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Rasalgethi",
    "name": "hu-HU-Chirp3-HD-Rasalgethi",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Sadachbia",
    "name": "hu-HU-Chirp3-HD-Sadachbia",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Sadaltager",
    "name": "hu-HU-Chirp3-HD-Sadaltager",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Schedar",
    "name": "hu-HU-Chirp3-HD-Schedar",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Sulafat",
    "name": "hu-HU-Chirp3-HD-Sulafat",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Umbriel",
    "name": "hu-HU-Chirp3-HD-Umbriel",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Vindemiatrix",
    "name": "hu-HU-Chirp3-HD-Vindemiatrix",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Zephyr",
    "name": "hu-HU-Chirp3-HD-Zephyr",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Chirp3-HD-Zubenelgenubi",
    "name": "hu-HU-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Standard-B",
    "name": "hu-HU-Standard-B",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "hu-HU-Wavenet-B",
    "name": "hu-HU-Wavenet-B",
    "languages": [
      "hu-HU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Achernar",
    "name": "id-ID-Chirp3-HD-Achernar",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Achird",
    "name": "id-ID-Chirp3-HD-Achird",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Algenib",
    "name": "id-ID-Chirp3-HD-Algenib",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Algieba",
    "name": "id-ID-Chirp3-HD-Algieba",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Alnilam",
    "name": "id-ID-Chirp3-HD-Alnilam",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Aoede",
    "name": "id-ID-Chirp3-HD-Aoede",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Autonoe",
    "name": "id-ID-Chirp3-HD-Autonoe",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Callirrhoe",
    "name": "id-ID-Chirp3-HD-Callirrhoe",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Charon",
    "name": "id-ID-Chirp3-HD-Charon",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Despina",
    "name": "id-ID-Chirp3-HD-Despina",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Enceladus",
    "name": "id-ID-Chirp3-HD-Enceladus",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Erinome",
    "name": "id-ID-Chirp3-HD-Erinome",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Fenrir",
    "name": "id-ID-Chirp3-HD-Fenrir",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Gacrux",
    "name": "id-ID-Chirp3-HD-Gacrux",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Iapetus",
    "name": "id-ID-Chirp3-HD-Iapetus",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Kore",
    "name": "id-ID-Chirp3-HD-Kore",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Laomedeia",
    "name": "id-ID-Chirp3-HD-Laomedeia",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Leda",
    "name": "id-ID-Chirp3-HD-Leda",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Orus",
    "name": "id-ID-Chirp3-HD-Orus",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Puck",
    "name": "id-ID-Chirp3-HD-Puck",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Pulcherrima",
    "name": "id-ID-Chirp3-HD-Pulcherrima",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Rasalgethi",
    "name": "id-ID-Chirp3-HD-Rasalgethi",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Sadachbia",
    "name": "id-ID-Chirp3-HD-Sadachbia",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Sadaltager",
    "name": "id-ID-Chirp3-HD-Sadaltager",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Schedar",
    "name": "id-ID-Chirp3-HD-Schedar",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Sulafat",
    "name": "id-ID-Chirp3-HD-Sulafat",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Umbriel",
    "name": "id-ID-Chirp3-HD-Umbriel",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Vindemiatrix",
    "name": "id-ID-Chirp3-HD-Vindemiatrix",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Zephyr",
    "name": "id-ID-Chirp3-HD-Zephyr",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Chirp3-HD-Zubenelgenubi",
    "name": "id-ID-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Standard-A",
    "name": "id-ID-Standard-A",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Standard-B",
    "name": "id-ID-Standard-B",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Standard-C",
    "name": "id-ID-Standard-C",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Standard-D",
    "name": "id-ID-Standard-D",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Wavenet-A",
    "name": "id-ID-Wavenet-A",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Wavenet-B",
    "name": "id-ID-Wavenet-B",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Wavenet-C",
    "name": "id-ID-Wavenet-C",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "id-ID-Wavenet-D",
    "name": "id-ID-Wavenet-D",
    "languages": [
      "id-ID"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "is-IS-Standard-B",
    "name": "is-IS-Standard-B",
    "languages": [
      "is-IS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp-HD-D",
    "name": "it-IT-Chirp-HD-D",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp-HD-F",
    "name": "it-IT-Chirp-HD-F",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp-HD-O",
    "name": "it-IT-Chirp-HD-O",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Achernar",
    "name": "it-IT-Chirp3-HD-Achernar",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Achird",
    "name": "it-IT-Chirp3-HD-Achird",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Algenib",
    "name": "it-IT-Chirp3-HD-Algenib",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Algieba",
    "name": "it-IT-Chirp3-HD-Algieba",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Alnilam",
    "name": "it-IT-Chirp3-HD-Alnilam",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Aoede",
    "name": "it-IT-Chirp3-HD-Aoede",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Autonoe",
    "name": "it-IT-Chirp3-HD-Autonoe",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Callirrhoe",
    "name": "it-IT-Chirp3-HD-Callirrhoe",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Charon",
    "name": "it-IT-Chirp3-HD-Charon",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Despina",
    "name": "it-IT-Chirp3-HD-Despina",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Enceladus",
    "name": "it-IT-Chirp3-HD-Enceladus",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Erinome",
    "name": "it-IT-Chirp3-HD-Erinome",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Fenrir",
    "name": "it-IT-Chirp3-HD-Fenrir",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Gacrux",
    "name": "it-IT-Chirp3-HD-Gacrux",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Iapetus",
    "name": "it-IT-Chirp3-HD-Iapetus",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Kore",
    "name": "it-IT-Chirp3-HD-Kore",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Laomedeia",
    "name": "it-IT-Chirp3-HD-Laomedeia",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Leda",
    "name": "it-IT-Chirp3-HD-Leda",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Orus",
    "name": "it-IT-Chirp3-HD-Orus",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Puck",
    "name": "it-IT-Chirp3-HD-Puck",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Pulcherrima",
    "name": "it-IT-Chirp3-HD-Pulcherrima",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Rasalgethi",
    "name": "it-IT-Chirp3-HD-Rasalgethi",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Sadachbia",
    "name": "it-IT-Chirp3-HD-Sadachbia",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Sadaltager",
    "name": "it-IT-Chirp3-HD-Sadaltager",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Schedar",
    "name": "it-IT-Chirp3-HD-Schedar",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Sulafat",
    "name": "it-IT-Chirp3-HD-Sulafat",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Umbriel",
    "name": "it-IT-Chirp3-HD-Umbriel",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Vindemiatrix",
    "name": "it-IT-Chirp3-HD-Vindemiatrix",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Zephyr",
    "name": "it-IT-Chirp3-HD-Zephyr",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Chirp3-HD-Zubenelgenubi",
    "name": "it-IT-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Neural2-A",
    "name": "it-IT-Neural2-A",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Neural2-E",
    "name": "it-IT-Neural2-E",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Neural2-F",
    "name": "it-IT-Neural2-F",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Standard-E",
    "name": "it-IT-Standard-E",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Standard-F",
    "name": "it-IT-Standard-F",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Wavenet-E",
    "name": "it-IT-Wavenet-E",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "it-IT-Wavenet-F",
    "name": "it-IT-Wavenet-F",
    "languages": [
      "it-IT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Achernar",
    "name": "ja-JP-Chirp3-HD-Achernar",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Achird",
    "name": "ja-JP-Chirp3-HD-Achird",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Algenib",
    "name": "ja-JP-Chirp3-HD-Algenib",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Algieba",
    "name": "ja-JP-Chirp3-HD-Algieba",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Alnilam",
    "name": "ja-JP-Chirp3-HD-Alnilam",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Aoede",
    "name": "ja-JP-Chirp3-HD-Aoede",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Autonoe",
    "name": "ja-JP-Chirp3-HD-Autonoe",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Callirrhoe",
    "name": "ja-JP-Chirp3-HD-Callirrhoe",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Charon",
    "name": "ja-JP-Chirp3-HD-Charon",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Despina",
    "name": "ja-JP-Chirp3-HD-Despina",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Enceladus",
    "name": "ja-JP-Chirp3-HD-Enceladus",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Erinome",
    "name": "ja-JP-Chirp3-HD-Erinome",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Fenrir",
    "name": "ja-JP-Chirp3-HD-Fenrir",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Gacrux",
    "name": "ja-JP-Chirp3-HD-Gacrux",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Iapetus",
    "name": "ja-JP-Chirp3-HD-Iapetus",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Kore",
    "name": "ja-JP-Chirp3-HD-Kore",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Laomedeia",
    "name": "ja-JP-Chirp3-HD-Laomedeia",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Leda",
    "name": "ja-JP-Chirp3-HD-Leda",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Orus",
    "name": "ja-JP-Chirp3-HD-Orus",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Puck",
    "name": "ja-JP-Chirp3-HD-Puck",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Pulcherrima",
    "name": "ja-JP-Chirp3-HD-Pulcherrima",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Rasalgethi",
    "name": "ja-JP-Chirp3-HD-Rasalgethi",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Sadachbia",
    "name": "ja-JP-Chirp3-HD-Sadachbia",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Sadaltager",
    "name": "ja-JP-Chirp3-HD-Sadaltager",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Schedar",
    "name": "ja-JP-Chirp3-HD-Schedar",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Sulafat",
    "name": "ja-JP-Chirp3-HD-Sulafat",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Umbriel",
    "name": "ja-JP-Chirp3-HD-Umbriel",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Vindemiatrix",
    "name": "ja-JP-Chirp3-HD-Vindemiatrix",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Zephyr",
    "name": "ja-JP-Chirp3-HD-Zephyr",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Chirp3-HD-Zubenelgenubi",
    "name": "ja-JP-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Neural2-B",
    "name": "ja-JP-Neural2-B",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Neural2-C",
    "name": "ja-JP-Neural2-C",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Neural2-D",
    "name": "ja-JP-Neural2-D",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Standard-A",
    "name": "ja-JP-Standard-A",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Standard-B",
    "name": "ja-JP-Standard-B",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Standard-C",
    "name": "ja-JP-Standard-C",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Standard-D",
    "name": "ja-JP-Standard-D",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Wavenet-A",
    "name": "ja-JP-Wavenet-A",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Wavenet-B",
    "name": "ja-JP-Wavenet-B",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Wavenet-C",
    "name": "ja-JP-Wavenet-C",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ja-JP-Wavenet-D",
    "name": "ja-JP-Wavenet-D",
    "languages": [
      "ja-JP"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Achernar",
    "name": "kn-IN-Chirp3-HD-Achernar",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Achird",
    "name": "kn-IN-Chirp3-HD-Achird",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Algenib",
    "name": "kn-IN-Chirp3-HD-Algenib",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Algieba",
    "name": "kn-IN-Chirp3-HD-Algieba",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Alnilam",
    "name": "kn-IN-Chirp3-HD-Alnilam",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Aoede",
    "name": "kn-IN-Chirp3-HD-Aoede",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Autonoe",
    "name": "kn-IN-Chirp3-HD-Autonoe",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Callirrhoe",
    "name": "kn-IN-Chirp3-HD-Callirrhoe",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Charon",
    "name": "kn-IN-Chirp3-HD-Charon",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Despina",
    "name": "kn-IN-Chirp3-HD-Despina",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Enceladus",
    "name": "kn-IN-Chirp3-HD-Enceladus",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Erinome",
    "name": "kn-IN-Chirp3-HD-Erinome",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Fenrir",
    "name": "kn-IN-Chirp3-HD-Fenrir",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Gacrux",
    "name": "kn-IN-Chirp3-HD-Gacrux",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Iapetus",
    "name": "kn-IN-Chirp3-HD-Iapetus",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Kore",
    "name": "kn-IN-Chirp3-HD-Kore",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Laomedeia",
    "name": "kn-IN-Chirp3-HD-Laomedeia",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Leda",
    "name": "kn-IN-Chirp3-HD-Leda",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Orus",
    "name": "kn-IN-Chirp3-HD-Orus",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Puck",
    "name": "kn-IN-Chirp3-HD-Puck",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Pulcherrima",
    "name": "kn-IN-Chirp3-HD-Pulcherrima",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Rasalgethi",
    "name": "kn-IN-Chirp3-HD-Rasalgethi",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Sadachbia",
    "name": "kn-IN-Chirp3-HD-Sadachbia",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Sadaltager",
    "name": "kn-IN-Chirp3-HD-Sadaltager",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Schedar",
    "name": "kn-IN-Chirp3-HD-Schedar",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Sulafat",
    "name": "kn-IN-Chirp3-HD-Sulafat",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Umbriel",
    "name": "kn-IN-Chirp3-HD-Umbriel",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Vindemiatrix",
    "name": "kn-IN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Zephyr",
    "name": "kn-IN-Chirp3-HD-Zephyr",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Chirp3-HD-Zubenelgenubi",
    "name": "kn-IN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Standard-A",
    "name": "kn-IN-Standard-A",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Standard-B",
    "name": "kn-IN-Standard-B",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Standard-C",
    "name": "kn-IN-Standard-C",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Standard-D",
    "name": "kn-IN-Standard-D",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Wavenet-A",
    "name": "kn-IN-Wavenet-A",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Wavenet-B",
    "name": "kn-IN-Wavenet-B",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Wavenet-C",
    "name": "kn-IN-Wavenet-C",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "kn-IN-Wavenet-D",
    "name": "kn-IN-Wavenet-D",
    "languages": [
      "kn-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Achernar",
    "name": "ko-KR-Chirp3-HD-Achernar",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Achird",
    "name": "ko-KR-Chirp3-HD-Achird",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Algenib",
    "name": "ko-KR-Chirp3-HD-Algenib",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Algieba",
    "name": "ko-KR-Chirp3-HD-Algieba",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Alnilam",
    "name": "ko-KR-Chirp3-HD-Alnilam",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Aoede",
    "name": "ko-KR-Chirp3-HD-Aoede",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Autonoe",
    "name": "ko-KR-Chirp3-HD-Autonoe",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Callirrhoe",
    "name": "ko-KR-Chirp3-HD-Callirrhoe",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Charon",
    "name": "ko-KR-Chirp3-HD-Charon",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Despina",
    "name": "ko-KR-Chirp3-HD-Despina",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Enceladus",
    "name": "ko-KR-Chirp3-HD-Enceladus",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Erinome",
    "name": "ko-KR-Chirp3-HD-Erinome",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Fenrir",
    "name": "ko-KR-Chirp3-HD-Fenrir",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Gacrux",
    "name": "ko-KR-Chirp3-HD-Gacrux",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Iapetus",
    "name": "ko-KR-Chirp3-HD-Iapetus",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Kore",
    "name": "ko-KR-Chirp3-HD-Kore",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Laomedeia",
    "name": "ko-KR-Chirp3-HD-Laomedeia",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Leda",
    "name": "ko-KR-Chirp3-HD-Leda",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Orus",
    "name": "ko-KR-Chirp3-HD-Orus",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Puck",
    "name": "ko-KR-Chirp3-HD-Puck",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Pulcherrima",
    "name": "ko-KR-Chirp3-HD-Pulcherrima",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Rasalgethi",
    "name": "ko-KR-Chirp3-HD-Rasalgethi",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Sadachbia",
    "name": "ko-KR-Chirp3-HD-Sadachbia",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Sadaltager",
    "name": "ko-KR-Chirp3-HD-Sadaltager",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Schedar",
    "name": "ko-KR-Chirp3-HD-Schedar",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Sulafat",
    "name": "ko-KR-Chirp3-HD-Sulafat",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Umbriel",
    "name": "ko-KR-Chirp3-HD-Umbriel",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Vindemiatrix",
    "name": "ko-KR-Chirp3-HD-Vindemiatrix",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Zephyr",
    "name": "ko-KR-Chirp3-HD-Zephyr",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Chirp3-HD-Zubenelgenubi",
    "name": "ko-KR-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Neural2-A",
    "name": "ko-KR-Neural2-A",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Neural2-B",
    "name": "ko-KR-Neural2-B",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Neural2-C",
    "name": "ko-KR-Neural2-C",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Standard-A",
    "name": "ko-KR-Standard-A",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Standard-B",
    "name": "ko-KR-Standard-B",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Standard-C",
    "name": "ko-KR-Standard-C",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Standard-D",
    "name": "ko-KR-Standard-D",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Wavenet-A",
    "name": "ko-KR-Wavenet-A",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Wavenet-B",
    "name": "ko-KR-Wavenet-B",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Wavenet-C",
    "name": "ko-KR-Wavenet-C",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ko-KR-Wavenet-D",
    "name": "ko-KR-Wavenet-D",
    "languages": [
      "ko-KR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Achernar",
    "name": "lt-LT-Chirp3-HD-Achernar",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Achird",
    "name": "lt-LT-Chirp3-HD-Achird",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Algenib",
    "name": "lt-LT-Chirp3-HD-Algenib",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Algieba",
    "name": "lt-LT-Chirp3-HD-Algieba",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Alnilam",
    "name": "lt-LT-Chirp3-HD-Alnilam",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Aoede",
    "name": "lt-LT-Chirp3-HD-Aoede",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Autonoe",
    "name": "lt-LT-Chirp3-HD-Autonoe",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Callirrhoe",
    "name": "lt-LT-Chirp3-HD-Callirrhoe",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Charon",
    "name": "lt-LT-Chirp3-HD-Charon",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Despina",
    "name": "lt-LT-Chirp3-HD-Despina",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Enceladus",
    "name": "lt-LT-Chirp3-HD-Enceladus",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Erinome",
    "name": "lt-LT-Chirp3-HD-Erinome",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Fenrir",
    "name": "lt-LT-Chirp3-HD-Fenrir",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Gacrux",
    "name": "lt-LT-Chirp3-HD-Gacrux",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Iapetus",
    "name": "lt-LT-Chirp3-HD-Iapetus",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Kore",
    "name": "lt-LT-Chirp3-HD-Kore",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Laomedeia",
    "name": "lt-LT-Chirp3-HD-Laomedeia",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Leda",
    "name": "lt-LT-Chirp3-HD-Leda",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Orus",
    "name": "lt-LT-Chirp3-HD-Orus",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Puck",
    "name": "lt-LT-Chirp3-HD-Puck",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Pulcherrima",
    "name": "lt-LT-Chirp3-HD-Pulcherrima",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Rasalgethi",
    "name": "lt-LT-Chirp3-HD-Rasalgethi",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Sadachbia",
    "name": "lt-LT-Chirp3-HD-Sadachbia",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Sadaltager",
    "name": "lt-LT-Chirp3-HD-Sadaltager",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Schedar",
    "name": "lt-LT-Chirp3-HD-Schedar",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Sulafat",
    "name": "lt-LT-Chirp3-HD-Sulafat",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Umbriel",
    "name": "lt-LT-Chirp3-HD-Umbriel",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Vindemiatrix",
    "name": "lt-LT-Chirp3-HD-Vindemiatrix",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Zephyr",
    "name": "lt-LT-Chirp3-HD-Zephyr",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Chirp3-HD-Zubenelgenubi",
    "name": "lt-LT-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lt-LT-Standard-B",
    "name": "lt-LT-Standard-B",
    "languages": [
      "lt-LT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Achernar",
    "name": "lv-LV-Chirp3-HD-Achernar",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Achird",
    "name": "lv-LV-Chirp3-HD-Achird",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Algenib",
    "name": "lv-LV-Chirp3-HD-Algenib",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Algieba",
    "name": "lv-LV-Chirp3-HD-Algieba",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Alnilam",
    "name": "lv-LV-Chirp3-HD-Alnilam",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Aoede",
    "name": "lv-LV-Chirp3-HD-Aoede",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Autonoe",
    "name": "lv-LV-Chirp3-HD-Autonoe",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Callirrhoe",
    "name": "lv-LV-Chirp3-HD-Callirrhoe",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Charon",
    "name": "lv-LV-Chirp3-HD-Charon",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Despina",
    "name": "lv-LV-Chirp3-HD-Despina",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Enceladus",
    "name": "lv-LV-Chirp3-HD-Enceladus",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Erinome",
    "name": "lv-LV-Chirp3-HD-Erinome",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Fenrir",
    "name": "lv-LV-Chirp3-HD-Fenrir",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Gacrux",
    "name": "lv-LV-Chirp3-HD-Gacrux",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Iapetus",
    "name": "lv-LV-Chirp3-HD-Iapetus",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Kore",
    "name": "lv-LV-Chirp3-HD-Kore",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Laomedeia",
    "name": "lv-LV-Chirp3-HD-Laomedeia",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Leda",
    "name": "lv-LV-Chirp3-HD-Leda",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Orus",
    "name": "lv-LV-Chirp3-HD-Orus",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Puck",
    "name": "lv-LV-Chirp3-HD-Puck",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Pulcherrima",
    "name": "lv-LV-Chirp3-HD-Pulcherrima",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Rasalgethi",
    "name": "lv-LV-Chirp3-HD-Rasalgethi",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Sadachbia",
    "name": "lv-LV-Chirp3-HD-Sadachbia",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Sadaltager",
    "name": "lv-LV-Chirp3-HD-Sadaltager",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Schedar",
    "name": "lv-LV-Chirp3-HD-Schedar",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Sulafat",
    "name": "lv-LV-Chirp3-HD-Sulafat",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Umbriel",
    "name": "lv-LV-Chirp3-HD-Umbriel",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Vindemiatrix",
    "name": "lv-LV-Chirp3-HD-Vindemiatrix",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Zephyr",
    "name": "lv-LV-Chirp3-HD-Zephyr",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Chirp3-HD-Zubenelgenubi",
    "name": "lv-LV-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "lv-LV-Standard-B",
    "name": "lv-LV-Standard-B",
    "languages": [
      "lv-LV"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Achernar",
    "name": "ml-IN-Chirp3-HD-Achernar",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Achird",
    "name": "ml-IN-Chirp3-HD-Achird",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Algenib",
    "name": "ml-IN-Chirp3-HD-Algenib",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Algieba",
    "name": "ml-IN-Chirp3-HD-Algieba",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Alnilam",
    "name": "ml-IN-Chirp3-HD-Alnilam",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Aoede",
    "name": "ml-IN-Chirp3-HD-Aoede",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Autonoe",
    "name": "ml-IN-Chirp3-HD-Autonoe",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Callirrhoe",
    "name": "ml-IN-Chirp3-HD-Callirrhoe",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Charon",
    "name": "ml-IN-Chirp3-HD-Charon",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Despina",
    "name": "ml-IN-Chirp3-HD-Despina",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Enceladus",
    "name": "ml-IN-Chirp3-HD-Enceladus",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Erinome",
    "name": "ml-IN-Chirp3-HD-Erinome",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Fenrir",
    "name": "ml-IN-Chirp3-HD-Fenrir",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Gacrux",
    "name": "ml-IN-Chirp3-HD-Gacrux",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Iapetus",
    "name": "ml-IN-Chirp3-HD-Iapetus",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Kore",
    "name": "ml-IN-Chirp3-HD-Kore",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Laomedeia",
    "name": "ml-IN-Chirp3-HD-Laomedeia",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Leda",
    "name": "ml-IN-Chirp3-HD-Leda",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Orus",
    "name": "ml-IN-Chirp3-HD-Orus",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Puck",
    "name": "ml-IN-Chirp3-HD-Puck",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Pulcherrima",
    "name": "ml-IN-Chirp3-HD-Pulcherrima",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Rasalgethi",
    "name": "ml-IN-Chirp3-HD-Rasalgethi",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Sadachbia",
    "name": "ml-IN-Chirp3-HD-Sadachbia",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Sadaltager",
    "name": "ml-IN-Chirp3-HD-Sadaltager",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Schedar",
    "name": "ml-IN-Chirp3-HD-Schedar",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Sulafat",
    "name": "ml-IN-Chirp3-HD-Sulafat",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Umbriel",
    "name": "ml-IN-Chirp3-HD-Umbriel",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Vindemiatrix",
    "name": "ml-IN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Zephyr",
    "name": "ml-IN-Chirp3-HD-Zephyr",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Chirp3-HD-Zubenelgenubi",
    "name": "ml-IN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Standard-A",
    "name": "ml-IN-Standard-A",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Standard-B",
    "name": "ml-IN-Standard-B",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Standard-C",
    "name": "ml-IN-Standard-C",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Standard-D",
    "name": "ml-IN-Standard-D",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Wavenet-A",
    "name": "ml-IN-Wavenet-A",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Wavenet-B",
    "name": "ml-IN-Wavenet-B",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Wavenet-C",
    "name": "ml-IN-Wavenet-C",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ml-IN-Wavenet-D",
    "name": "ml-IN-Wavenet-D",
    "languages": [
      "ml-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Achernar",
    "name": "mr-IN-Chirp3-HD-Achernar",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Achird",
    "name": "mr-IN-Chirp3-HD-Achird",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Algenib",
    "name": "mr-IN-Chirp3-HD-Algenib",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Algieba",
    "name": "mr-IN-Chirp3-HD-Algieba",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Alnilam",
    "name": "mr-IN-Chirp3-HD-Alnilam",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Aoede",
    "name": "mr-IN-Chirp3-HD-Aoede",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Autonoe",
    "name": "mr-IN-Chirp3-HD-Autonoe",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Callirrhoe",
    "name": "mr-IN-Chirp3-HD-Callirrhoe",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Charon",
    "name": "mr-IN-Chirp3-HD-Charon",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Despina",
    "name": "mr-IN-Chirp3-HD-Despina",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Enceladus",
    "name": "mr-IN-Chirp3-HD-Enceladus",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Erinome",
    "name": "mr-IN-Chirp3-HD-Erinome",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Fenrir",
    "name": "mr-IN-Chirp3-HD-Fenrir",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Gacrux",
    "name": "mr-IN-Chirp3-HD-Gacrux",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Iapetus",
    "name": "mr-IN-Chirp3-HD-Iapetus",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Kore",
    "name": "mr-IN-Chirp3-HD-Kore",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Laomedeia",
    "name": "mr-IN-Chirp3-HD-Laomedeia",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Leda",
    "name": "mr-IN-Chirp3-HD-Leda",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Orus",
    "name": "mr-IN-Chirp3-HD-Orus",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Puck",
    "name": "mr-IN-Chirp3-HD-Puck",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Pulcherrima",
    "name": "mr-IN-Chirp3-HD-Pulcherrima",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Rasalgethi",
    "name": "mr-IN-Chirp3-HD-Rasalgethi",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Sadachbia",
    "name": "mr-IN-Chirp3-HD-Sadachbia",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Sadaltager",
    "name": "mr-IN-Chirp3-HD-Sadaltager",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Schedar",
    "name": "mr-IN-Chirp3-HD-Schedar",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Sulafat",
    "name": "mr-IN-Chirp3-HD-Sulafat",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Umbriel",
    "name": "mr-IN-Chirp3-HD-Umbriel",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Vindemiatrix",
    "name": "mr-IN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Zephyr",
    "name": "mr-IN-Chirp3-HD-Zephyr",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Chirp3-HD-Zubenelgenubi",
    "name": "mr-IN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Standard-A",
    "name": "mr-IN-Standard-A",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Standard-B",
    "name": "mr-IN-Standard-B",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Standard-C",
    "name": "mr-IN-Standard-C",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Wavenet-A",
    "name": "mr-IN-Wavenet-A",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Wavenet-B",
    "name": "mr-IN-Wavenet-B",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "mr-IN-Wavenet-C",
    "name": "mr-IN-Wavenet-C",
    "languages": [
      "mr-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ms-MY-Standard-A",
    "name": "ms-MY-Standard-A",
    "languages": [
      "ms-MY"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ms-MY-Standard-B",
    "name": "ms-MY-Standard-B",
    "languages": [
      "ms-MY"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ms-MY-Standard-C",
    "name": "ms-MY-Standard-C",
    "languages": [
      "ms-MY"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ms-MY-Standard-D",
    "name": "ms-MY-Standard-D",
    "languages": [
      "ms-MY"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ms-MY-Wavenet-A",
    "name": "ms-MY-Wavenet-A",
    "languages": [
      "ms-MY"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ms-MY-Wavenet-B",
    "name": "ms-MY-Wavenet-B",
    "languages": [
      "ms-MY"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ms-MY-Wavenet-C",
    "name": "ms-MY-Wavenet-C",
    "languages": [
      "ms-MY"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ms-MY-Wavenet-D",
    "name": "ms-MY-Wavenet-D",
    "languages": [
      "ms-MY"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Achernar",
    "name": "nb-NO-Chirp3-HD-Achernar",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Achird",
    "name": "nb-NO-Chirp3-HD-Achird",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Algenib",
    "name": "nb-NO-Chirp3-HD-Algenib",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Algieba",
    "name": "nb-NO-Chirp3-HD-Algieba",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Alnilam",
    "name": "nb-NO-Chirp3-HD-Alnilam",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Aoede",
    "name": "nb-NO-Chirp3-HD-Aoede",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Autonoe",
    "name": "nb-NO-Chirp3-HD-Autonoe",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Callirrhoe",
    "name": "nb-NO-Chirp3-HD-Callirrhoe",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Charon",
    "name": "nb-NO-Chirp3-HD-Charon",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Despina",
    "name": "nb-NO-Chirp3-HD-Despina",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Enceladus",
    "name": "nb-NO-Chirp3-HD-Enceladus",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Erinome",
    "name": "nb-NO-Chirp3-HD-Erinome",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Fenrir",
    "name": "nb-NO-Chirp3-HD-Fenrir",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Gacrux",
    "name": "nb-NO-Chirp3-HD-Gacrux",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Iapetus",
    "name": "nb-NO-Chirp3-HD-Iapetus",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Kore",
    "name": "nb-NO-Chirp3-HD-Kore",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Laomedeia",
    "name": "nb-NO-Chirp3-HD-Laomedeia",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Leda",
    "name": "nb-NO-Chirp3-HD-Leda",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Orus",
    "name": "nb-NO-Chirp3-HD-Orus",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Puck",
    "name": "nb-NO-Chirp3-HD-Puck",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Pulcherrima",
    "name": "nb-NO-Chirp3-HD-Pulcherrima",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Rasalgethi",
    "name": "nb-NO-Chirp3-HD-Rasalgethi",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Sadachbia",
    "name": "nb-NO-Chirp3-HD-Sadachbia",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Sadaltager",
    "name": "nb-NO-Chirp3-HD-Sadaltager",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Schedar",
    "name": "nb-NO-Chirp3-HD-Schedar",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Sulafat",
    "name": "nb-NO-Chirp3-HD-Sulafat",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Umbriel",
    "name": "nb-NO-Chirp3-HD-Umbriel",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Vindemiatrix",
    "name": "nb-NO-Chirp3-HD-Vindemiatrix",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Zephyr",
    "name": "nb-NO-Chirp3-HD-Zephyr",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Chirp3-HD-Zubenelgenubi",
    "name": "nb-NO-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Standard-F",
    "name": "nb-NO-Standard-F",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Standard-G",
    "name": "nb-NO-Standard-G",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Wavenet-F",
    "name": "nb-NO-Wavenet-F",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nb-NO-Wavenet-G",
    "name": "nb-NO-Wavenet-G",
    "languages": [
      "nb-NO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Achernar",
    "name": "nl-BE-Chirp3-HD-Achernar",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Achird",
    "name": "nl-BE-Chirp3-HD-Achird",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Algenib",
    "name": "nl-BE-Chirp3-HD-Algenib",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Algieba",
    "name": "nl-BE-Chirp3-HD-Algieba",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Alnilam",
    "name": "nl-BE-Chirp3-HD-Alnilam",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Aoede",
    "name": "nl-BE-Chirp3-HD-Aoede",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Autonoe",
    "name": "nl-BE-Chirp3-HD-Autonoe",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Callirrhoe",
    "name": "nl-BE-Chirp3-HD-Callirrhoe",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Charon",
    "name": "nl-BE-Chirp3-HD-Charon",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Despina",
    "name": "nl-BE-Chirp3-HD-Despina",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Enceladus",
    "name": "nl-BE-Chirp3-HD-Enceladus",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Erinome",
    "name": "nl-BE-Chirp3-HD-Erinome",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Fenrir",
    "name": "nl-BE-Chirp3-HD-Fenrir",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Gacrux",
    "name": "nl-BE-Chirp3-HD-Gacrux",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Iapetus",
    "name": "nl-BE-Chirp3-HD-Iapetus",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Kore",
    "name": "nl-BE-Chirp3-HD-Kore",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Laomedeia",
    "name": "nl-BE-Chirp3-HD-Laomedeia",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Leda",
    "name": "nl-BE-Chirp3-HD-Leda",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Orus",
    "name": "nl-BE-Chirp3-HD-Orus",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Puck",
    "name": "nl-BE-Chirp3-HD-Puck",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Pulcherrima",
    "name": "nl-BE-Chirp3-HD-Pulcherrima",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Rasalgethi",
    "name": "nl-BE-Chirp3-HD-Rasalgethi",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Sadachbia",
    "name": "nl-BE-Chirp3-HD-Sadachbia",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Sadaltager",
    "name": "nl-BE-Chirp3-HD-Sadaltager",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Schedar",
    "name": "nl-BE-Chirp3-HD-Schedar",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Sulafat",
    "name": "nl-BE-Chirp3-HD-Sulafat",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Umbriel",
    "name": "nl-BE-Chirp3-HD-Umbriel",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Vindemiatrix",
    "name": "nl-BE-Chirp3-HD-Vindemiatrix",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Zephyr",
    "name": "nl-BE-Chirp3-HD-Zephyr",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Chirp3-HD-Zubenelgenubi",
    "name": "nl-BE-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Standard-C",
    "name": "nl-BE-Standard-C",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Standard-D",
    "name": "nl-BE-Standard-D",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Wavenet-C",
    "name": "nl-BE-Wavenet-C",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-BE-Wavenet-D",
    "name": "nl-BE-Wavenet-D",
    "languages": [
      "nl-BE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Achernar",
    "name": "nl-NL-Chirp3-HD-Achernar",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Achird",
    "name": "nl-NL-Chirp3-HD-Achird",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Algenib",
    "name": "nl-NL-Chirp3-HD-Algenib",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Algieba",
    "name": "nl-NL-Chirp3-HD-Algieba",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Alnilam",
    "name": "nl-NL-Chirp3-HD-Alnilam",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Aoede",
    "name": "nl-NL-Chirp3-HD-Aoede",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Autonoe",
    "name": "nl-NL-Chirp3-HD-Autonoe",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Callirrhoe",
    "name": "nl-NL-Chirp3-HD-Callirrhoe",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Charon",
    "name": "nl-NL-Chirp3-HD-Charon",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Despina",
    "name": "nl-NL-Chirp3-HD-Despina",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Enceladus",
    "name": "nl-NL-Chirp3-HD-Enceladus",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Erinome",
    "name": "nl-NL-Chirp3-HD-Erinome",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Fenrir",
    "name": "nl-NL-Chirp3-HD-Fenrir",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Gacrux",
    "name": "nl-NL-Chirp3-HD-Gacrux",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Iapetus",
    "name": "nl-NL-Chirp3-HD-Iapetus",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Kore",
    "name": "nl-NL-Chirp3-HD-Kore",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Laomedeia",
    "name": "nl-NL-Chirp3-HD-Laomedeia",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Leda",
    "name": "nl-NL-Chirp3-HD-Leda",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Orus",
    "name": "nl-NL-Chirp3-HD-Orus",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Puck",
    "name": "nl-NL-Chirp3-HD-Puck",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Pulcherrima",
    "name": "nl-NL-Chirp3-HD-Pulcherrima",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Rasalgethi",
    "name": "nl-NL-Chirp3-HD-Rasalgethi",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Sadachbia",
    "name": "nl-NL-Chirp3-HD-Sadachbia",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Sadaltager",
    "name": "nl-NL-Chirp3-HD-Sadaltager",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Schedar",
    "name": "nl-NL-Chirp3-HD-Schedar",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Sulafat",
    "name": "nl-NL-Chirp3-HD-Sulafat",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Umbriel",
    "name": "nl-NL-Chirp3-HD-Umbriel",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Vindemiatrix",
    "name": "nl-NL-Chirp3-HD-Vindemiatrix",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Zephyr",
    "name": "nl-NL-Chirp3-HD-Zephyr",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Chirp3-HD-Zubenelgenubi",
    "name": "nl-NL-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Standard-F",
    "name": "nl-NL-Standard-F",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Standard-G",
    "name": "nl-NL-Standard-G",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Wavenet-F",
    "name": "nl-NL-Wavenet-F",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "nl-NL-Wavenet-G",
    "name": "nl-NL-Wavenet-G",
    "languages": [
      "nl-NL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Achernar",
    "name": "pa-IN-Chirp3-HD-Achernar",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Achird",
    "name": "pa-IN-Chirp3-HD-Achird",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Algenib",
    "name": "pa-IN-Chirp3-HD-Algenib",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Algieba",
    "name": "pa-IN-Chirp3-HD-Algieba",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Alnilam",
    "name": "pa-IN-Chirp3-HD-Alnilam",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Aoede",
    "name": "pa-IN-Chirp3-HD-Aoede",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Autonoe",
    "name": "pa-IN-Chirp3-HD-Autonoe",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Callirrhoe",
    "name": "pa-IN-Chirp3-HD-Callirrhoe",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Charon",
    "name": "pa-IN-Chirp3-HD-Charon",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Despina",
    "name": "pa-IN-Chirp3-HD-Despina",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Enceladus",
    "name": "pa-IN-Chirp3-HD-Enceladus",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Erinome",
    "name": "pa-IN-Chirp3-HD-Erinome",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Fenrir",
    "name": "pa-IN-Chirp3-HD-Fenrir",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Gacrux",
    "name": "pa-IN-Chirp3-HD-Gacrux",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Iapetus",
    "name": "pa-IN-Chirp3-HD-Iapetus",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Kore",
    "name": "pa-IN-Chirp3-HD-Kore",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Laomedeia",
    "name": "pa-IN-Chirp3-HD-Laomedeia",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Leda",
    "name": "pa-IN-Chirp3-HD-Leda",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Orus",
    "name": "pa-IN-Chirp3-HD-Orus",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Puck",
    "name": "pa-IN-Chirp3-HD-Puck",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Pulcherrima",
    "name": "pa-IN-Chirp3-HD-Pulcherrima",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Rasalgethi",
    "name": "pa-IN-Chirp3-HD-Rasalgethi",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Sadachbia",
    "name": "pa-IN-Chirp3-HD-Sadachbia",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Sadaltager",
    "name": "pa-IN-Chirp3-HD-Sadaltager",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Schedar",
    "name": "pa-IN-Chirp3-HD-Schedar",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Sulafat",
    "name": "pa-IN-Chirp3-HD-Sulafat",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Umbriel",
    "name": "pa-IN-Chirp3-HD-Umbriel",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Vindemiatrix",
    "name": "pa-IN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Zephyr",
    "name": "pa-IN-Chirp3-HD-Zephyr",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Chirp3-HD-Zubenelgenubi",
    "name": "pa-IN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Standard-A",
    "name": "pa-IN-Standard-A",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Standard-B",
    "name": "pa-IN-Standard-B",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Standard-C",
    "name": "pa-IN-Standard-C",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Standard-D",
    "name": "pa-IN-Standard-D",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Wavenet-A",
    "name": "pa-IN-Wavenet-A",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Wavenet-B",
    "name": "pa-IN-Wavenet-B",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Wavenet-C",
    "name": "pa-IN-Wavenet-C",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pa-IN-Wavenet-D",
    "name": "pa-IN-Wavenet-D",
    "languages": [
      "pa-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Achernar",
    "name": "pl-PL-Chirp3-HD-Achernar",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Achird",
    "name": "pl-PL-Chirp3-HD-Achird",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Algenib",
    "name": "pl-PL-Chirp3-HD-Algenib",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Algieba",
    "name": "pl-PL-Chirp3-HD-Algieba",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Alnilam",
    "name": "pl-PL-Chirp3-HD-Alnilam",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Aoede",
    "name": "pl-PL-Chirp3-HD-Aoede",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Autonoe",
    "name": "pl-PL-Chirp3-HD-Autonoe",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Callirrhoe",
    "name": "pl-PL-Chirp3-HD-Callirrhoe",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Charon",
    "name": "pl-PL-Chirp3-HD-Charon",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Despina",
    "name": "pl-PL-Chirp3-HD-Despina",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Enceladus",
    "name": "pl-PL-Chirp3-HD-Enceladus",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Erinome",
    "name": "pl-PL-Chirp3-HD-Erinome",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Fenrir",
    "name": "pl-PL-Chirp3-HD-Fenrir",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Gacrux",
    "name": "pl-PL-Chirp3-HD-Gacrux",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Iapetus",
    "name": "pl-PL-Chirp3-HD-Iapetus",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Kore",
    "name": "pl-PL-Chirp3-HD-Kore",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Laomedeia",
    "name": "pl-PL-Chirp3-HD-Laomedeia",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Leda",
    "name": "pl-PL-Chirp3-HD-Leda",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Orus",
    "name": "pl-PL-Chirp3-HD-Orus",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Puck",
    "name": "pl-PL-Chirp3-HD-Puck",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Pulcherrima",
    "name": "pl-PL-Chirp3-HD-Pulcherrima",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Rasalgethi",
    "name": "pl-PL-Chirp3-HD-Rasalgethi",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Sadachbia",
    "name": "pl-PL-Chirp3-HD-Sadachbia",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Sadaltager",
    "name": "pl-PL-Chirp3-HD-Sadaltager",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Schedar",
    "name": "pl-PL-Chirp3-HD-Schedar",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Sulafat",
    "name": "pl-PL-Chirp3-HD-Sulafat",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Umbriel",
    "name": "pl-PL-Chirp3-HD-Umbriel",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Vindemiatrix",
    "name": "pl-PL-Chirp3-HD-Vindemiatrix",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Zephyr",
    "name": "pl-PL-Chirp3-HD-Zephyr",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Chirp3-HD-Zubenelgenubi",
    "name": "pl-PL-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Standard-F",
    "name": "pl-PL-Standard-F",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Standard-G",
    "name": "pl-PL-Standard-G",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Wavenet-F",
    "name": "pl-PL-Wavenet-F",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pl-PL-Wavenet-G",
    "name": "pl-PL-Wavenet-G",
    "languages": [
      "pl-PL"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Achernar",
    "name": "pt-BR-Chirp3-HD-Achernar",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Achird",
    "name": "pt-BR-Chirp3-HD-Achird",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Algenib",
    "name": "pt-BR-Chirp3-HD-Algenib",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Algieba",
    "name": "pt-BR-Chirp3-HD-Algieba",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Alnilam",
    "name": "pt-BR-Chirp3-HD-Alnilam",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Aoede",
    "name": "pt-BR-Chirp3-HD-Aoede",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Autonoe",
    "name": "pt-BR-Chirp3-HD-Autonoe",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Callirrhoe",
    "name": "pt-BR-Chirp3-HD-Callirrhoe",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Charon",
    "name": "pt-BR-Chirp3-HD-Charon",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Despina",
    "name": "pt-BR-Chirp3-HD-Despina",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Enceladus",
    "name": "pt-BR-Chirp3-HD-Enceladus",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Erinome",
    "name": "pt-BR-Chirp3-HD-Erinome",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Fenrir",
    "name": "pt-BR-Chirp3-HD-Fenrir",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Gacrux",
    "name": "pt-BR-Chirp3-HD-Gacrux",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Iapetus",
    "name": "pt-BR-Chirp3-HD-Iapetus",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Kore",
    "name": "pt-BR-Chirp3-HD-Kore",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Laomedeia",
    "name": "pt-BR-Chirp3-HD-Laomedeia",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Leda",
    "name": "pt-BR-Chirp3-HD-Leda",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Orus",
    "name": "pt-BR-Chirp3-HD-Orus",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Puck",
    "name": "pt-BR-Chirp3-HD-Puck",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Pulcherrima",
    "name": "pt-BR-Chirp3-HD-Pulcherrima",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Rasalgethi",
    "name": "pt-BR-Chirp3-HD-Rasalgethi",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Sadachbia",
    "name": "pt-BR-Chirp3-HD-Sadachbia",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Sadaltager",
    "name": "pt-BR-Chirp3-HD-Sadaltager",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Schedar",
    "name": "pt-BR-Chirp3-HD-Schedar",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Sulafat",
    "name": "pt-BR-Chirp3-HD-Sulafat",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Umbriel",
    "name": "pt-BR-Chirp3-HD-Umbriel",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Vindemiatrix",
    "name": "pt-BR-Chirp3-HD-Vindemiatrix",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Zephyr",
    "name": "pt-BR-Chirp3-HD-Zephyr",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Chirp3-HD-Zubenelgenubi",
    "name": "pt-BR-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Neural2-A",
    "name": "pt-BR-Neural2-A",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Neural2-B",
    "name": "pt-BR-Neural2-B",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Neural2-C",
    "name": "pt-BR-Neural2-C",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Standard-A",
    "name": "pt-BR-Standard-A",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Standard-B",
    "name": "pt-BR-Standard-B",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Standard-C",
    "name": "pt-BR-Standard-C",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Standard-D",
    "name": "pt-BR-Standard-D",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Standard-E",
    "name": "pt-BR-Standard-E",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Wavenet-A",
    "name": "pt-BR-Wavenet-A",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Wavenet-B",
    "name": "pt-BR-Wavenet-B",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Wavenet-C",
    "name": "pt-BR-Wavenet-C",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Wavenet-D",
    "name": "pt-BR-Wavenet-D",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-BR-Wavenet-E",
    "name": "pt-BR-Wavenet-E",
    "languages": [
      "pt-BR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-PT-Standard-E",
    "name": "pt-PT-Standard-E",
    "languages": [
      "pt-PT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-PT-Standard-F",
    "name": "pt-PT-Standard-F",
    "languages": [
      "pt-PT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-PT-Wavenet-E",
    "name": "pt-PT-Wavenet-E",
    "languages": [
      "pt-PT"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "pt-PT-Wavenet-F",
    "name": "pt-PT-Wavenet-F",
    "languages": [
      "pt-PT"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Achernar",
    "name": "ro-RO-Chirp3-HD-Achernar",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Achird",
    "name": "ro-RO-Chirp3-HD-Achird",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Algenib",
    "name": "ro-RO-Chirp3-HD-Algenib",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Algieba",
    "name": "ro-RO-Chirp3-HD-Algieba",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Alnilam",
    "name": "ro-RO-Chirp3-HD-Alnilam",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Aoede",
    "name": "ro-RO-Chirp3-HD-Aoede",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Autonoe",
    "name": "ro-RO-Chirp3-HD-Autonoe",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Callirrhoe",
    "name": "ro-RO-Chirp3-HD-Callirrhoe",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Charon",
    "name": "ro-RO-Chirp3-HD-Charon",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Despina",
    "name": "ro-RO-Chirp3-HD-Despina",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Enceladus",
    "name": "ro-RO-Chirp3-HD-Enceladus",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Erinome",
    "name": "ro-RO-Chirp3-HD-Erinome",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Fenrir",
    "name": "ro-RO-Chirp3-HD-Fenrir",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Gacrux",
    "name": "ro-RO-Chirp3-HD-Gacrux",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Iapetus",
    "name": "ro-RO-Chirp3-HD-Iapetus",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Kore",
    "name": "ro-RO-Chirp3-HD-Kore",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Laomedeia",
    "name": "ro-RO-Chirp3-HD-Laomedeia",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Leda",
    "name": "ro-RO-Chirp3-HD-Leda",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Orus",
    "name": "ro-RO-Chirp3-HD-Orus",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Puck",
    "name": "ro-RO-Chirp3-HD-Puck",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Pulcherrima",
    "name": "ro-RO-Chirp3-HD-Pulcherrima",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Rasalgethi",
    "name": "ro-RO-Chirp3-HD-Rasalgethi",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Sadachbia",
    "name": "ro-RO-Chirp3-HD-Sadachbia",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Sadaltager",
    "name": "ro-RO-Chirp3-HD-Sadaltager",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Schedar",
    "name": "ro-RO-Chirp3-HD-Schedar",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Sulafat",
    "name": "ro-RO-Chirp3-HD-Sulafat",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Umbriel",
    "name": "ro-RO-Chirp3-HD-Umbriel",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Vindemiatrix",
    "name": "ro-RO-Chirp3-HD-Vindemiatrix",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Zephyr",
    "name": "ro-RO-Chirp3-HD-Zephyr",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Chirp3-HD-Zubenelgenubi",
    "name": "ro-RO-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Standard-B",
    "name": "ro-RO-Standard-B",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ro-RO-Wavenet-B",
    "name": "ro-RO-Wavenet-B",
    "languages": [
      "ro-RO"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Chirp3-HD-Aoede",
    "name": "ru-RU-Chirp3-HD-Aoede",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Chirp3-HD-Charon",
    "name": "ru-RU-Chirp3-HD-Charon",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Chirp3-HD-Fenrir",
    "name": "ru-RU-Chirp3-HD-Fenrir",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Chirp3-HD-Kore",
    "name": "ru-RU-Chirp3-HD-Kore",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Chirp3-HD-Leda",
    "name": "ru-RU-Chirp3-HD-Leda",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Chirp3-HD-Orus",
    "name": "ru-RU-Chirp3-HD-Orus",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Chirp3-HD-Puck",
    "name": "ru-RU-Chirp3-HD-Puck",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Chirp3-HD-Zephyr",
    "name": "ru-RU-Chirp3-HD-Zephyr",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Standard-A",
    "name": "ru-RU-Standard-A",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Standard-B",
    "name": "ru-RU-Standard-B",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Standard-C",
    "name": "ru-RU-Standard-C",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Standard-D",
    "name": "ru-RU-Standard-D",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Standard-E",
    "name": "ru-RU-Standard-E",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Wavenet-A",
    "name": "ru-RU-Wavenet-A",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Wavenet-B",
    "name": "ru-RU-Wavenet-B",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Wavenet-C",
    "name": "ru-RU-Wavenet-C",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Wavenet-D",
    "name": "ru-RU-Wavenet-D",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ru-RU-Wavenet-E",
    "name": "ru-RU-Wavenet-E",
    "languages": [
      "ru-RU"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Achernar",
    "name": "sk-SK-Chirp3-HD-Achernar",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Achird",
    "name": "sk-SK-Chirp3-HD-Achird",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Algenib",
    "name": "sk-SK-Chirp3-HD-Algenib",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Algieba",
    "name": "sk-SK-Chirp3-HD-Algieba",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Alnilam",
    "name": "sk-SK-Chirp3-HD-Alnilam",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Aoede",
    "name": "sk-SK-Chirp3-HD-Aoede",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Autonoe",
    "name": "sk-SK-Chirp3-HD-Autonoe",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Callirrhoe",
    "name": "sk-SK-Chirp3-HD-Callirrhoe",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Charon",
    "name": "sk-SK-Chirp3-HD-Charon",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Despina",
    "name": "sk-SK-Chirp3-HD-Despina",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Enceladus",
    "name": "sk-SK-Chirp3-HD-Enceladus",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Erinome",
    "name": "sk-SK-Chirp3-HD-Erinome",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Fenrir",
    "name": "sk-SK-Chirp3-HD-Fenrir",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Gacrux",
    "name": "sk-SK-Chirp3-HD-Gacrux",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Iapetus",
    "name": "sk-SK-Chirp3-HD-Iapetus",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Kore",
    "name": "sk-SK-Chirp3-HD-Kore",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Laomedeia",
    "name": "sk-SK-Chirp3-HD-Laomedeia",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Leda",
    "name": "sk-SK-Chirp3-HD-Leda",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Orus",
    "name": "sk-SK-Chirp3-HD-Orus",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Puck",
    "name": "sk-SK-Chirp3-HD-Puck",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Pulcherrima",
    "name": "sk-SK-Chirp3-HD-Pulcherrima",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Rasalgethi",
    "name": "sk-SK-Chirp3-HD-Rasalgethi",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Sadachbia",
    "name": "sk-SK-Chirp3-HD-Sadachbia",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Sadaltager",
    "name": "sk-SK-Chirp3-HD-Sadaltager",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Schedar",
    "name": "sk-SK-Chirp3-HD-Schedar",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Sulafat",
    "name": "sk-SK-Chirp3-HD-Sulafat",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Umbriel",
    "name": "sk-SK-Chirp3-HD-Umbriel",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Vindemiatrix",
    "name": "sk-SK-Chirp3-HD-Vindemiatrix",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Zephyr",
    "name": "sk-SK-Chirp3-HD-Zephyr",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Chirp3-HD-Zubenelgenubi",
    "name": "sk-SK-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Standard-B",
    "name": "sk-SK-Standard-B",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sk-SK-Wavenet-B",
    "name": "sk-SK-Wavenet-B",
    "languages": [
      "sk-SK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Achernar",
    "name": "sl-SI-Chirp3-HD-Achernar",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Achird",
    "name": "sl-SI-Chirp3-HD-Achird",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Algenib",
    "name": "sl-SI-Chirp3-HD-Algenib",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Algieba",
    "name": "sl-SI-Chirp3-HD-Algieba",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Alnilam",
    "name": "sl-SI-Chirp3-HD-Alnilam",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Aoede",
    "name": "sl-SI-Chirp3-HD-Aoede",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Autonoe",
    "name": "sl-SI-Chirp3-HD-Autonoe",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Callirrhoe",
    "name": "sl-SI-Chirp3-HD-Callirrhoe",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Charon",
    "name": "sl-SI-Chirp3-HD-Charon",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Despina",
    "name": "sl-SI-Chirp3-HD-Despina",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Enceladus",
    "name": "sl-SI-Chirp3-HD-Enceladus",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Erinome",
    "name": "sl-SI-Chirp3-HD-Erinome",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Fenrir",
    "name": "sl-SI-Chirp3-HD-Fenrir",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Gacrux",
    "name": "sl-SI-Chirp3-HD-Gacrux",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Iapetus",
    "name": "sl-SI-Chirp3-HD-Iapetus",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Kore",
    "name": "sl-SI-Chirp3-HD-Kore",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Laomedeia",
    "name": "sl-SI-Chirp3-HD-Laomedeia",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Leda",
    "name": "sl-SI-Chirp3-HD-Leda",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Orus",
    "name": "sl-SI-Chirp3-HD-Orus",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Puck",
    "name": "sl-SI-Chirp3-HD-Puck",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Pulcherrima",
    "name": "sl-SI-Chirp3-HD-Pulcherrima",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Rasalgethi",
    "name": "sl-SI-Chirp3-HD-Rasalgethi",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Sadachbia",
    "name": "sl-SI-Chirp3-HD-Sadachbia",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Sadaltager",
    "name": "sl-SI-Chirp3-HD-Sadaltager",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Schedar",
    "name": "sl-SI-Chirp3-HD-Schedar",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Sulafat",
    "name": "sl-SI-Chirp3-HD-Sulafat",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Umbriel",
    "name": "sl-SI-Chirp3-HD-Umbriel",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Vindemiatrix",
    "name": "sl-SI-Chirp3-HD-Vindemiatrix",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Zephyr",
    "name": "sl-SI-Chirp3-HD-Zephyr",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sl-SI-Chirp3-HD-Zubenelgenubi",
    "name": "sl-SI-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "sl-SI"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Achernar",
    "name": "sr-RS-Chirp3-HD-Achernar",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Achird",
    "name": "sr-RS-Chirp3-HD-Achird",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Algenib",
    "name": "sr-RS-Chirp3-HD-Algenib",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Algieba",
    "name": "sr-RS-Chirp3-HD-Algieba",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Alnilam",
    "name": "sr-RS-Chirp3-HD-Alnilam",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Aoede",
    "name": "sr-RS-Chirp3-HD-Aoede",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Autonoe",
    "name": "sr-RS-Chirp3-HD-Autonoe",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Callirrhoe",
    "name": "sr-RS-Chirp3-HD-Callirrhoe",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Charon",
    "name": "sr-RS-Chirp3-HD-Charon",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Despina",
    "name": "sr-RS-Chirp3-HD-Despina",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Enceladus",
    "name": "sr-RS-Chirp3-HD-Enceladus",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Erinome",
    "name": "sr-RS-Chirp3-HD-Erinome",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Fenrir",
    "name": "sr-RS-Chirp3-HD-Fenrir",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Gacrux",
    "name": "sr-RS-Chirp3-HD-Gacrux",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Iapetus",
    "name": "sr-RS-Chirp3-HD-Iapetus",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Kore",
    "name": "sr-RS-Chirp3-HD-Kore",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Laomedeia",
    "name": "sr-RS-Chirp3-HD-Laomedeia",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Leda",
    "name": "sr-RS-Chirp3-HD-Leda",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Orus",
    "name": "sr-RS-Chirp3-HD-Orus",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Puck",
    "name": "sr-RS-Chirp3-HD-Puck",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Pulcherrima",
    "name": "sr-RS-Chirp3-HD-Pulcherrima",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Rasalgethi",
    "name": "sr-RS-Chirp3-HD-Rasalgethi",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Sadachbia",
    "name": "sr-RS-Chirp3-HD-Sadachbia",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Sadaltager",
    "name": "sr-RS-Chirp3-HD-Sadaltager",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Schedar",
    "name": "sr-RS-Chirp3-HD-Schedar",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Sulafat",
    "name": "sr-RS-Chirp3-HD-Sulafat",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Umbriel",
    "name": "sr-RS-Chirp3-HD-Umbriel",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Vindemiatrix",
    "name": "sr-RS-Chirp3-HD-Vindemiatrix",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Zephyr",
    "name": "sr-RS-Chirp3-HD-Zephyr",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Chirp3-HD-Zubenelgenubi",
    "name": "sr-RS-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sr-RS-Standard-B",
    "name": "sr-RS-Standard-B",
    "languages": [
      "sr-RS"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Achernar",
    "name": "sv-SE-Chirp3-HD-Achernar",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Achird",
    "name": "sv-SE-Chirp3-HD-Achird",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Algenib",
    "name": "sv-SE-Chirp3-HD-Algenib",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Algieba",
    "name": "sv-SE-Chirp3-HD-Algieba",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Alnilam",
    "name": "sv-SE-Chirp3-HD-Alnilam",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Aoede",
    "name": "sv-SE-Chirp3-HD-Aoede",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Autonoe",
    "name": "sv-SE-Chirp3-HD-Autonoe",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Callirrhoe",
    "name": "sv-SE-Chirp3-HD-Callirrhoe",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Charon",
    "name": "sv-SE-Chirp3-HD-Charon",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Despina",
    "name": "sv-SE-Chirp3-HD-Despina",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Enceladus",
    "name": "sv-SE-Chirp3-HD-Enceladus",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Erinome",
    "name": "sv-SE-Chirp3-HD-Erinome",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Fenrir",
    "name": "sv-SE-Chirp3-HD-Fenrir",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Gacrux",
    "name": "sv-SE-Chirp3-HD-Gacrux",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Iapetus",
    "name": "sv-SE-Chirp3-HD-Iapetus",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Kore",
    "name": "sv-SE-Chirp3-HD-Kore",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Laomedeia",
    "name": "sv-SE-Chirp3-HD-Laomedeia",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Leda",
    "name": "sv-SE-Chirp3-HD-Leda",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Orus",
    "name": "sv-SE-Chirp3-HD-Orus",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Puck",
    "name": "sv-SE-Chirp3-HD-Puck",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Pulcherrima",
    "name": "sv-SE-Chirp3-HD-Pulcherrima",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Rasalgethi",
    "name": "sv-SE-Chirp3-HD-Rasalgethi",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Sadachbia",
    "name": "sv-SE-Chirp3-HD-Sadachbia",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Sadaltager",
    "name": "sv-SE-Chirp3-HD-Sadaltager",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Schedar",
    "name": "sv-SE-Chirp3-HD-Schedar",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Sulafat",
    "name": "sv-SE-Chirp3-HD-Sulafat",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Umbriel",
    "name": "sv-SE-Chirp3-HD-Umbriel",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Vindemiatrix",
    "name": "sv-SE-Chirp3-HD-Vindemiatrix",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Zephyr",
    "name": "sv-SE-Chirp3-HD-Zephyr",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Chirp3-HD-Zubenelgenubi",
    "name": "sv-SE-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Standard-A",
    "name": "sv-SE-Standard-A",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Standard-B",
    "name": "sv-SE-Standard-B",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Standard-C",
    "name": "sv-SE-Standard-C",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Standard-D",
    "name": "sv-SE-Standard-D",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Standard-E",
    "name": "sv-SE-Standard-E",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Standard-F",
    "name": "sv-SE-Standard-F",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Standard-G",
    "name": "sv-SE-Standard-G",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Wavenet-A",
    "name": "sv-SE-Wavenet-A",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Wavenet-B",
    "name": "sv-SE-Wavenet-B",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Wavenet-C",
    "name": "sv-SE-Wavenet-C",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Wavenet-D",
    "name": "sv-SE-Wavenet-D",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Wavenet-E",
    "name": "sv-SE-Wavenet-E",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Wavenet-F",
    "name": "sv-SE-Wavenet-F",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sv-SE-Wavenet-G",
    "name": "sv-SE-Wavenet-G",
    "languages": [
      "sv-SE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Achernar",
    "name": "sw-KE-Chirp3-HD-Achernar",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Achird",
    "name": "sw-KE-Chirp3-HD-Achird",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Algenib",
    "name": "sw-KE-Chirp3-HD-Algenib",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Algieba",
    "name": "sw-KE-Chirp3-HD-Algieba",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Alnilam",
    "name": "sw-KE-Chirp3-HD-Alnilam",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Aoede",
    "name": "sw-KE-Chirp3-HD-Aoede",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Autonoe",
    "name": "sw-KE-Chirp3-HD-Autonoe",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Callirrhoe",
    "name": "sw-KE-Chirp3-HD-Callirrhoe",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Charon",
    "name": "sw-KE-Chirp3-HD-Charon",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Despina",
    "name": "sw-KE-Chirp3-HD-Despina",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Enceladus",
    "name": "sw-KE-Chirp3-HD-Enceladus",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Erinome",
    "name": "sw-KE-Chirp3-HD-Erinome",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Fenrir",
    "name": "sw-KE-Chirp3-HD-Fenrir",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Gacrux",
    "name": "sw-KE-Chirp3-HD-Gacrux",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Iapetus",
    "name": "sw-KE-Chirp3-HD-Iapetus",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Kore",
    "name": "sw-KE-Chirp3-HD-Kore",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Laomedeia",
    "name": "sw-KE-Chirp3-HD-Laomedeia",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Leda",
    "name": "sw-KE-Chirp3-HD-Leda",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Orus",
    "name": "sw-KE-Chirp3-HD-Orus",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Puck",
    "name": "sw-KE-Chirp3-HD-Puck",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Pulcherrima",
    "name": "sw-KE-Chirp3-HD-Pulcherrima",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Rasalgethi",
    "name": "sw-KE-Chirp3-HD-Rasalgethi",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Sadachbia",
    "name": "sw-KE-Chirp3-HD-Sadachbia",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Sadaltager",
    "name": "sw-KE-Chirp3-HD-Sadaltager",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Schedar",
    "name": "sw-KE-Chirp3-HD-Schedar",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Sulafat",
    "name": "sw-KE-Chirp3-HD-Sulafat",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Umbriel",
    "name": "sw-KE-Chirp3-HD-Umbriel",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Vindemiatrix",
    "name": "sw-KE-Chirp3-HD-Vindemiatrix",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Zephyr",
    "name": "sw-KE-Chirp3-HD-Zephyr",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "sw-KE-Chirp3-HD-Zubenelgenubi",
    "name": "sw-KE-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "sw-KE"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Achernar",
    "name": "ta-IN-Chirp3-HD-Achernar",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Achird",
    "name": "ta-IN-Chirp3-HD-Achird",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Algenib",
    "name": "ta-IN-Chirp3-HD-Algenib",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Algieba",
    "name": "ta-IN-Chirp3-HD-Algieba",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Alnilam",
    "name": "ta-IN-Chirp3-HD-Alnilam",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Aoede",
    "name": "ta-IN-Chirp3-HD-Aoede",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Autonoe",
    "name": "ta-IN-Chirp3-HD-Autonoe",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Callirrhoe",
    "name": "ta-IN-Chirp3-HD-Callirrhoe",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Charon",
    "name": "ta-IN-Chirp3-HD-Charon",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Despina",
    "name": "ta-IN-Chirp3-HD-Despina",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Enceladus",
    "name": "ta-IN-Chirp3-HD-Enceladus",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Erinome",
    "name": "ta-IN-Chirp3-HD-Erinome",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Fenrir",
    "name": "ta-IN-Chirp3-HD-Fenrir",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Gacrux",
    "name": "ta-IN-Chirp3-HD-Gacrux",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Iapetus",
    "name": "ta-IN-Chirp3-HD-Iapetus",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Kore",
    "name": "ta-IN-Chirp3-HD-Kore",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Laomedeia",
    "name": "ta-IN-Chirp3-HD-Laomedeia",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Leda",
    "name": "ta-IN-Chirp3-HD-Leda",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Orus",
    "name": "ta-IN-Chirp3-HD-Orus",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Puck",
    "name": "ta-IN-Chirp3-HD-Puck",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Pulcherrima",
    "name": "ta-IN-Chirp3-HD-Pulcherrima",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Rasalgethi",
    "name": "ta-IN-Chirp3-HD-Rasalgethi",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Sadachbia",
    "name": "ta-IN-Chirp3-HD-Sadachbia",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Sadaltager",
    "name": "ta-IN-Chirp3-HD-Sadaltager",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Schedar",
    "name": "ta-IN-Chirp3-HD-Schedar",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Sulafat",
    "name": "ta-IN-Chirp3-HD-Sulafat",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Umbriel",
    "name": "ta-IN-Chirp3-HD-Umbriel",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Vindemiatrix",
    "name": "ta-IN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Zephyr",
    "name": "ta-IN-Chirp3-HD-Zephyr",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Chirp3-HD-Zubenelgenubi",
    "name": "ta-IN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Standard-A",
    "name": "ta-IN-Standard-A",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Standard-B",
    "name": "ta-IN-Standard-B",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Standard-C",
    "name": "ta-IN-Standard-C",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Standard-D",
    "name": "ta-IN-Standard-D",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Wavenet-A",
    "name": "ta-IN-Wavenet-A",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Wavenet-B",
    "name": "ta-IN-Wavenet-B",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Wavenet-C",
    "name": "ta-IN-Wavenet-C",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ta-IN-Wavenet-D",
    "name": "ta-IN-Wavenet-D",
    "languages": [
      "ta-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Achernar",
    "name": "te-IN-Chirp3-HD-Achernar",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Achird",
    "name": "te-IN-Chirp3-HD-Achird",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Algenib",
    "name": "te-IN-Chirp3-HD-Algenib",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Algieba",
    "name": "te-IN-Chirp3-HD-Algieba",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Alnilam",
    "name": "te-IN-Chirp3-HD-Alnilam",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Aoede",
    "name": "te-IN-Chirp3-HD-Aoede",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Autonoe",
    "name": "te-IN-Chirp3-HD-Autonoe",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Callirrhoe",
    "name": "te-IN-Chirp3-HD-Callirrhoe",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Charon",
    "name": "te-IN-Chirp3-HD-Charon",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Despina",
    "name": "te-IN-Chirp3-HD-Despina",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Enceladus",
    "name": "te-IN-Chirp3-HD-Enceladus",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Erinome",
    "name": "te-IN-Chirp3-HD-Erinome",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Fenrir",
    "name": "te-IN-Chirp3-HD-Fenrir",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Gacrux",
    "name": "te-IN-Chirp3-HD-Gacrux",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Iapetus",
    "name": "te-IN-Chirp3-HD-Iapetus",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Kore",
    "name": "te-IN-Chirp3-HD-Kore",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Laomedeia",
    "name": "te-IN-Chirp3-HD-Laomedeia",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Leda",
    "name": "te-IN-Chirp3-HD-Leda",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Orus",
    "name": "te-IN-Chirp3-HD-Orus",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Puck",
    "name": "te-IN-Chirp3-HD-Puck",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Pulcherrima",
    "name": "te-IN-Chirp3-HD-Pulcherrima",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Rasalgethi",
    "name": "te-IN-Chirp3-HD-Rasalgethi",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Sadachbia",
    "name": "te-IN-Chirp3-HD-Sadachbia",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Sadaltager",
    "name": "te-IN-Chirp3-HD-Sadaltager",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Schedar",
    "name": "te-IN-Chirp3-HD-Schedar",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Sulafat",
    "name": "te-IN-Chirp3-HD-Sulafat",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Umbriel",
    "name": "te-IN-Chirp3-HD-Umbriel",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Vindemiatrix",
    "name": "te-IN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Zephyr",
    "name": "te-IN-Chirp3-HD-Zephyr",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Chirp3-HD-Zubenelgenubi",
    "name": "te-IN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Standard-A",
    "name": "te-IN-Standard-A",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Standard-B",
    "name": "te-IN-Standard-B",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Standard-C",
    "name": "te-IN-Standard-C",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "te-IN-Standard-D",
    "name": "te-IN-Standard-D",
    "languages": [
      "te-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Achernar",
    "name": "th-TH-Chirp3-HD-Achernar",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Achird",
    "name": "th-TH-Chirp3-HD-Achird",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Algenib",
    "name": "th-TH-Chirp3-HD-Algenib",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Algieba",
    "name": "th-TH-Chirp3-HD-Algieba",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Alnilam",
    "name": "th-TH-Chirp3-HD-Alnilam",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Aoede",
    "name": "th-TH-Chirp3-HD-Aoede",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Autonoe",
    "name": "th-TH-Chirp3-HD-Autonoe",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Callirrhoe",
    "name": "th-TH-Chirp3-HD-Callirrhoe",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Charon",
    "name": "th-TH-Chirp3-HD-Charon",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Despina",
    "name": "th-TH-Chirp3-HD-Despina",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Enceladus",
    "name": "th-TH-Chirp3-HD-Enceladus",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Erinome",
    "name": "th-TH-Chirp3-HD-Erinome",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Fenrir",
    "name": "th-TH-Chirp3-HD-Fenrir",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Gacrux",
    "name": "th-TH-Chirp3-HD-Gacrux",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Iapetus",
    "name": "th-TH-Chirp3-HD-Iapetus",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Kore",
    "name": "th-TH-Chirp3-HD-Kore",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Laomedeia",
    "name": "th-TH-Chirp3-HD-Laomedeia",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Leda",
    "name": "th-TH-Chirp3-HD-Leda",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Orus",
    "name": "th-TH-Chirp3-HD-Orus",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Puck",
    "name": "th-TH-Chirp3-HD-Puck",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Pulcherrima",
    "name": "th-TH-Chirp3-HD-Pulcherrima",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Rasalgethi",
    "name": "th-TH-Chirp3-HD-Rasalgethi",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Sadachbia",
    "name": "th-TH-Chirp3-HD-Sadachbia",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Sadaltager",
    "name": "th-TH-Chirp3-HD-Sadaltager",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Schedar",
    "name": "th-TH-Chirp3-HD-Schedar",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Sulafat",
    "name": "th-TH-Chirp3-HD-Sulafat",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Umbriel",
    "name": "th-TH-Chirp3-HD-Umbriel",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Vindemiatrix",
    "name": "th-TH-Chirp3-HD-Vindemiatrix",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Zephyr",
    "name": "th-TH-Chirp3-HD-Zephyr",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Chirp3-HD-Zubenelgenubi",
    "name": "th-TH-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Neural2-C",
    "name": "th-TH-Neural2-C",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "th-TH-Standard-A",
    "name": "th-TH-Standard-A",
    "languages": [
      "th-TH"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Achernar",
    "name": "tr-TR-Chirp3-HD-Achernar",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Achird",
    "name": "tr-TR-Chirp3-HD-Achird",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Algenib",
    "name": "tr-TR-Chirp3-HD-Algenib",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Algieba",
    "name": "tr-TR-Chirp3-HD-Algieba",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Alnilam",
    "name": "tr-TR-Chirp3-HD-Alnilam",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Aoede",
    "name": "tr-TR-Chirp3-HD-Aoede",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Autonoe",
    "name": "tr-TR-Chirp3-HD-Autonoe",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Callirrhoe",
    "name": "tr-TR-Chirp3-HD-Callirrhoe",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Charon",
    "name": "tr-TR-Chirp3-HD-Charon",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Despina",
    "name": "tr-TR-Chirp3-HD-Despina",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Enceladus",
    "name": "tr-TR-Chirp3-HD-Enceladus",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Erinome",
    "name": "tr-TR-Chirp3-HD-Erinome",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Fenrir",
    "name": "tr-TR-Chirp3-HD-Fenrir",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Gacrux",
    "name": "tr-TR-Chirp3-HD-Gacrux",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Iapetus",
    "name": "tr-TR-Chirp3-HD-Iapetus",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Kore",
    "name": "tr-TR-Chirp3-HD-Kore",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Laomedeia",
    "name": "tr-TR-Chirp3-HD-Laomedeia",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Leda",
    "name": "tr-TR-Chirp3-HD-Leda",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Orus",
    "name": "tr-TR-Chirp3-HD-Orus",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Puck",
    "name": "tr-TR-Chirp3-HD-Puck",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Pulcherrima",
    "name": "tr-TR-Chirp3-HD-Pulcherrima",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Rasalgethi",
    "name": "tr-TR-Chirp3-HD-Rasalgethi",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Sadachbia",
    "name": "tr-TR-Chirp3-HD-Sadachbia",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Sadaltager",
    "name": "tr-TR-Chirp3-HD-Sadaltager",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Schedar",
    "name": "tr-TR-Chirp3-HD-Schedar",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Sulafat",
    "name": "tr-TR-Chirp3-HD-Sulafat",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Umbriel",
    "name": "tr-TR-Chirp3-HD-Umbriel",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Vindemiatrix",
    "name": "tr-TR-Chirp3-HD-Vindemiatrix",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Zephyr",
    "name": "tr-TR-Chirp3-HD-Zephyr",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Chirp3-HD-Zubenelgenubi",
    "name": "tr-TR-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Standard-A",
    "name": "tr-TR-Standard-A",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Standard-B",
    "name": "tr-TR-Standard-B",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Standard-C",
    "name": "tr-TR-Standard-C",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Standard-D",
    "name": "tr-TR-Standard-D",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Standard-E",
    "name": "tr-TR-Standard-E",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Wavenet-A",
    "name": "tr-TR-Wavenet-A",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Wavenet-B",
    "name": "tr-TR-Wavenet-B",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Wavenet-C",
    "name": "tr-TR-Wavenet-C",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Wavenet-D",
    "name": "tr-TR-Wavenet-D",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "tr-TR-Wavenet-E",
    "name": "tr-TR-Wavenet-E",
    "languages": [
      "tr-TR"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Achernar",
    "name": "uk-UA-Chirp3-HD-Achernar",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Achird",
    "name": "uk-UA-Chirp3-HD-Achird",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Algenib",
    "name": "uk-UA-Chirp3-HD-Algenib",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Algieba",
    "name": "uk-UA-Chirp3-HD-Algieba",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Alnilam",
    "name": "uk-UA-Chirp3-HD-Alnilam",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Aoede",
    "name": "uk-UA-Chirp3-HD-Aoede",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Autonoe",
    "name": "uk-UA-Chirp3-HD-Autonoe",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Callirrhoe",
    "name": "uk-UA-Chirp3-HD-Callirrhoe",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Charon",
    "name": "uk-UA-Chirp3-HD-Charon",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Despina",
    "name": "uk-UA-Chirp3-HD-Despina",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Enceladus",
    "name": "uk-UA-Chirp3-HD-Enceladus",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Erinome",
    "name": "uk-UA-Chirp3-HD-Erinome",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Fenrir",
    "name": "uk-UA-Chirp3-HD-Fenrir",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Gacrux",
    "name": "uk-UA-Chirp3-HD-Gacrux",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Iapetus",
    "name": "uk-UA-Chirp3-HD-Iapetus",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Kore",
    "name": "uk-UA-Chirp3-HD-Kore",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Laomedeia",
    "name": "uk-UA-Chirp3-HD-Laomedeia",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Leda",
    "name": "uk-UA-Chirp3-HD-Leda",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Orus",
    "name": "uk-UA-Chirp3-HD-Orus",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Puck",
    "name": "uk-UA-Chirp3-HD-Puck",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Pulcherrima",
    "name": "uk-UA-Chirp3-HD-Pulcherrima",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Rasalgethi",
    "name": "uk-UA-Chirp3-HD-Rasalgethi",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Sadachbia",
    "name": "uk-UA-Chirp3-HD-Sadachbia",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Sadaltager",
    "name": "uk-UA-Chirp3-HD-Sadaltager",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Schedar",
    "name": "uk-UA-Chirp3-HD-Schedar",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Sulafat",
    "name": "uk-UA-Chirp3-HD-Sulafat",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Umbriel",
    "name": "uk-UA-Chirp3-HD-Umbriel",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Vindemiatrix",
    "name": "uk-UA-Chirp3-HD-Vindemiatrix",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Zephyr",
    "name": "uk-UA-Chirp3-HD-Zephyr",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Chirp3-HD-Zubenelgenubi",
    "name": "uk-UA-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Standard-B",
    "name": "uk-UA-Standard-B",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "uk-UA-Wavenet-B",
    "name": "uk-UA-Wavenet-B",
    "languages": [
      "uk-UA"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Achernar",
    "name": "ur-IN-Chirp3-HD-Achernar",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Achird",
    "name": "ur-IN-Chirp3-HD-Achird",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Algenib",
    "name": "ur-IN-Chirp3-HD-Algenib",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Algieba",
    "name": "ur-IN-Chirp3-HD-Algieba",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Alnilam",
    "name": "ur-IN-Chirp3-HD-Alnilam",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Aoede",
    "name": "ur-IN-Chirp3-HD-Aoede",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Autonoe",
    "name": "ur-IN-Chirp3-HD-Autonoe",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Callirrhoe",
    "name": "ur-IN-Chirp3-HD-Callirrhoe",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Charon",
    "name": "ur-IN-Chirp3-HD-Charon",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Despina",
    "name": "ur-IN-Chirp3-HD-Despina",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Enceladus",
    "name": "ur-IN-Chirp3-HD-Enceladus",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Erinome",
    "name": "ur-IN-Chirp3-HD-Erinome",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Fenrir",
    "name": "ur-IN-Chirp3-HD-Fenrir",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Gacrux",
    "name": "ur-IN-Chirp3-HD-Gacrux",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Iapetus",
    "name": "ur-IN-Chirp3-HD-Iapetus",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Kore",
    "name": "ur-IN-Chirp3-HD-Kore",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Laomedeia",
    "name": "ur-IN-Chirp3-HD-Laomedeia",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Leda",
    "name": "ur-IN-Chirp3-HD-Leda",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Orus",
    "name": "ur-IN-Chirp3-HD-Orus",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Puck",
    "name": "ur-IN-Chirp3-HD-Puck",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Pulcherrima",
    "name": "ur-IN-Chirp3-HD-Pulcherrima",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Rasalgethi",
    "name": "ur-IN-Chirp3-HD-Rasalgethi",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Sadachbia",
    "name": "ur-IN-Chirp3-HD-Sadachbia",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Sadaltager",
    "name": "ur-IN-Chirp3-HD-Sadaltager",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Schedar",
    "name": "ur-IN-Chirp3-HD-Schedar",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Sulafat",
    "name": "ur-IN-Chirp3-HD-Sulafat",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Umbriel",
    "name": "ur-IN-Chirp3-HD-Umbriel",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Vindemiatrix",
    "name": "ur-IN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Zephyr",
    "name": "ur-IN-Chirp3-HD-Zephyr",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Chirp3-HD-Zubenelgenubi",
    "name": "ur-IN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Standard-A",
    "name": "ur-IN-Standard-A",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Standard-B",
    "name": "ur-IN-Standard-B",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Wavenet-A",
    "name": "ur-IN-Wavenet-A",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "ur-IN-Wavenet-B",
    "name": "ur-IN-Wavenet-B",
    "languages": [
      "ur-IN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Achernar",
    "name": "vi-VN-Chirp3-HD-Achernar",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Achird",
    "name": "vi-VN-Chirp3-HD-Achird",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Algenib",
    "name": "vi-VN-Chirp3-HD-Algenib",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Algieba",
    "name": "vi-VN-Chirp3-HD-Algieba",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Alnilam",
    "name": "vi-VN-Chirp3-HD-Alnilam",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Aoede",
    "name": "vi-VN-Chirp3-HD-Aoede",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Autonoe",
    "name": "vi-VN-Chirp3-HD-Autonoe",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Callirrhoe",
    "name": "vi-VN-Chirp3-HD-Callirrhoe",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Charon",
    "name": "vi-VN-Chirp3-HD-Charon",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Despina",
    "name": "vi-VN-Chirp3-HD-Despina",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Enceladus",
    "name": "vi-VN-Chirp3-HD-Enceladus",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Erinome",
    "name": "vi-VN-Chirp3-HD-Erinome",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Fenrir",
    "name": "vi-VN-Chirp3-HD-Fenrir",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Gacrux",
    "name": "vi-VN-Chirp3-HD-Gacrux",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Iapetus",
    "name": "vi-VN-Chirp3-HD-Iapetus",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Kore",
    "name": "vi-VN-Chirp3-HD-Kore",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Laomedeia",
    "name": "vi-VN-Chirp3-HD-Laomedeia",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Leda",
    "name": "vi-VN-Chirp3-HD-Leda",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Orus",
    "name": "vi-VN-Chirp3-HD-Orus",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Puck",
    "name": "vi-VN-Chirp3-HD-Puck",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Pulcherrima",
    "name": "vi-VN-Chirp3-HD-Pulcherrima",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Rasalgethi",
    "name": "vi-VN-Chirp3-HD-Rasalgethi",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Sadachbia",
    "name": "vi-VN-Chirp3-HD-Sadachbia",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Sadaltager",
    "name": "vi-VN-Chirp3-HD-Sadaltager",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Schedar",
    "name": "vi-VN-Chirp3-HD-Schedar",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Sulafat",
    "name": "vi-VN-Chirp3-HD-Sulafat",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Umbriel",
    "name": "vi-VN-Chirp3-HD-Umbriel",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Vindemiatrix",
    "name": "vi-VN-Chirp3-HD-Vindemiatrix",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Zephyr",
    "name": "vi-VN-Chirp3-HD-Zephyr",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Chirp3-HD-Zubenelgenubi",
    "name": "vi-VN-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Neural2-A",
    "name": "vi-VN-Neural2-A",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Neural2-D",
    "name": "vi-VN-Neural2-D",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Standard-A",
    "name": "vi-VN-Standard-A",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Standard-B",
    "name": "vi-VN-Standard-B",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Standard-C",
    "name": "vi-VN-Standard-C",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Standard-D",
    "name": "vi-VN-Standard-D",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Wavenet-A",
    "name": "vi-VN-Wavenet-A",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Wavenet-B",
    "name": "vi-VN-Wavenet-B",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Wavenet-C",
    "name": "vi-VN-Wavenet-C",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "vi-VN-Wavenet-D",
    "name": "vi-VN-Wavenet-D",
    "languages": [
      "vi-VN"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Achernar",
    "name": "yue-HK-Chirp3-HD-Achernar",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Achird",
    "name": "yue-HK-Chirp3-HD-Achird",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Algenib",
    "name": "yue-HK-Chirp3-HD-Algenib",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Algieba",
    "name": "yue-HK-Chirp3-HD-Algieba",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Alnilam",
    "name": "yue-HK-Chirp3-HD-Alnilam",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Aoede",
    "name": "yue-HK-Chirp3-HD-Aoede",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Autonoe",
    "name": "yue-HK-Chirp3-HD-Autonoe",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Callirrhoe",
    "name": "yue-HK-Chirp3-HD-Callirrhoe",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Charon",
    "name": "yue-HK-Chirp3-HD-Charon",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Despina",
    "name": "yue-HK-Chirp3-HD-Despina",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Enceladus",
    "name": "yue-HK-Chirp3-HD-Enceladus",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Erinome",
    "name": "yue-HK-Chirp3-HD-Erinome",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Fenrir",
    "name": "yue-HK-Chirp3-HD-Fenrir",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Gacrux",
    "name": "yue-HK-Chirp3-HD-Gacrux",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Iapetus",
    "name": "yue-HK-Chirp3-HD-Iapetus",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Kore",
    "name": "yue-HK-Chirp3-HD-Kore",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Laomedeia",
    "name": "yue-HK-Chirp3-HD-Laomedeia",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Leda",
    "name": "yue-HK-Chirp3-HD-Leda",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Orus",
    "name": "yue-HK-Chirp3-HD-Orus",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Puck",
    "name": "yue-HK-Chirp3-HD-Puck",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Pulcherrima",
    "name": "yue-HK-Chirp3-HD-Pulcherrima",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Rasalgethi",
    "name": "yue-HK-Chirp3-HD-Rasalgethi",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Sadachbia",
    "name": "yue-HK-Chirp3-HD-Sadachbia",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Sadaltager",
    "name": "yue-HK-Chirp3-HD-Sadaltager",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Schedar",
    "name": "yue-HK-Chirp3-HD-Schedar",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Sulafat",
    "name": "yue-HK-Chirp3-HD-Sulafat",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Umbriel",
    "name": "yue-HK-Chirp3-HD-Umbriel",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Vindemiatrix",
    "name": "yue-HK-Chirp3-HD-Vindemiatrix",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Zephyr",
    "name": "yue-HK-Chirp3-HD-Zephyr",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Chirp3-HD-Zubenelgenubi",
    "name": "yue-HK-Chirp3-HD-Zubenelgenubi",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Standard-A",
    "name": "yue-HK-Standard-A",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Standard-B",
    "name": "yue-HK-Standard-B",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Standard-C",
    "name": "yue-HK-Standard-C",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "FEMALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "GOOGLE",
    "voice_id": "yue-HK-Standard-D",
    "name": "yue-HK-Standard-D",
    "languages": [
      "yue-HK"
    ],
    "ssml_gender": "MALE",
    "natural_sample_rate_hertz": 24000
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "CwhRBWXzGAHq8TQ4Fs17",
    "name": "Roger - Laid-Back, Casual, Resonant",
    "category": "premade",
    "labels": {
      "use_case": "conversational",
      "gender": "male",
      "accent": "american",
      "age": "middle_aged",
      "language": "en",
      "descriptive": "classy"
    },
    "description": "Easy going and perfect for casual conversations.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/CwhRBWXzGAHq8TQ4Fs17/58ee3ff5-f6f2-4628-93b8-e38eb31806b0.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "EXAVITQu4vr4xnSDxMaL",
    "name": "Sarah - Mature, Reassuring, Confident",
    "category": "premade",
    "labels": {
      "use_case": "entertainment_tv",
      "gender": "female",
      "accent": "american",
      "age": "young",
      "language": "en",
      "descriptive": "professional"
    },
    "description": "Young adult woman with a confident and warm, mature quality and a reassuring, professional tone.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/EXAVITQu4vr4xnSDxMaL/01a3e33c-6e99-4ee7-8543-ff2216a32186.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "FGY2WhTYpPnrIDTdsKH5",
    "name": "Laura - Enthusiast, Quirky Attitude",
    "category": "premade",
    "labels": {
      "use_case": "social_media",
      "gender": "female",
      "accent": "american",
      "age": "young",
      "language": "en",
      "descriptive": "sassy"
    },
    "description": "This young adult female voice delivers sunny enthusiasm with a quirky attitude.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/FGY2WhTYpPnrIDTdsKH5/67341759-ad08-41a5-be6e-de12fe448618.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "IKne3meq5aSn9XLyUdCD",
    "name": "Charlie - Deep, Confident, Energetic",
    "category": "premade",
    "labels": {
      "use_case": "conversational",
      "gender": "male",
      "accent": "australian",
      "age": "young",
      "language": "en",
      "descriptive": "hyped"
    },
    "description": "A young Australian male with a confident and energetic voice.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/IKne3meq5aSn9XLyUdCD/102de6f2-22ed-43e0-a1f1-111fa75c5481.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "JBFqnCBsd6RMkjVDRZzb",
    "name": "George - Warm, Captivating Storyteller",
    "category": "premade",
    "labels": {
      "use_case": "narrative_story",
      "gender": "male",
      "accent": "british",
      "age": "middle_aged",
      "language": "en",
      "descriptive": "mature"
    },
    "description": "Warm resonance that instantly captivates listeners.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/JBFqnCBsd6RMkjVDRZzb/e6206d1a-0721-4787-aafb-06a6e705cac5.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "N2lVS1w4EtoT3dr4eOWO",
    "name": "Callum - Husky Trickster",
    "category": "premade",
    "labels": {
      "use_case": "characters_animation",
      "gender": "male",
      "accent": "american",
      "age": "middle_aged",
      "language": "en"
    },
    "description": "Deceptively gravelly, yet unsettling edge.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/N2lVS1w4EtoT3dr4eOWO/ac833bd8-ffda-4938-9ebc-b0f99ca25481.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "SAz9YHcvj6GT2YYXdXww",
    "name": "River - Relaxed, Neutral, Informative",
    "category": "premade",
    "labels": {
      "use_case": "conversational",
      "gender": "neutral",
      "accent": "american",
      "age": "middle_aged",
      "language": "en",
      "descriptive": "calm"
    },
    "description": "A relaxed, neutral voice ready for narrations or conversational projects.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/SAz9YHcvj6GT2YYXdXww/e6c95f0b-2227-491a-b3d7-2249240decb7.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "SOYHLrjzK2X1ezoPC6cr",
    "name": "Harry - Fierce Warrior",
    "category": "premade",
    "labels": {
      "use_case": "characters_animation",
      "gender": "male",
      "accent": "american",
      "age": "young",
      "language": "en",
      "descriptive": "rough"
    },
    "description": "An animated warrior ready to charge forward.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/SOYHLrjzK2X1ezoPC6cr/86d178f6-f4b6-4e0e-85be-3de19f490794.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "TX3LPaxmHKxFdv7VOQHJ",
    "name": "Liam - Energetic, Social Media Creator",
    "category": "premade",
    "labels": {
      "use_case": "social_media",
      "gender": "male",
      "accent": "american",
      "age": "young",
      "language": "en",
      "descriptive": "confident"
    },
    "description": "A young adult with energy and warmth - suitable for reels and shorts.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/TX3LPaxmHKxFdv7VOQHJ/63148076-6363-42db-aea8-31424308b92c.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "Xb7hH8MSUJpSbSDYk0k2",
    "name": "Alice - Clear, Engaging Educator",
    "category": "premade",
    "labels": {
      "use_case": "informative_educational",
      "gender": "female",
      "accent": "british",
      "age": "middle_aged",
      "language": "en",
      "descriptive": "professional"
    },
    "description": "Clear and engaging, friendly woman with a British accent suitable for e-learning.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/Xb7hH8MSUJpSbSDYk0k2/d10f7534-11f6-41fe-a012-2de1e482d336.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "XrExE9yKIg1WjnnlVkGX",
    "name": "Matilda - Knowledgable, Professional",
    "category": "premade",
    "labels": {
      "use_case": "informative_educational",
      "gender": "female",
      "accent": "american",
      "age": "middle_aged",
      "language": "en",
      "descriptive": "upbeat"
    },
    "description": "A professional woman with a pleasing alto pitch. Suitable for many use cases.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/XrExE9yKIg1WjnnlVkGX/b930e18d-6b4d-466e-bab2-0ae97c6d8535.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "bIHbv24MWmeRgasZH58o",
    "name": "Will - Relaxed Optimist",
    "category": "premade",
    "labels": {
      "use_case": "conversational",
      "gender": "male",
      "accent": "american",
      "age": "young",
      "language": "en",
      "descriptive": "chill"
    },
    "description": "Conversational and laid back.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/bIHbv24MWmeRgasZH58o/8caf8f3d-ad29-4980-af41-53f20c72d7a4.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "cgSgspJ2msm6clMCkdW9",
    "name": "Jessica - Playful, Bright, Warm",
    "category": "premade",
    "labels": {
      "use_case": "conversational",
      "gender": "female",
      "accent": "american",
      "age": "young",
      "language": "en",
      "descriptive": "cute"
    },
    "description": "Young and popular, this playful American female voice is perfect for trendy content.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/cgSgspJ2msm6clMCkdW9/56a97bf8-b69b-448f-846c-c3a11683d45a.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "cjVigY5qzO86Huf0OWal",
    "name": "Eric - Smooth, Trustworthy",
    "category": "premade",
    "labels": {
      "use_case": "conversational",
      "gender": "male",
      "accent": "american",
      "age": "middle_aged",
      "language": "en",
      "descriptive": "classy"
    },
    "description": "A smooth tenor pitch from a man in his 40s - perfect for agentic use cases.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/cjVigY5qzO86Huf0OWal/d098fda0-6456-4030-b3d8-63aa048c9070.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "hpp4J3VqNfWAUOO0d1Us",
    "name": "Bella - Professional, Bright, Warm",
    "category": "premade",
    "labels": {
      "use_case": "informative_educational",
      "gender": "female",
      "accent": "american",
      "age": "middle_aged",
      "language": "en",
      "descriptive": "professional"
    },
    "description": "This voice is warm, bright, and professional, characterized by a Standard American accent and a polished, narrative quality. It features a medium-high pitch with crisp diction and a deliberate, rhythmic pace that makes it highly intelligible and engaging for long-form listening.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/hpp4J3VqNfWAUOO0d1Us/dab0f5ba-3aa4-48a8-9fad-f138fea1126d.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "iP95p4xoKVk53GoZ742B",
    "name": "Chris - Charming, Down-to-Earth",
    "category": "premade",
    "labels": {
      "use_case": "conversational",
      "gender": "male",
      "accent": "american",
      "age": "middle_aged",
      "language": "en",
      "descriptive": "casual"
    },
    "description": "Natural and real, this down-to-earth voice is great across many use-cases.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/iP95p4xoKVk53GoZ742B/3f4bde72-cc48-40dd-829f-57fbf906f4d7.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "nPczCjzI2devNBz1zQrb",
    "name": "Brian - Deep, Resonant and Comforting",
    "category": "premade",
    "labels": {
      "use_case": "social_media",
      "gender": "male",
      "accent": "american",
      "age": "middle_aged",
      "language": "en",
      "descriptive": "classy"
    },
    "description": "Middle-aged man with a resonant and comforting tone. Great for narrations and advertisements.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/nPczCjzI2devNBz1zQrb/2dd3e72c-4fd3-42f1-93ea-abc5d4e5aa1d.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "onwK4e9ZLuTAKqWW03F9",
    "name": "Daniel - Steady Broadcaster",
    "category": "premade",
    "labels": {
      "use_case": "informative_educational",
      "gender": "male",
      "accent": "british",
      "age": "middle_aged",
      "language": "en",
      "descriptive": "formal"
    },
    "description": "A strong voice perfect for delivering a professional broadcast or news story.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/onwK4e9ZLuTAKqWW03F9/7eee0236-1a72-4b86-b303-5dcadc007ba9.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "pFZP5JQG7iQjIQuC4Bku",
    "name": "Lily - Velvety Actress",
    "category": "premade",
    "labels": {
      "use_case": "informative_educational",
      "gender": "female",
      "accent": "british",
      "age": "middle_aged",
      "language": "en",
      "descriptive": "confident"
    },
    "description": "Velvety British female voice delivers news and narrations with warmth and clarity.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/pFZP5JQG7iQjIQuC4Bku/89b68b35-b3dd-4348-a84a-a3c13a3c2b30.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "pNInz6obpgDQGcFmaJgB",
    "name": "Adam - Dominant, Firm",
    "category": "premade",
    "labels": {
      "use_case": "social_media",
      "gender": "male",
      "accent": "american",
      "age": "middle_aged",
      "language": "en"
    },
    "description": "A bright tenor pitch that immediately cuts through. The delivery is brash and openly confident, speaking with unwavering certainty and a slightly aggressive self-assurance.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/pNInz6obpgDQGcFmaJgB/d6905d7a-dd26-4187-bfff-1bd3a5ea7cac.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "pqHfZKP75CvOlQylNhV4",
    "name": "Bill - Wise, Mature, Balanced",
    "category": "premade",
    "labels": {
      "use_case": "advertisement",
      "gender": "male",
      "accent": "american",
      "age": "old",
      "language": "en",
      "descriptive": "crisp"
    },
    "description": "Friendly and comforting voice ready to narrate your stories.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/pqHfZKP75CvOlQylNhV4/d782b3ff-84ba-4029-848c-acf01285524d.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "kh59ZgGFT1YQNe4P0U2V",
    "name": "Fernanda Velez 1",
    "category": "generated",
    "labels": {
      "language": "es"
    },
    "description": "Perfect audio quality, studio-quality recording. A 28-year-old female with a sweet, charming, and soft Colombian accent from Bogotá. Her tone is warm, friendly, and deeply endearing. She speaks at a relaxed, conversational pace with a natural, melodic rhythm. She sounds like a very approachable, lovely, yet highly capable art gallery assistant who easily connects with people and makes them feel right at home.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/database/workspace/be17d2e8b82a4ef2b2f60f45f04587a2/voices/kh59ZgGFT1YQNe4P0U2V/7c00954f-4f78-415b-b606-93d871560e53.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "6fCgvtwGV3EuT2W6NpkC",
    "name": "Paisa 1",
    "category": "generated",
    "labels": {
      "gender": "female",
      "accent": "es-latin-american",
      "age": "young",
      "language": "es"
    },
    "description": "Native Spanish, Colombian. Female, 25 years old. Studio quality recording, noise-free signal. Magnetic and joyful digital influencer. Radiantly happy, witty, and charmingly persuasive. Very bright and buttery timbre with a clear, forward proximity as if speaking directly into a high-end studio microphone. Pacing is rhythmic and musical, featuring the iconic \"sing-song\" melodic lift at the end of sentences typical of Antioquia. Expressive and animated delivery with natural breathiness.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/database/workspace/be17d2e8b82a4ef2b2f60f45f04587a2/voices/6fCgvtwGV3EuT2W6NpkC/d6a097d3-5e08-4ef3-8c11-84d8c4589387.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "gcAJmlnwJ8sPTGGWgC0B",
    "name": "Colombiana",
    "category": "generated",
    "labels": {
      "gender": "female",
      "accent": "es-latin-american",
      "age": "young",
      "language": "es"
    },
    "description": "Perfect audio quality. A 25-year-old female with a thick Colombian accent from Medellin. Her tone is warm, smooth, and melodious. She speaks at a natural, calm, and conversational pace. She sounds fun, charming, and approachable, like she is chatting casually with a close friend.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/database/workspace/be17d2e8b82a4ef2b2f60f45f04587a2/voices/gcAJmlnwJ8sPTGGWgC0B/52798879-90dd-4fcb-af5f-ac2643bcc66d.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "rXY1z4wbLU6JPeCTH3D3",
    "name": "Fernanda Velez 2",
    "category": "generated",
    "labels": {
      "language": "es"
    },
    "description": "Perfect audio quality, recorded close to the mic like a high-quality voice message. A 30-year-old female with a highly natural, charming, and clear Colombian accent from Bogotá. Her tone is warm, effortlessly professional, and intimately conversational. She speaks at a relaxed, everyday pace with natural pauses, slight breaths, and a friendly cadence, exactly like sending an efficient but personal voice note to a valued client or friend.",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/database/workspace/be17d2e8b82a4ef2b2f60f45f04587a2/voices/rXY1z4wbLU6JPeCTH3D3/abf688df-1070-45bc-8dd1-6e07b4807623.mp3"
  },
  {
    "provider": "ELEVENLABS",
    "voice_id": "uZSVlfKbjQq3kGazBT1h",
    "name": "Paisa 2",
    "category": "generated",
    "labels": {
      "gender": "male",
      "accent": "es-latin-american",
      "age": "young",
      "language": "es"
    },
    "description": "Native Spanish, Colombian (paisa/Medellín). Female, 30 years old. Studio quality recording, noise-free signal. Persona: Magnetic and joyful digital influencer. Emotion: Radiantly happy, witty, and charmingly persuasive. Very bright and buttery timbre with a clear, forward proximity as if speaking directly into a high-end studio microphone. Pacing is rhythmic and musical, featuring the iconic \"sing-song\" melodic lift at the end of sentences typical of Antioquia. ",
    "preview_url": "https://storage.googleapis.com/eleven-public-prod/database/workspace/be17d2e8b82a4ef2b2f60f45f04587a2/voices/uZSVlfKbjQq3kGazBT1h/9fedf4d0-a076-4b05-ab95-98c5bf39d192.mp3"
  }
]
```

---

## ✅ PASS — GET /audio/providers/models — Listar modelos disponibles

**Request:**
```
GET https://quevino-audio-2lkhisz2aa-uc.a.run.app/audio/providers/models
```

**Response:** HTTP `200` (esperado: `200`)
```json
[
  {
    "provider": "GOOGLE",
    "model_id": "journey",
    "name": "Google Journey (Premium)"
  },
  {
    "provider": "GOOGLE",
    "model_id": "studio",
    "name": "Google Studio (High-Fidelity)"
  },
  {
    "provider": "GOOGLE",
    "model_id": "wavenet",
    "name": "Google WaveNet (Neural)"
  },
  {
    "provider": "GOOGLE",
    "model_id": "standard",
    "name": "Google Standard"
  },
  {
    "provider": "ELEVENLABS",
    "model_id": "eleven_v3",
    "name": "Eleven v3",
    "description": "The most expressive model. Supports 70+ languages. Requires more prompt engineering than our previous models.",
    "can_do_text_to_speech": true,
    "languages": [
      {
        "language_id": "af",
        "name": "Afrikaans"
      },
      {
        "language_id": "ar",
        "name": "Arabic"
      },
      {
        "language_id": "hy",
        "name": "Armenian"
      },
      {
        "language_id": "as",
        "name": "Assamese"
      },
      {
        "language_id": "az",
        "name": "Azerbaijani"
      },
      {
        "language_id": "be",
        "name": "Belarusian"
      },
      {
        "language_id": "bn",
        "name": "Bengali"
      },
      {
        "language_id": "bs",
        "name": "Bosnian"
      },
      {
        "language_id": "bg",
        "name": "Bulgarian"
      },
      {
        "language_id": "ca",
        "name": "Catalan"
      },
      {
        "language_id": "ceb",
        "name": "Cebuano"
      },
      {
        "language_id": "ny",
        "name": "Chichewa"
      },
      {
        "language_id": "hr",
        "name": "Croatian"
      },
      {
        "language_id": "cs",
        "name": "Czech"
      },
      {
        "language_id": "da",
        "name": "Danish"
      },
      {
        "language_id": "nl",
        "name": "Dutch"
      },
      {
        "language_id": "en",
        "name": "English"
      },
      {
        "language_id": "et",
        "name": "Estonian"
      },
      {
        "language_id": "fil",
        "name": "Filipino"
      },
      {
        "language_id": "fi",
        "name": "Finnish"
      },
      {
        "language_id": "fr",
        "name": "French"
      },
      {
        "language_id": "gl",
        "name": "Galician"
      },
      {
        "language_id": "ka",
        "name": "Georgian"
      },
      {
        "language_id": "de",
        "name": "German"
      },
      {
        "language_id": "el",
        "name": "Greek"
      },
      {
        "language_id": "gu",
        "name": "Gujarati"
      },
      {
        "language_id": "ha",
        "name": "Hausa"
      },
      {
        "language_id": "he",
        "name": "Hebrew"
      },
      {
        "language_id": "hi",
        "name": "Hindi"
      },
      {
        "language_id": "hu",
        "name": "Hungarian"
      },
      {
        "language_id": "is",
        "name": "Icelandic"
      },
      {
        "language_id": "id",
        "name": "Indonesian"
      },
      {
        "language_id": "ga",
        "name": "Irish"
      },
      {
        "language_id": "it",
        "name": "Italian"
      },
      {
        "language_id": "ja",
        "name": "Japanese"
      },
      {
        "language_id": "jv",
        "name": "Javanese"
      },
      {
        "language_id": "kn",
        "name": "Kannada"
      },
      {
        "language_id": "kk",
        "name": "Kazakh"
      },
      {
        "language_id": "ky",
        "name": "Kirghiz"
      },
      {
        "language_id": "ko",
        "name": "Korean"
      },
      {
        "language_id": "lv",
        "name": "Latvian"
      },
      {
        "language_id": "ln",
        "name": "Lingala"
      },
      {
        "language_id": "lt",
        "name": "Lithuanian"
      },
      {
        "language_id": "lb",
        "name": "Luxembourgish"
      },
      {
        "language_id": "mk",
        "name": "Macedonian"
      },
      {
        "language_id": "ms",
        "name": "Malay"
      },
      {
        "language_id": "ml",
        "name": "Malayalam"
      },
      {
        "language_id": "zh",
        "name": "Mandarin Chinese"
      },
      {
        "language_id": "mr",
        "name": "Marathi"
      },
      {
        "language_id": "ne",
        "name": "Nepali"
      },
      {
        "language_id": "no",
        "name": "Norwegian"
      },
      {
        "language_id": "ps",
        "name": "Pashto"
      },
      {
        "language_id": "fa",
        "name": "Persian"
      },
      {
        "language_id": "pl",
        "name": "Polish"
      },
      {
        "language_id": "pt",
        "name": "Portuguese"
      },
      {
        "language_id": "pa",
        "name": "Punjabi"
      },
      {
        "language_id": "ro",
        "name": "Romanian"
      },
      {
        "language_id": "ru",
        "name": "Russian"
      },
      {
        "language_id": "sr",
        "name": "Serbian"
      },
      {
        "language_id": "sd",
        "name": "Sindhi"
      },
      {
        "language_id": "sk",
        "name": "Slovak"
      },
      {
        "language_id": "sl",
        "name": "Slovenian"
      },
      {
        "language_id": "so",
        "name": "Somali"
      },
      {
        "language_id": "es",
        "name": "Spanish"
      },
      {
        "language_id": "sw",
        "name": "Swahili"
      },
      {
        "language_id": "sv",
        "name": "Swedish"
      },
      {
        "language_id": "ta",
        "name": "Tamil"
      },
      {
        "language_id": "te",
        "name": "Telugu"
      },
      {
        "language_id": "th",
        "name": "Thai"
      },
      {
        "language_id": "tr",
        "name": "Turkish"
      },
      {
        "language_id": "uk",
        "name": "Ukrainian"
      },
      {
        "language_id": "ur",
        "name": "Urdu"
      },
      {
        "language_id": "vi",
        "name": "Vietnamese"
      },
      {
        "language_id": "cy",
        "name": "Welsh"
      }
    ]
  },
  {
    "provider": "ELEVENLABS",
    "model_id": "eleven_multilingual_v2",
    "name": "Eleven Multilingual v2",
    "description": "Our most life-like, emotionally rich mode in 29 languages. Best for voice overs, audiobooks, post-production, or any other content creation needs.",
    "can_do_text_to_speech": true,
    "languages": [
      {
        "language_id": "en",
        "name": "English"
      },
      {
        "language_id": "ja",
        "name": "Japanese"
      },
      {
        "language_id": "zh",
        "name": "Chinese"
      },
      {
        "language_id": "de",
        "name": "German"
      },
      {
        "language_id": "hi",
        "name": "Hindi"
      },
      {
        "language_id": "fr",
        "name": "French"
      },
      {
        "language_id": "ko",
        "name": "Korean"
      },
      {
        "language_id": "pt",
        "name": "Portuguese"
      },
      {
        "language_id": "it",
        "name": "Italian"
      },
      {
        "language_id": "es",
        "name": "Spanish"
      },
      {
        "language_id": "id",
        "name": "Indonesian"
      },
      {
        "language_id": "nl",
        "name": "Dutch"
      },
      {
        "language_id": "tr",
        "name": "Turkish"
      },
      {
        "language_id": "fil",
        "name": "Filipino"
      },
      {
        "language_id": "pl",
        "name": "Polish"
      },
      {
        "language_id": "sv",
        "name": "Swedish"
      },
      {
        "language_id": "bg",
        "name": "Bulgarian"
      },
      {
        "language_id": "ro",
        "name": "Romanian"
      },
      {
        "language_id": "ar",
        "name": "Arabic"
      },
      {
        "language_id": "cs",
        "name": "Czech"
      },
      {
        "language_id": "el",
        "name": "Greek"
      },
      {
        "language_id": "fi",
        "name": "Finnish"
      },
      {
        "language_id": "hr",
        "name": "Croatian"
      },
      {
        "language_id": "ms",
        "name": "Malay"
      },
      {
        "language_id": "sk",
        "name": "Slovak"
      },
      {
        "language_id": "da",
        "name": "Danish"
      },
      {
        "language_id": "ta",
        "name": "Tamil"
      },
      {
        "language_id": "uk",
        "name": "Ukrainian"
      },
      {
        "language_id": "ru",
        "name": "Russian"
      }
    ]
  },
  {
    "provider": "ELEVENLABS",
    "model_id": "eleven_flash_v2_5",
    "name": "Eleven Flash v2.5",
    "description": "Our ultra low latency model in 32 languages. Ideal for conversational use cases.",
    "can_do_text_to_speech": true,
    "languages": [
      {
        "language_id": "en",
        "name": "English"
      },
      {
        "language_id": "ja",
        "name": "Japanese"
      },
      {
        "language_id": "zh",
        "name": "Chinese"
      },
      {
        "language_id": "de",
        "name": "German"
      },
      {
        "language_id": "hi",
        "name": "Hindi"
      },
      {
        "language_id": "fr",
        "name": "French"
      },
      {
        "language_id": "ko",
        "name": "Korean"
      },
      {
        "language_id": "pt",
        "name": "Portuguese"
      },
      {
        "language_id": "it",
        "name": "Italian"
      },
      {
        "language_id": "es",
        "name": "Spanish"
      },
      {
        "language_id": "ru",
        "name": "Russian"
      },
      {
        "language_id": "id",
        "name": "Indonesian"
      },
      {
        "language_id": "nl",
        "name": "Dutch"
      },
      {
        "language_id": "tr",
        "name": "Turkish"
      },
      {
        "language_id": "fil",
        "name": "Filipino"
      },
      {
        "language_id": "pl",
        "name": "Polish"
      },
      {
        "language_id": "sv",
        "name": "Swedish"
      },
      {
        "language_id": "bg",
        "name": "Bulgarian"
      },
      {
        "language_id": "ro",
        "name": "Romanian"
      },
      {
        "language_id": "ar",
        "name": "Arabic"
      },
      {
        "language_id": "cs",
        "name": "Czech"
      },
      {
        "language_id": "el",
        "name": "Greek"
      },
      {
        "language_id": "fi",
        "name": "Finnish"
      },
      {
        "language_id": "hr",
        "name": "Croatian"
      },
      {
        "language_id": "ms",
        "name": "Malay"
      },
      {
        "language_id": "sk",
        "name": "Slovak"
      },
      {
        "language_id": "da",
        "name": "Danish"
      },
      {
        "language_id": "ta",
        "name": "Tamil"
      },
      {
        "language_id": "uk",
        "name": "Ukrainian"
      },
      {
        "language_id": "hu",
        "name": "Hungarian"
      },
      {
        "language_id": "no",
        "name": "Norwegian"
      },
      {
        "language_id": "vi",
        "name": "Vietnamese"
      }
    ]
  },
  {
    "provider": "ELEVENLABS",
    "model_id": "eleven_turbo_v2_5",
    "name": "Eleven Turbo v2.5",
    "description": "Our high quality, low latency model in 32 languages. Best for developer use cases where speed matters and you need non-English languages.",
    "can_do_text_to_speech": true,
    "languages": [
      {
        "language_id": "en",
        "name": "English"
      },
      {
        "language_id": "ja",
        "name": "Japanese"
      },
      {
        "language_id": "zh",
        "name": "Chinese"
      },
      {
        "language_id": "de",
        "name": "German"
      },
      {
        "language_id": "hi",
        "name": "Hindi"
      },
      {
        "language_id": "fr",
        "name": "French"
      },
      {
        "language_id": "ko",
        "name": "Korean"
      },
      {
        "language_id": "pt",
        "name": "Portuguese"
      },
      {
        "language_id": "it",
        "name": "Italian"
      },
      {
        "language_id": "es",
        "name": "Spanish"
      },
      {
        "language_id": "ru",
        "name": "Russian"
      },
      {
        "language_id": "id",
        "name": "Indonesian"
      },
      {
        "language_id": "nl",
        "name": "Dutch"
      },
      {
        "language_id": "tr",
        "name": "Turkish"
      },
      {
        "language_id": "fil",
        "name": "Filipino"
      },
      {
        "language_id": "pl",
        "name": "Polish"
      },
      {
        "language_id": "sv",
        "name": "Swedish"
      },
      {
        "language_id": "bg",
        "name": "Bulgarian"
      },
      {
        "language_id": "ro",
        "name": "Romanian"
      },
      {
        "language_id": "ar",
        "name": "Arabic"
      },
      {
        "language_id": "cs",
        "name": "Czech"
      },
      {
        "language_id": "el",
        "name": "Greek"
      },
      {
        "language_id": "fi",
        "name": "Finnish"
      },
      {
        "language_id": "hr",
        "name": "Croatian"
      },
      {
        "language_id": "ms",
        "name": "Malay"
      },
      {
        "language_id": "sk",
        "name": "Slovak"
      },
      {
        "language_id": "da",
        "name": "Danish"
      },
      {
        "language_id": "ta",
        "name": "Tamil"
      },
      {
        "language_id": "uk",
        "name": "Ukrainian"
      },
      {
        "language_id": "vi",
        "name": "Vietnamese"
      },
      {
        "language_id": "no",
        "name": "Norwegian"
      },
      {
        "language_id": "hu",
        "name": "Hungarian"
      }
    ]
  },
  {
    "provider": "ELEVENLABS",
    "model_id": "eleven_turbo_v2",
    "name": "Eleven Turbo v2",
    "description": "Our English-only, low latency model. Best for developer use cases where speed matters and you only need English. Performance is on par with Turbo v2.5.",
    "can_do_text_to_speech": true,
    "languages": [
      {
        "language_id": "en",
        "name": "English"
      }
    ]
  },
  {
    "provider": "ELEVENLABS",
    "model_id": "eleven_flash_v2",
    "name": "Eleven Flash v2",
    "description": "Our ultra low latency model in english. Ideal for conversational use cases.",
    "can_do_text_to_speech": true,
    "languages": [
      {
        "language_id": "en",
        "name": "English"
      }
    ]
  },
  {
    "provider": "ELEVENLABS",
    "model_id": "eleven_english_sts_v2",
    "name": "Eleven English v2",
    "description": "Our state-of-the-art speech to speech model suitable for scenarios where you need maximum control over the content and prosody of your generations.",
    "can_do_text_to_speech": false,
    "languages": [
      {
        "language_id": "en",
        "name": "English"
      }
    ]
  },
  {
    "provider": "ELEVENLABS",
    "model_id": "eleven_monolingual_v1",
    "name": "Eleven English v1",
    "description": "Our first ever text to speech model. Now outclassed by Multilingual v2 (for content creation) and Turbo v2.5 (for low latency use cases).",
    "can_do_text_to_speech": true,
    "languages": [
      {
        "language_id": "en",
        "name": "English"
      }
    ]
  },
  {
    "provider": "ELEVENLABS",
    "model_id": "eleven_multilingual_sts_v2",
    "name": "Eleven Multilingual v2",
    "description": "Our cutting-edge, multilingual speech-to-speech model is designed for situations that demand unparalleled control over both the content and the prosody of the generated speech across various languages.",
    "can_do_text_to_speech": false,
    "languages": [
      {
        "language_id": "en",
        "name": "English"
      },
      {
        "language_id": "ja",
        "name": "Japanese"
      },
      {
        "language_id": "zh",
        "name": "Chinese"
      },
      {
        "language_id": "de",
        "name": "German"
      },
      {
        "language_id": "hi",
        "name": "Hindi"
      },
      {
        "language_id": "fr",
        "name": "French"
      },
      {
        "language_id": "ko",
        "name": "Korean"
      },
      {
        "language_id": "pt",
        "name": "Portuguese"
      },
      {
        "language_id": "it",
        "name": "Italian"
      },
      {
        "language_id": "es",
        "name": "Spanish"
      },
      {
        "language_id": "ru",
        "name": "Russian"
      },
      {
        "language_id": "id",
        "name": "Indonesian"
      },
      {
        "language_id": "nl",
        "name": "Dutch"
      },
      {
        "language_id": "tr",
        "name": "Turkish"
      },
      {
        "language_id": "fil",
        "name": "Filipino"
      },
      {
        "language_id": "pl",
        "name": "Polish"
      },
      {
        "language_id": "sv",
        "name": "Swedish"
      },
      {
        "language_id": "bg",
        "name": "Bulgarian"
      },
      {
        "language_id": "ro",
        "name": "Romanian"
      },
      {
        "language_id": "ar",
        "name": "Arabic"
      },
      {
        "language_id": "cs",
        "name": "Czech"
      },
      {
        "language_id": "el",
        "name": "Greek"
      },
      {
        "language_id": "fi",
        "name": "Finnish"
      },
      {
        "language_id": "hr",
        "name": "Croatian"
      },
      {
        "language_id": "ms",
        "name": "Malay"
      },
      {
        "language_id": "sk",
        "name": "Slovak"
      },
      {
        "language_id": "da",
        "name": "Danish"
      },
      {
        "language_id": "ta",
        "name": "Tamil"
      },
      {
        "language_id": "uk",
        "name": "Ukrainian"
      }
    ]
  },
  {
    "provider": "ELEVENLABS",
    "model_id": "eleven_multilingual_v1",
    "name": "Eleven Multilingual v1",
    "description": "Our first Multilingual model, capability of generating speech in 10 languages. Now outclassed by Multilingual v2 (for content creation) and Turbo v2.5 (for low latency use cases).",
    "can_do_text_to_speech": true,
    "languages": [
      {
        "language_id": "en",
        "name": "English"
      },
      {
        "language_id": "de",
        "name": "German"
      },
      {
        "language_id": "pl",
        "name": "Polish"
      },
      {
        "language_id": "es",
        "name": "Spanish"
      },
      {
        "language_id": "it",
        "name": "Italian"
      },
      {
        "language_id": "fr",
        "name": "French"
      },
      {
        "language_id": "pt",
        "name": "Portuguese"
      },
      {
        "language_id": "hi",
        "name": "Hindi"
      },
      {
        "language_id": "ar",
        "name": "Arabic"
      }
    ]
  }
]
```

---

## ✅ PASS — POST /audio/generate — Generación ElevenLabs (eleven_multilingual_v2)

**Request:**
```
POST https://quevino-audio-2lkhisz2aa-uc.a.run.app/audio/generate
{
  "text": "Hola, este es un test de integración de la API de audio de Que Vino.",
  "provider": "ELEVENLABS",
  "voice_id": "CwhRBWXzGAHq8TQ4Fs17",
  "model_id": "eleven_multilingual_v2",
  "output_format": "mp3",
  "enrich_audio": false
}
```

**Response:** HTTP `201` (esperado: `201`)
```json
{
  "content_type": "audio/mpeg",
  "size_bytes": 64827,
  "X-Generation-ID": "d9bc9cc8-3c53-41e8-81c0-91d5d7c66fa3",
  "X-Enrichment-Status": "SKIPPED"
}
```

---

## ✅ PASS — POST /audio/generate — Sin token (esperado: 401)

**Request:**
```
POST https://quevino-audio-2lkhisz2aa-uc.a.run.app/audio/generate
{
  "text": "test",
  "provider": "ELEVENLABS",
  "voice_id": "CwhRBWXzGAHq8TQ4Fs17"
}
```

**Response:** HTTP `401` (esperado: `401`)
```json
{
  "error": "UNAUTHORIZED",
  "message": "Missing Bearer Token"
}
```

---

## ✅ PASS — POST /audio/generate — Payload incompleto sin voice_id (esperado: 422)

**Request:**
```
POST https://quevino-audio-2lkhisz2aa-uc.a.run.app/audio/generate
{
  "text": "test",
  "provider": "ELEVENLABS"
}
```

**Response:** HTTP `422` (esperado: `422`)
```json
Faltan parámetros obligatorios: text, provider o voice_id
```

---
