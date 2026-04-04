# Test Results — quevino-knowledge-stores

**Entorno:** Producción (Cloud Run)  
**URL Base:** `https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app`  
**Fecha:** 2026-04-03 18:02:42  
**Resultado:** `6/6` pruebas exitosas  

---

## ✅ PASS — GET /health — Endpoint público (sin autenticación)

**Request:**
```
GET https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/health
```

**Response:** HTTP `200` (esperado: `200`)
```json
{
  "status": "ok",
  "environment": "dev"
}
```

---

## ✅ PASS — GET /knowledge-stores — Listar todos los stores

**Request:**
```
GET https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/knowledge-stores
```

**Response:** HTTP `200` (esperado: `200`)
```json
[
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh",
    "display_name": "grapes"
  },
  {
    "id": "fileSearchStores/regions-lgpvlubvqt3g",
    "display_name": "regions"
  },
  {
    "id": "fileSearchStores/wineries-0ozxegajz53s",
    "display_name": "wineries"
  },
  {
    "id": "fileSearchStores/testintegrationstore-35uva56j1x1o",
    "display_name": "test-integration-store"
  }
]
```

---

## ✅ PASS — GET /knowledge-stores/grapes-bpdsyaih31jh/files — Listar archivos del store

**Request:**
```
GET https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/knowledge-stores/grapes-bpdsyaih31jh/files
```

**Response:** HTTP `200` (esperado: `200`)
```json
[
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmuscat-de-alexandriam-szlxgvyv79ml",
    "display_name": "grapes/Muscat de Alexandria.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Muscat de Alexandria.md",
      "exact_size_bytes": "15622",
      "upload_date": "2026-04-03T23:58:56.418039"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmuscat-blancmd-l22pipmqyd1v",
    "display_name": "grapes/Muscat Blanc.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Muscat Blanc.md",
      "exact_size_bytes": "9032",
      "upload_date": "2026-04-03T23:58:56.417393"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesnebbiolomd-ge0k4aumfsju",
    "display_name": "grapes/Nebbiolo.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Nebbiolo.md",
      "exact_size_bytes": "10081",
      "upload_date": "2026-04-03T23:58:56.729536"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesnerello-mascalesemd-tm3wauypyegs",
    "display_name": "grapes/Nerello Mascalese.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Nerello Mascalese.md",
      "exact_size_bytes": "14563",
      "upload_date": "2026-04-03T23:58:57.234700"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesnegroamaromd-x5n0ykc3gzw8",
    "display_name": "grapes/Negroamaro.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Negroamaro.md",
      "exact_size_bytes": "8939",
      "upload_date": "2026-04-03T23:58:57.195301"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesnero-davolamd-8e3o2iv4s1m5",
    "display_name": "grapes/Nero d'Avola.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Nero d'Avola.md",
      "exact_size_bytes": "10887",
      "upload_date": "2026-04-03T23:58:57.517306"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespetit-verdotmd-1x5o063v16mt",
    "display_name": "grapes/Petit Verdot.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Petit Verdot.md",
      "exact_size_bytes": "10412",
      "upload_date": "2026-04-03T23:58:57.894736"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespetite-sirahmd-u699ls8rf7xt",
    "display_name": "grapes/Petite Sirah.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Petite Sirah.md",
      "exact_size_bytes": "10807",
      "upload_date": "2026-04-03T23:58:57.934487"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespicpoulmd-2fppl17fugw4",
    "display_name": "grapes/Picpoul.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Picpoul.md",
      "exact_size_bytes": "9313",
      "upload_date": "2026-04-03T23:58:58.124909"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespinot-blancmd-0bnlsnjofeyw",
    "display_name": "grapes/Pinot Blanc.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Pinot Blanc.md",
      "exact_size_bytes": "11991",
      "upload_date": "2026-04-03T23:58:58.376872"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespinot-noirmd-5qnk9ccc6c91",
    "display_name": "grapes/Pinot Noir.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Pinot Noir.md",
      "exact_size_bytes": "11705",
      "upload_date": "2026-04-03T23:58:58.862004"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespinot-grismd-cli25nc0x08c",
    "display_name": "grapes/Pinot Gris.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Pinot Gris.md",
      "exact_size_bytes": "12869",
      "upload_date": "2026-04-03T23:58:58.814577"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespinotagemd-osq60ru5qpew",
    "display_name": "grapes/Pinotage.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Pinotage.md",
      "exact_size_bytes": "10690",
      "upload_date": "2026-04-03T23:58:59.080385"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesportomd-cv4h2zpwx6bm",
    "display_name": "grapes/Porto.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Porto.md",
      "exact_size_bytes": "9117",
      "upload_date": "2026-04-03T23:58:59.520980"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesproseccomd-emexad3a73jj",
    "display_name": "grapes/Prosecco.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Prosecco.md",
      "exact_size_bytes": "11902",
      "upload_date": "2026-04-03T23:58:59.560584"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesrieslingmd-gdaptuh2qemk",
    "display_name": "grapes/Riesling.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Riesling.md",
      "exact_size_bytes": "9880",
      "upload_date": "2026-04-03T23:58:59.796064"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesroussannemd-l8awy8xmspy2",
    "display_name": "grapes/Roussanne.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Roussanne.md",
      "exact_size_bytes": "10488",
      "upload_date": "2026-04-03T23:59:00.291545"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessagrantinomd-02ieli7m1wwa",
    "display_name": "grapes/Sagrantino.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Sagrantino.md",
      "exact_size_bytes": "8555",
      "upload_date": "2026-04-03T23:59:00.334328"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessangiovesemd-nipqqmi8lkhw",
    "display_name": "grapes/Sangiovese.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Sangiovese.md",
      "exact_size_bytes": "15421",
      "upload_date": "2026-04-03T23:59:00.604802"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessauvignon-blancmd-fa7ngurf5uxh",
    "display_name": "grapes/Sauvignon Blanc.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Sauvignon Blanc.md",
      "exact_size_bytes": "10926",
      "upload_date": "2026-04-03T23:59:01.070458"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessauternesmd-i9zwss2xvgl4",
    "display_name": "grapes/Sauternes.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Sauternes.md",
      "exact_size_bytes": "14506",
      "upload_date": "2026-04-03T23:59:00.967792"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesschiavamd-rsr2cgb3ijj3",
    "display_name": "grapes/Schiava.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Schiava.md",
      "exact_size_bytes": "13036",
      "upload_date": "2026-04-03T23:59:01.604727"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessavatianomd-oay4anwj4510",
    "display_name": "grapes/Savatiano.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Savatiano.md",
      "exact_size_bytes": "8744",
      "upload_date": "2026-04-03T23:59:01.604212"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessemillonmd-fgip2lwp7l1c",
    "display_name": "grapes/Sémillon.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Sémillon.md",
      "exact_size_bytes": "12274",
      "upload_date": "2026-04-03T23:59:01.604861"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessherrymd-595kaqt61plq",
    "display_name": "grapes/Sherry.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Sherry.md",
      "exact_size_bytes": "12543",
      "upload_date": "2026-04-03T23:59:01.646048"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessyrahmd-m6msur53lfg2",
    "display_name": "grapes/Syrah.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Syrah.md",
      "exact_size_bytes": "10503",
      "upload_date": "2026-04-03T23:59:02.426988"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessilvanermd-uxqucmnr6yls",
    "display_name": "grapes/Silvaner.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Silvaner.md",
      "exact_size_bytes": "8355",
      "upload_date": "2026-04-03T23:59:02.379999"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapestannatmd-jaqwwx9uroq1",
    "display_name": "grapes/Tannat.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Tannat.md",
      "exact_size_bytes": "9328",
      "upload_date": "2026-04-03T23:59:02.471513"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapestempranillomd-zqdbb4w8o8w9",
    "display_name": "grapes/Tempranillo.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Tempranillo.md",
      "exact_size_bytes": "10996",
      "upload_date": "2026-04-03T23:59:02.830403"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapestorrontesmd-69ldflfkw720",
    "display_name": "grapes/Torrontés.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Torrontés.md",
      "exact_size_bytes": "10356",
      "upload_date": "2026-04-03T23:59:03.192832"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapestouriga-nacionalmd-c6uub1rmmnvz",
    "display_name": "grapes/Touriga Nacional.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Touriga Nacional.md",
      "exact_size_bytes": "19192",
      "upload_date": "2026-04-03T23:59:03.719564"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesvalpolicella-blendmd-e4xp72v0qse1",
    "display_name": "grapes/Valpolicella Blend.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Valpolicella Blend.md",
      "exact_size_bytes": "16831",
      "upload_date": "2026-04-03T23:59:03.808713"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapestrebbiano-toscanomd-enkontaqicht",
    "display_name": "grapes/Trebbiano Toscano.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Trebbiano Toscano.md",
      "exact_size_bytes": "10996",
      "upload_date": "2026-04-03T23:59:03.765236"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesverdicchiomd-uib67sahtt74",
    "display_name": "grapes/Verdicchio.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Verdicchio.md",
      "exact_size_bytes": "11383",
      "upload_date": "2026-04-03T23:59:04.224283"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesverdejomd-hlcjoz8fm6gd",
    "display_name": "grapes/Verdejo.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Verdejo.md",
      "exact_size_bytes": "13675",
      "upload_date": "2026-04-03T23:59:03.991228"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesvermentinomd-dnt9md9er875",
    "display_name": "grapes/Vermentino.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Vermentino.md",
      "exact_size_bytes": "18737",
      "upload_date": "2026-04-03T23:59:04.447276"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesvin-santomd-pc5enup3e742",
    "display_name": "grapes/Vin Santo.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Vin Santo.md",
      "exact_size_bytes": "8635",
      "upload_date": "2026-04-03T23:59:04.494111"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesviogniermd-z0zg2ihb8mve",
    "display_name": "grapes/Viognier.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Viognier.md",
      "exact_size_bytes": "13409",
      "upload_date": "2026-04-03T23:59:05.138250"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesvinho-verdemd-imqllnimvt2a",
    "display_name": "grapes/Vinho Verde.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Vinho Verde.md",
      "exact_size_bytes": "13602",
      "upload_date": "2026-04-03T23:59:04.846295"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesviuramd-vdkqj5qeyzlp",
    "display_name": "grapes/Viura.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Viura.md",
      "exact_size_bytes": "17698",
      "upload_date": "2026-04-03T23:59:05.138332"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapeszinfandelmd-pn18gbf86jlm",
    "display_name": "grapes/Zinfandel.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Zinfandel.md",
      "exact_size_bytes": "13319",
      "upload_date": "2026-04-03T23:59:05.667549"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesxinomavromd-pumgoidkfnkp",
    "display_name": "grapes/Xinomavro.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Xinomavro.md",
      "exact_size_bytes": "11234",
      "upload_date": "2026-04-03T23:59:05.576245"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapeszweigeltmd-kyvstcusbetp",
    "display_name": "grapes/Zweigelt.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Zweigelt.md",
      "exact_size_bytes": "12501",
      "upload_date": "2026-04-03T23:59:05.695212"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesbagamd-q94mup2bq6i1",
    "display_name": "grapes/Baga.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Baga.md",
      "exact_size_bytes": "11532",
      "upload_date": "2026-04-04T00:02:25.919902"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesalbarinomd-lu5vfg0eos2p",
    "display_name": "grapes/Albariño.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Albariño.md",
      "exact_size_bytes": "12161",
      "upload_date": "2026-04-04T00:02:25.919740"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesagiorgitikomd-3hwiqsmp3n8a",
    "display_name": "grapes/Agiorgitiko.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Agiorgitiko.md",
      "exact_size_bytes": "11158",
      "upload_date": "2026-04-04T00:02:25.919672"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesalicante-bouschetmd-rrmqhlugdgsk",
    "display_name": "grapes/Alicante Bouschet.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Alicante Bouschet.md",
      "exact_size_bytes": "12791",
      "upload_date": "2026-04-04T00:02:25.919770"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesassyrtikomd-aonulphnzr9w",
    "display_name": "grapes/Assyrtiko.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Assyrtiko.md",
      "exact_size_bytes": "11967",
      "upload_date": "2026-04-04T00:02:25.919876"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesarintomd-gfklb04bkeuy",
    "display_name": "grapes/Arinto.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Arinto.md",
      "exact_size_bytes": "11211",
      "upload_date": "2026-04-04T00:02:25.919847"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesblaufrankischmd-oyosrg3wycam",
    "display_name": "grapes/Blaufränkisch.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Blaufränkisch.md",
      "exact_size_bytes": "13954",
      "upload_date": "2026-04-04T00:02:25.919972"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesbobalmd-bh1010r06a6q",
    "display_name": "grapes/Bobal.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Bobal.md",
      "exact_size_bytes": "13697",
      "upload_date": "2026-04-04T00:02:25.920002"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesbarberamd-1dqt8npy322l",
    "display_name": "grapes/Barbera.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Barbera.md",
      "exact_size_bytes": "15891",
      "upload_date": "2026-04-04T00:02:25.919943"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesbonarda-argentinamd-nt2nszc4vhgh",
    "display_name": "grapes/Bonarda Argentina.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Bonarda Argentina.md",
      "exact_size_bytes": "9870",
      "upload_date": "2026-04-04T00:02:25.963758"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesbordeaux-blend-redmd-a5mi1lxee8vb",
    "display_name": "grapes/Bordeaux Blend (Red).md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Bordeaux Blend (Red).md",
      "exact_size_bytes": "11336",
      "upload_date": "2026-04-04T00:02:27.643782"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesbrachettomd-0edt9io6fc0j",
    "display_name": "grapes/Brachetto.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Brachetto.md",
      "exact_size_bytes": "11340",
      "upload_date": "2026-04-04T00:02:27.643909"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescabernet-francmd-yy0hevm2a866",
    "display_name": "grapes/Cabernet Franc.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Cabernet Franc.md",
      "exact_size_bytes": "12990",
      "upload_date": "2026-04-04T00:02:28.475938"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescabernet-sauvignonmd-0qt992vjorwg",
    "display_name": "grapes/Cabernet Sauvignon.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Cabernet Sauvignon.md",
      "exact_size_bytes": "16334",
      "upload_date": "2026-04-04T00:02:28.605344"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescarignanmd-x9u2wdyneoi4",
    "display_name": "grapes/Carignan.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Carignan.md",
      "exact_size_bytes": "14113",
      "upload_date": "2026-04-04T00:02:28.605463"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescavamd-igb9i04u4wac",
    "display_name": "grapes/Cava.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Cava.md",
      "exact_size_bytes": "12707",
      "upload_date": "2026-04-04T00:02:29.510660"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescastelaomd-1cyhn8pe3efa",
    "display_name": "grapes/Castelao.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Castelao.md",
      "exact_size_bytes": "12318",
      "upload_date": "2026-04-04T00:02:29.473769"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescarmeneremd-zr7svfpu2690",
    "display_name": "grapes/Carmenere.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Carmenere.md",
      "exact_size_bytes": "12003",
      "upload_date": "2026-04-04T00:02:29.416746"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapeschampagnemd-zrye0infeq14",
    "display_name": "grapes/Champagne.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Champagne.md",
      "exact_size_bytes": "15527",
      "upload_date": "2026-04-04T00:02:29.510866"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapeschardonnaymd-qkzw7exgi6gv",
    "display_name": "grapes/Chardonnay.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Chardonnay.md",
      "exact_size_bytes": "14965",
      "upload_date": "2026-04-04T00:02:29.893445"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapeschenin-blancmd-xe39ayurwoq8",
    "display_name": "grapes/Chenin Blanc.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Chenin Blanc.md",
      "exact_size_bytes": "12273",
      "upload_date": "2026-04-04T00:02:30.263638"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescolombardmd-mj179sw4nl70",
    "display_name": "grapes/Colombard.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Colombard.md",
      "exact_size_bytes": "7843",
      "upload_date": "2026-04-04T00:02:30.679106"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescinsaultmd-nu4wbsuoca9s",
    "display_name": "grapes/Cinsault.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Cinsault.md",
      "exact_size_bytes": "13569",
      "upload_date": "2026-04-04T00:02:30.501772"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesconcordmd-fyayvo5120qw",
    "display_name": "grapes/Concord.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Concord.md",
      "exact_size_bytes": "8887",
      "upload_date": "2026-04-04T00:02:30.770722"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescortesemd-3nn3ek8pcy6l",
    "display_name": "grapes/Cortese.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Cortese.md",
      "exact_size_bytes": "9813",
      "upload_date": "2026-04-04T00:02:31.310541"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfalanghinamd-9uv7ra1u3hh6",
    "display_name": "grapes/Falanghina.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Falanghina.md",
      "exact_size_bytes": "9920",
      "upload_date": "2026-04-04T00:02:31.529425"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescremantmd-esow461loikw",
    "display_name": "grapes/Cremant.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Cremant.md",
      "exact_size_bytes": "14276",
      "upload_date": "2026-04-04T00:02:31.357320"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfernao-piresmd-bswl7yvuxej6",
    "display_name": "grapes/Fernão Pires.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Fernão Pires.md",
      "exact_size_bytes": "9908",
      "upload_date": "2026-04-04T00:02:31.530274"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfianomd-usqnvjufr5br",
    "display_name": "grapes/Fiano.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Fiano.md",
      "exact_size_bytes": "12293",
      "upload_date": "2026-04-04T00:02:32.176062"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfranciacortamd-1r0v8var9z82",
    "display_name": "grapes/Franciacorta.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Franciacorta.md",
      "exact_size_bytes": "14651",
      "upload_date": "2026-04-04T00:02:32.280123"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfriulanomd-cx41rfjtc7if",
    "display_name": "grapes/Friulano.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Friulano.md",
      "exact_size_bytes": "14825",
      "upload_date": "2026-04-04T00:02:32.894225"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfurmintmd-ds7du2guy4rn",
    "display_name": "grapes/Furmint.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Furmint.md",
      "exact_size_bytes": "14087",
      "upload_date": "2026-04-04T00:02:32.894354"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfrappatomd-5aj7df5yamd3",
    "display_name": "grapes/Frappato.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Frappato.md",
      "exact_size_bytes": "14378",
      "upload_date": "2026-04-04T00:02:32.851700"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgsm-blend-md-247u3qtqb2mk",
    "display_name": "grapes/GSM Blend .md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/GSM Blend .md",
      "exact_size_bytes": "9501",
      "upload_date": "2026-04-04T00:02:33.516583"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgarganegamd-v1d2ypyheiee",
    "display_name": "grapes/Garganega.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Garganega.md",
      "exact_size_bytes": "9778",
      "upload_date": "2026-04-04T00:02:33.793454"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgamaymd-pn2ns986gdvf",
    "display_name": "grapes/Gamay.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Gamay.md",
      "exact_size_bytes": "10728",
      "upload_date": "2026-04-04T00:02:33.615668"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgarnacha-blancamd-ylmlcyuwohbt",
    "display_name": "grapes/Garnacha Blanca.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Garnacha Blanca.md",
      "exact_size_bytes": "8670",
      "upload_date": "2026-04-04T00:02:34.206762"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgewurztraminermd-2ecujdupjqag",
    "display_name": "grapes/Gewürztraminer.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Gewürztraminer.md",
      "exact_size_bytes": "8432",
      "upload_date": "2026-04-04T00:02:34.308979"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgrenachemd-rj7brgh8hkf1",
    "display_name": "grapes/Grenache.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Grenache.md",
      "exact_size_bytes": "11981",
      "upload_date": "2026-04-04T00:02:34.919568"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgrechettomd-3e30qrz9sxiv",
    "display_name": "grapes/Grechetto.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Grechetto.md",
      "exact_size_bytes": "8393",
      "upload_date": "2026-04-04T00:02:34.488974"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgruner-veltlinermd-1des890iy752",
    "display_name": "grapes/Grüner Veltliner.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Grüner Veltliner.md",
      "exact_size_bytes": "10649",
      "upload_date": "2026-04-04T00:02:35.116781"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesice-winemd-4x3jltfceo9o",
    "display_name": "grapes/Ice Wine.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Ice Wine.md",
      "exact_size_bytes": "11962",
      "upload_date": "2026-04-04T00:02:35.337381"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapeslambruscomd-wa6pycdm1hjj",
    "display_name": "grapes/Lambrusco.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Lambrusco.md",
      "exact_size_bytes": "12079",
      "upload_date": "2026-04-04T00:02:35.544794"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmarsalamd-p0az23wpkqhq",
    "display_name": "grapes/Marsala.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Marsala.md",
      "exact_size_bytes": "10091",
      "upload_date": "2026-04-04T00:02:36.254920"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmalbecmd-z9ix17wa1035",
    "display_name": "grapes/Malbec.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Malbec.md",
      "exact_size_bytes": "11791",
      "upload_date": "2026-04-04T00:02:36.197142"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmarsannemd-9z59yj1o9jsv",
    "display_name": "grapes/Marsanne.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Marsanne.md",
      "exact_size_bytes": "7980",
      "upload_date": "2026-04-04T00:02:36.303766"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmadeiramd-gbdsjgiyjx4c",
    "display_name": "grapes/Madeira.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Madeira.md",
      "exact_size_bytes": "17127",
      "upload_date": "2026-04-04T00:02:36.197075"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmenciamd-ji5k4fnyck23",
    "display_name": "grapes/Mencía.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Mencía.md",
      "exact_size_bytes": "7962",
      "upload_date": "2026-04-04T00:02:36.950256"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmelonmd-yw3gixyfcqcq",
    "display_name": "grapes/Melon.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Melon.md",
      "exact_size_bytes": "15576",
      "upload_date": "2026-04-04T00:02:36.909740"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmerlotmd-0vyniiql44hk",
    "display_name": "grapes/Merlot.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Merlot.md",
      "exact_size_bytes": "11801",
      "upload_date": "2026-04-04T00:02:36.951781"
    }
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmonastrellmd-rnqphk9s3hy6",
    "display_name": "grapes/Monastrell.md",
    "metadata": {
      "bucket_name": "que-vino-23032025-databases",
      "original_filename": "grapes/Monastrell.md",
      "exact_size_bytes": "8995",
      "upload_date": "2026-04-04T00:02:37.442994"
    }
  }
]
```

---

## ✅ PASS — POST /knowledge-stores/sync — Sincronizar 'grapes' (Bucket Resolver)

**Request:**
```
POST https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/knowledge-stores/sync
{
  "bucket_name": "grapes",
  "store_name": "grapes"
}
```

**Response:** HTTP `200` (esperado: `200`)
```json
{
  "status": "completed",
  "transaction_id": "a32e4858-a8a4-41ce-85de-30eb278e3307",
  "summary": {
    "uploaded": 2,
    "skipped": 95,
    "deleted": 0,
    "errors": 0
  }
}
```

---

## ✅ PASS — GET /knowledge-stores — Sin token (esperado: 401)

**Request:**
```
GET https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/knowledge-stores
```

**Response:** HTTP `401` (esperado: `401`)
```json
{
  "error_code": "UNAUTHORIZED",
  "message": "Authorization header missing",
  "detail": "Add Bearer token"
}
```

---

## ✅ PASS — GET /knowledge-stores — Token inválido (esperado: 401)

**Request:**
```
GET https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/knowledge-stores
```

**Response:** HTTP `401` (esperado: `401`)
```json
{
  "error_code": "INVALID_TOKEN",
  "message": "Token authentication failed",
  "detail": "Invalid base64-encoded string: number of data characters (5) cannot be 1 more than a multiple of 4"
}
```

---
