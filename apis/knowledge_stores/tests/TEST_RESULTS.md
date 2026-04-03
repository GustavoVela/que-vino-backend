# Test Results — quevino-knowledge-stores

**Entorno:** Producción (Cloud Run)  
**URL Base:** `https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app`  
**Fecha:** 2026-04-02 18:47:40  
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
    "id": "fileSearchStores/grapesv2-g6u5ywotqjyc",
    "display_name": "grapes_v2"
  },
  {
    "id": "fileSearchStores/regions-lgpvlubvqt3g",
    "display_name": "regions"
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
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesagiorgitikomd-0mqjwl3rgv34",
    "display_name": "grapes/Agiorgitiko.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesalbarinomd-2u9bh459g4yt",
    "display_name": "grapes/Albariño.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesalicante-bouschetmd-q7x7agy52r4o",
    "display_name": "grapes/Alicante Bouschet.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesarintomd-8tg3l15syt6a",
    "display_name": "grapes/Arinto.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesassyrtikomd-gbubs1u3no3m",
    "display_name": "grapes/Assyrtiko.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesbagamd-64dlnx84rxn2",
    "display_name": "grapes/Baga.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesbarberamd-57wi44m28qo8",
    "display_name": "grapes/Barbera.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesblaufrankischmd-ve58a20fqvob",
    "display_name": "grapes/Blaufränkisch.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesbobalmd-xiysdnu93bwn",
    "display_name": "grapes/Bobal.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesbonarda-argentinamd-dij0g33g9ne9",
    "display_name": "grapes/Bonarda Argentina.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesbrachettomd-kjioh12tsqlu",
    "display_name": "grapes/Brachetto.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesbordeaux-blend-redmd-asv3n74o9b5k",
    "display_name": "grapes/Bordeaux Blend (Red).md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescastelaomd-twkvuxgu2i6s",
    "display_name": "grapes/Castelao.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescabernet-francmd-gnuokaxv1i9n",
    "display_name": "grapes/Cabernet Franc.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescarignanmd-ehjurhdj2lki",
    "display_name": "grapes/Carignan.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapeschampagnemd-4nlbqg8arh2y",
    "display_name": "grapes/Champagne.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescarmeneremd-sywxusvgsr71",
    "display_name": "grapes/Carmenere.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescabernet-sauvignonmd-ycdm73g87g84",
    "display_name": "grapes/Cabernet Sauvignon.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescavamd-uwqpct0dm7nr",
    "display_name": "grapes/Cava.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapeschenin-blancmd-squgav61y3mx",
    "display_name": "grapes/Chenin Blanc.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapeschardonnaymd-7zdda9q2ibn9",
    "display_name": "grapes/Chardonnay.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescolombardmd-wis55ksh4vfr",
    "display_name": "grapes/Colombard.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescinsaultmd-ksz62nft0yb2",
    "display_name": "grapes/Cinsault.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesconcordmd-hwbhejyhdlcw",
    "display_name": "grapes/Concord.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescortesemd-vvgx0pxgw002",
    "display_name": "grapes/Cortese.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescremantmd-udpdt1cbaymz",
    "display_name": "grapes/Cremant.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfalanghinamd-soz29qe40gvm",
    "display_name": "grapes/Falanghina.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfernao-piresmd-7nefta4d4qkl",
    "display_name": "grapes/Fernão Pires.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfianomd-0qt37cp3yprl",
    "display_name": "grapes/Fiano.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfranciacortamd-7p4m4fo5h74r",
    "display_name": "grapes/Franciacorta.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfrappatomd-2bx8a7yf6ci2",
    "display_name": "grapes/Frappato.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfriulanomd-gkbdaz1ao4l1",
    "display_name": "grapes/Friulano.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesfurmintmd-h6h7ng9dgv0e",
    "display_name": "grapes/Furmint.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgsm-blend-md-b96zmi628vo6",
    "display_name": "grapes/GSM Blend .md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgamaymd-0g1a7fs0ipfr",
    "display_name": "grapes/Gamay.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgarganegamd-bxz2crffdqop",
    "display_name": "grapes/Garganega.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgarnacha-blancamd-03op3no3rg4y",
    "display_name": "grapes/Garnacha Blanca.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgrechettomd-d2adsp4yboy3",
    "display_name": "grapes/Grechetto.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgewurztraminermd-kc3y38ych5kf",
    "display_name": "grapes/Gewürztraminer.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgruner-veltlinermd-wz186bgaoelk",
    "display_name": "grapes/Grüner Veltliner.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesgrenachemd-a1joyl5h4lwe",
    "display_name": "grapes/Grenache.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesice-winemd-hkspmh7c9yzf",
    "display_name": "grapes/Ice Wine.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapeslambruscomd-3d6cumcdxij5",
    "display_name": "grapes/Lambrusco.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmadeiramd-jcd1s629ghjb",
    "display_name": "grapes/Madeira.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmalbecmd-4u64iyw30n4w",
    "display_name": "grapes/Malbec.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmarsalamd-k5k9l8q4pan0",
    "display_name": "grapes/Marsala.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmarsannemd-tjsean3w0q62",
    "display_name": "grapes/Marsanne.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmelonmd-39vtq6nmbypu",
    "display_name": "grapes/Melon.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmenciamd-9jm8t7eo812o",
    "display_name": "grapes/Mencía.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmerlotmd-b3ntzwbz9ewc",
    "display_name": "grapes/Merlot.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmonastrellmd-cyice83nru9t",
    "display_name": "grapes/Monastrell.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmontepulcianomd-lsswclge5x2y",
    "display_name": "grapes/Montepulciano.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmoscatel-de-setubalmd-nsewgtq8w2al",
    "display_name": "grapes/Moscatel de Setúbal.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmoschofileromd-x0nwnjfo3kpb",
    "display_name": "grapes/Moschofilero.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmuscat-blancmd-51yxxwvqj08o",
    "display_name": "grapes/Muscat Blanc.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesmuscat-de-alexandriam-aryaiai29gdy",
    "display_name": "grapes/Muscat de Alexandria.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesnebbiolomd-n2u3k9o6507y",
    "display_name": "grapes/Nebbiolo.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesnegroamaromd-qax5gxa97afs",
    "display_name": "grapes/Negroamaro.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesnerello-mascalesemd-11qsd6flnpqg",
    "display_name": "grapes/Nerello Mascalese.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesnero-davolamd-9w884vj9925w",
    "display_name": "grapes/Nero d'Avola.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespetit-verdotmd-fnmctl1tghv0",
    "display_name": "grapes/Petit Verdot.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespetite-sirahmd-neic5m69kvll",
    "display_name": "grapes/Petite Sirah.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespicpoulmd-kdlrl1u8mky0",
    "display_name": "grapes/Picpoul.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespinot-blancmd-p99v80zju1sj",
    "display_name": "grapes/Pinot Blanc.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespinot-grismd-wjuavfckaluv",
    "display_name": "grapes/Pinot Gris.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespinot-noirmd-wrh1zegnnjx8",
    "display_name": "grapes/Pinot Noir.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapespinotagemd-pest5w2obith",
    "display_name": "grapes/Pinotage.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesportomd-n8j400anmf6q",
    "display_name": "grapes/Porto.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesproseccomd-xzhvbjfltleo",
    "display_name": "grapes/Prosecco.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesrieslingmd-su71ay8z9s2l",
    "display_name": "grapes/Riesling.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesroussannemd-gx1x4cb6kaid",
    "display_name": "grapes/Roussanne.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessagrantinomd-bkudvsct0vsr",
    "display_name": "grapes/Sagrantino.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessangiovesemd-w56izn9wh3ax",
    "display_name": "grapes/Sangiovese.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessauternesmd-kgy9v6lpkcri",
    "display_name": "grapes/Sauternes.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessavatianomd-upq7b03ezt9u",
    "display_name": "grapes/Savatiano.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessauvignon-blancmd-54b17ae3o0v6",
    "display_name": "grapes/Sauvignon Blanc.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesschiavamd-6l35jas2q0pe",
    "display_name": "grapes/Schiava.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessemillonmd-ob4a304f0l7g",
    "display_name": "grapes/Sémillon.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessherrymd-em6onh7tldss",
    "display_name": "grapes/Sherry.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessilvanermd-s50pxc9hdunw",
    "display_name": "grapes/Silvaner.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapessyrahmd-ndu7zezu35h0",
    "display_name": "grapes/Syrah.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapestannatmd-hrr73xrflkl9",
    "display_name": "grapes/Tannat.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapestempranillomd-zn3ra8h4ebiv",
    "display_name": "grapes/Tempranillo.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapestouriga-nacionalmd-oz1okd43cja5",
    "display_name": "grapes/Touriga Nacional.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapestrebbiano-toscanomd-zebtwtfdom7b",
    "display_name": "grapes/Trebbiano Toscano.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapestorrontesmd-8t43xl1fyype",
    "display_name": "grapes/Torrontés.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesvalpolicella-blendmd-b2womr439ibp",
    "display_name": "grapes/Valpolicella Blend.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesverdejomd-1y65o0f7dyc6",
    "display_name": "grapes/Verdejo.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesverdicchiomd-db1t6rjatti2",
    "display_name": "grapes/Verdicchio.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesvermentinomd-91qh85z7ohh2",
    "display_name": "grapes/Vermentino.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesvin-santomd-h9pw3gnbu2vo",
    "display_name": "grapes/Vin Santo.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesvinho-verdemd-19n2en4buo8p",
    "display_name": "grapes/Vinho Verde.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesviogniermd-qlmi35fil03x",
    "display_name": "grapes/Viognier.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesviuramd-haz3uuia10zp",
    "display_name": "grapes/Viura.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapesxinomavromd-zcwyi36f3d7y",
    "display_name": "grapes/Xinomavro.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapeszinfandelmd-26dpwpd19g4b",
    "display_name": "grapes/Zinfandel.md",
    "metadata": {}
  },
  {
    "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapeszweigeltmd-c9msvqu0i6pj",
    "display_name": "grapes/Zweigelt.md",
    "metadata": {}
  }
]
```

---

## ✅ PASS — POST /knowledge-stores/sync — Sincronizar bucket (bucket vacío)

**Request:**
```
POST https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/knowledge-stores/sync
{
  "bucket_name": "que-vino-23032025-audios",
  "prefix": "test-integration/",
  "store_name": "test-integration-store"
}
```

**Response:** HTTP `200` (esperado: `200`)
```json
{
  "status": "completed",
  "transaction_id": "a7e22719-6f7d-49cc-b437-9cb8919210ee",
  "summary": {
    "uploaded": 0,
    "skipped": 0,
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
