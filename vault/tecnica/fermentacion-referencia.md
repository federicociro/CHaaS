---
id: fermentacion-referencia
tipo: tecnica
titulo: "Fermentación acelerada — nota de referencia (no en uso)"
estado: activo
tags: [tecnica, fermentacion, referencia]
creado: 2026-07-09
actualizado: 2026-07-09
---

# Fermentación acelerada — nota de referencia

> **Nota**: el flujo actual del taller es **curado largo sin fermentación
> acelerada** (ver [[Procedimiento-embutido]]). Esta nota queda como material
> de referencia para el día que se introduzca cultivo iniciador y fase de
> estufado; no es un paso del proceso vigente.

Marco general para una fase de fermentación con cultivo iniciador:

- **Objetivo**: bajar el pH a **≤ 5,3** acumulando **≤ 370 grados-hora
  (°C·h)** con base 15,5 °C. Umbral tomado de la AMI para evitar producción de
  toxina estafilocócica.
- **Cámara** 22–24 °C, HR 90–92 %, temperatura máxima **< 32,2 °C**.
- **Medición de pH** a las 0 / 24 / 48 h. Si no hay pHmetro, ver
  [[phmetro-plan-de-compra]].
- **Cálculo de grados-hora**: `Σ (T_°C − 15,5) × h`. Cruzar pH 5,3 **antes**
  de agotar el presupuesto de 370 °C·h.

## Cultivo iniciador

Bacterias lácticas (acidificación) + estafilococos de cura (color y aroma),
rehidratados según ficha del proveedor. Sin cultivo activo → fermentación
poco predecible.

## Runbook (histórico) — fermentación fallida

Cuando exista fase de fermentación, este es el árbol de decisión que se
aplicaría si a las 48 h el pH sigue > 5,3 o se consumen los 370 °C·h sin
cruzar el objetivo. Es un problema de **seguridad**: sin acidificación a
tiempo, *S. aureus* puede producir enterotoxina termoestable.

### Causas frecuentes

- Cultivo iniciador inactivo (mal rehidratado, vencido, muerto por calor).
- Falta de azúcar fermentable (sin sustrato no baja el pH).
- Temperatura demasiado baja → cinética lenta, se agotan los grados-hora.
- Exceso de sal o nitrito inhibiendo el cultivo.

### Decisión

1. Verificar el presupuesto de grados-hora (`Σ (T_°C − 15,5) × h`):
   - Si ≤ 370 °C·h y el pH aún baja → dar más tiempo, vigilar de cerca.
   - Si > 370 °C·h sin llegar a pH 5,3 → **descartar el lote**. No se rescata.
2. Confirmar medición: si el pHmetro no está disponible o hay dudas del
   valor, ver [[phmetro-plan-de-compra]].

### Acción correctiva (próximo lote)

- Cultivo fresco y bien rehidratado; validar actividad.
- Asegurar azúcar fermentable (dextrosa) en la formulación.
- Ajustar temperatura de cámara al rango del cultivo (22–24 °C).
- Revisar dosis de sal/nitrito (≤ 80 ppm) — ver [[normativa-eu-2023-2108]].

### Registro

Anotar el lote fallido con `estado: archivado` y `ph_final` real.
`validate.py` lo marcará fuera de umbral, dejando traza de por qué no se
liberó.

## Umbrales relacionados

Ver [[barreras-control]] para el mapa completo de barreras (nitrito, pH,
merma, grados-hora) y [[normativa-eu-2023-2108]] para el marco legal del
nitrito.
