---
id: lote
tipo: lote
titulo: "Plantilla de lote"
estado: activo
tags: [lote, plantilla]
creado: 2026-07-08
actualizado: 2026-07-08
producto: "<tipo de producto>"
responsable: "<responsable>"
fecha_embutido: YYYY-MM-DD
fecha_liberacion: YYYY-MM-DD
mediciones:
  nitrito_ppm: 0
  ph_final: 0
  merma_pct: 0
  grados_hora: 0
---

# Plantilla de lote

Plantilla anonimizada para crear una nota de lote nueva. Los lotes reales viven
**fuera del repo publico** (ver README y `.gitignore`); esta plantilla solo
documenta la estructura y los campos que audita `scripts/validate.py` contra
los umbrales de [[barreras-control]].

## Ficha

| Campo | Valor | Umbral | Estado |
|---|---|---|---|
| Nitrito ingoing | `<ppm>` | ≤ 80 ppm | — |
| pH final | `<pH>` | ≤ 5.3 | — |
| Merma | `<%>` | ≥ 30 % | — |
| Grados-hora | `<°C·h>` | ≤ 370 °C·h | — |

## Trazabilidad

- Proceso seguido: [[Procedimiento-embutido]].
- Marco normativo del nitrito: [[normativa-eu-2023-2108]].
- Datos crudos y fórmulas: `tracker/registro-lotes.xlsx`, hoja `Lotes`.

## Incidencias

Registrar aquí anomalías del proceso (fermentación fuera de presupuesto de
grados-hora, [[case-hardening]], [[moho-indeseado]], etc.). Si no hubo,
poner "Ninguna".

## Cómo usar esta plantilla

1. Copiar este archivo a la carpeta local privada de lotes (por defecto
   `vault/lotes/lote-NN.md`, ignorada por git).
2. Cambiar `id` al nombre del archivo (`lote-NN`) y actualizar fechas,
   producto y responsable.
3. Al cierre, completar `mediciones` con los valores reales.
4. Correr `python scripts/validate.py` — debe pasar los cuatro umbrales.
