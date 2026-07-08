# CHaaS — Chorizos as a Service

> Sí, parece un repo de código. En realidad es de **chorizos**.
> CHaaS = *Chorizos as a Service*: un vault de conocimiento para
> **embutido crudo-curado-fermentado** con la disciplina de un repo de software
> (frontmatter, CI, runbooks, versionado).

## About

Notas, procedimientos y runbooks para producir salame / chorizo seco de forma
reproducible y segura. Cada lote se documenta como una nota Markdown con
metadata YAML; el CI valida que el vault esté bien formado antes de publicarlo.

El contenido es Markdown estilo Obsidian (frontmatter + `[[wikilinks]]`),
pensado para uso **local con Obsidian**. Compatible con cualquier publicador
que entienda el formato Obsidian (Quartz, Obsidian Publish, etc.) si en el
futuro se desea publicar.

## Barreras de inocuidad (referencia)

Los umbrales que hay que respetar en cada lote, documentados en
[`vault/tecnica/barreras-control.md`](vault/tecnica/barreras-control.md):

| Barrera | Umbral | Controla |
|---|---|---|
| Nitrito de sodio (ingoing) | ≤ **80 ppm** | *C. botulinum* — [Reg. UE 2023/2108](vault/normativa/normativa-eu-2023-2108.md) |
| pH final de fermentación | ≤ **5.3** | *S. aureus* / enterobacterias |
| Merma (pérdida de peso) | ≥ **30 %** | a_w → estabilidad microbiológica |
| Grados-hora hasta pH 5.3 | ≤ **370 °C·h** (base 15.5 °C) | toxina estafilocócica (AMI) |

## Estructura

```text
chaas/
├── README.md
├── requirements.txt              # PyYAML
├── .gitignore
├── .markdownlint-cli2.jsonc
├── scripts/
│   └── validate.py               # frontmatter + wikilinks
├── .github/workflows/
│   └── ci.yml                    # validate + markdownlint; lychee semanal
├── tracker/
│   └── registro-lotes.xlsx       # 4 hojas: Lotes, Umbrales, Merma, Dashboard
└── vault/
    ├── plantillas/lote.md         # plantilla anonimizada (bloque `mediciones`)
    ├── tecnica/barreras-control.md
    ├── procedimientos/Procedimiento-embutido.md
    ├── runbooks/                 # case-hardening, moho-indeseado, fermentacion-fallida
    ├── normativa/normativa-eu-2023-2108.md
    └── referencia/phmetro-plan-de-compra.md
```

> Los **lotes reales** (`vault/lotes/`) NO viven en este repo: contienen datos
> privados del taller (pesos, mediciones, fechas). Están ignorados por git —
> ver `.gitignore`. Para crear uno, copiar `vault/plantillas/lote.md` a
> `vault/lotes/lote-NN.md` en tu bóveda local.

## Convención de notas

Cada `.md` del vault lleva frontmatter YAML:

```yaml
---
id: <igual al nombre de archivo, sin extensión>
tipo: lote | tecnica | procedimiento | runbook | normativa | referencia
titulo: "..."
estado: borrador | activo | archivado
tags: [..]
creado: YYYY-MM-DD
actualizado: YYYY-MM-DD
---
```

Las notas de **lote** agregan el bloque con las mediciones del proceso:

```yaml
mediciones:
  nitrito_ppm: 78
  ph_final: 5.1
  merma_pct: 34
  grados_hora: 640
```

Los enlaces entre notas usan `[[nombre-de-archivo]]` (sin extensión), con
`[[destino|alias]]` y `[[destino#seccion]]` soportados.

## Uso

1. **Abrir el vault en Obsidian**: apuntar Obsidian a la carpeta `vault/` como
   bóveda. El flujo diario (leer, editar notas, seguir wikilinks) ocurre ahí.
2. **Validar y lintear** antes de commitear:

```bash
# Entorno
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Validar el vault (frontmatter + wikilinks)
python scripts/validate.py

# Lint de Markdown
npx markdownlint-cli2
```

`validate.py` sale con código ≠ 0 si falta frontmatter o hay un wikilink roto —
eso es lo que corta el merge en CI. Los umbrales de inocuidad se auditan a ojo
sobre la planilla de lotes; el repo los documenta, no los policía.

## Runbooks

Guías de acción para defectos frecuentes de proceso:

- [Case hardening](vault/runbooks/case-hardening.md) — corteza sellada, centro húmedo.
- [Moho indeseado](vault/runbooks/moho-indeseado.md) — flora de superficie no deseada.
- [Fermentación fallida](vault/runbooks/fermentacion-fallida.md) — no cruza pH 5.3 (seguridad).
