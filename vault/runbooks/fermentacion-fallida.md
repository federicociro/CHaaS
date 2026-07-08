---
id: fermentacion-fallida
tipo: runbook
titulo: "Runbook — fermentación fallida (no acidifica)"
estado: activo
tags: [runbook, fermentacion, seguridad, defecto]
creado: 2026-07-02
actualizado: 2026-07-02
---

# Runbook — Fermentación fallida

**Síntoma**: a las 48 h el pH sigue **> 5.3** y/o se consumieron los **665
grados-hora** sin cruzar el objetivo. Es un problema de **seguridad**, no
cosmético: sin acidificación a tiempo, *S. aureus* puede producir enterotoxina
termoestable.

## Causas frecuentes

- Cultivo iniciador inactivo (mal rehidratado, vencido, muerto por calor).
- Falta de azúcar fermentable (sin sustrato no baja el pH).
- Temperatura demasiado baja → cinética lenta, se agotan los grados-hora.
- Exceso de sal o nitrito inhibiendo el cultivo.

## Decisión

1. **Verificar el presupuesto de grados-hora** (`Σ (T_°C − 15.5) × h`):
   - Si **≤ 370 °C·h** y el pH aún baja → dar más tiempo, vigilar de cerca.
   - Si **> 370 °C·h** sin llegar a pH 5.3 → **descartar el lote**. No se rescata.
2. Confirmar medición: si el pHmetro no está disponible o dudás del valor, ver
   [[pHmetro-no-disponible]] para métodos alternativos antes de decidir.

## Acción correctiva (para el próximo lote)

- Cultivo fresco y bien rehidratado; validar actividad.
- Asegurar azúcar fermentable (dextrosa) en la formulación.
- Ajustar temperatura de cámara al rango del cultivo (22–24 °C).
- Revisar dosis de sal/nitrito (≤ 80 ppm) — ver [[normativa-eu-2023-2108]].

## Registro

Anotar el lote fallido con `estado: archivado` y `ph_final` real. `validate.py`
lo marcará fuera de umbral, dejando traza de por qué no se liberó.

Relacionado: [[Procedimiento-embutido]] · [[barreras-control]] · [[lote]]
