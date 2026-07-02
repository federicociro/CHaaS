---
id: case-hardening
tipo: runbook
titulo: "Runbook — case hardening (corteza endurecida)"
estado: activo
tags: [runbook, secado, defecto, case-hardening]
creado: 2026-07-02
actualizado: 2026-07-02
---

# Runbook — Case hardening

**Síntoma**: corteza externa seca y dura mientras el centro sigue húmedo/blando.
La costra sella la pieza e impide que salga la humedad interior → riesgo de
putrefacción central y a_w interna fuera de umbral.

## Causa

Gradiente de secado demasiado agresivo: HR muy baja y/o velocidad de aire alta
respecto a la difusión de agua desde el centro. La superficie pierde agua más
rápido de lo que el interior la repone.

## Diagnóstico

- Cortar una pieza: anillo externo endurecido + centro húmedo (halo).
- Merma total parece avanzar pero se **estanca** (la costra frena la evaporación).
- La merma (`merma_pct`) medida en balanza no refleja el secado real del núcleo.

## Acción

1. **Subir HR** de la cámara a 85–90 % y **bajar velocidad de aire**.
2. Alternar ciclos húmedo/seco para reequilibrar el gradiente.
3. En casos leves, envolver las piezas unos días para homogeneizar humedad.
4. No forzar temperatura para "recuperar" — agrava el sellado.

## Prevención

- Descenso gradual de HR en el [[Procedimiento-embutido]] (paso 4), no salto brusco.
- Calibre uniforme y embutido sin bolsas de aire.
- Registrar curva de merma en `tracker/registro-lotes.xlsx`: un estancamiento
  temprano es la señal de alarma.

Relacionado: [[barreras-control]] · [[moho-indeseado]]
