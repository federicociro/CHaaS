---
id: lote-00
tipo: lote
titulo: "Lote 00 — plantilla / lote de referencia"
estado: activo
tags: [lote, plantilla, referencia]
creado: 2026-07-02
actualizado: 2026-07-02
producto: "Salame tipo Milano"
responsable: "fede"
fecha_embutido: 2026-06-01
fecha_liberacion: 2026-07-01
mediciones:
  nitrito_ppm: 78
  ph_final: 5.1
  merma_pct: 34
  grados_hora: 640
---

# Lote 00 — plantilla

Lote de referencia y **plantilla** para nuevos lotes. Los valores del bloque
`mediciones` en el frontmatter son los que audita `scripts/validate.py` contra
los umbrales de [[barreras-control]].

## Ficha

| Campo | Valor | Umbral | Estado |
|---|---|---|---|
| Nitrito ingoing | 78 ppm | ≤ 80 ppm | OK |
| pH final | 5.1 | ≤ 5.3 | OK |
| Merma | 34 % | ≥ 30 % | OK |
| Grados-hora | 640 °F·h | ≤ 665 °F·h | OK |

## Trazabilidad

- Proceso seguido: [[Procedimiento-embutido]].
- Marco normativo del nitrito: [[normativa-eu-2023-2108]].
- Datos crudos y fórmulas: `tracker/registro-lotes.xlsx`, hoja `Lotes`.

## Incidencias

Ninguna. Fermentación cruzó pH 5.3 a las ~34 h (dentro del presupuesto de
grados-hora). Secado sin [[case-hardening]] ni [[moho-indeseado]].

## Cómo clonar este lote

1. Copiar este archivo a `vault/lotes/lote-NN.md`.
2. Cambiar `id` al nombre del archivo (`lote-NN`) y actualizar fechas.
3. Al cierre, completar `mediciones` con los valores reales.
4. Correr `python scripts/validate.py` — debe pasar los cuatro umbrales.
