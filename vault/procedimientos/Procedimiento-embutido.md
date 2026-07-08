---
id: Procedimiento-embutido
tipo: procedimiento
titulo: "Procedimiento estándar de embutido crudo-curado"
estado: activo
tags: [procedimiento, embutido, fermentacion, secado]
creado: 2026-07-02
actualizado: 2026-07-02
---

# Procedimiento de embutido crudo-curado

SOP base para salame/longaniza fermentada. Apoyado en las barreras descritas en
[[barreras-control]] y en el marco legal de [[normativa-eu-2023-2108]].

## 1. Insumos y preparación

- Carne magra 2–4 °C, grasa firme (dorsal). Todo el equipo desinfectado.
- **Sal de cura**: dosificar nitrito para **≤ 80 ppm ingoing** sobre masa total.
  Pesar en balanza de precisión; el nitrito no se estima "a ojo".
- **Cultivo iniciador** (bacterias lácticas + estafilococos de cura) rehidratado
  según ficha. Sin cultivo activo → riesgo de [[fermentacion-fallida]].
- Molido a temperatura de partido (grasa definida, sin embarrado).

## 2. Amasado y embutido

- Mezclar hasta ligar (pegajosidad de proteína extraída), sin subir de 4 °C.
- Embutir en tripa acondicionada, sin bolsas de aire (favorecen [[moho-indeseado]]
  interno y oxidación).
- Registrar **peso fresco** de cada pieza en `tracker/registro-lotes.xlsx`; es la
  base para calcular la **merma**.

## 3. Fermentación

Objetivo: bajar el pH a **≤ 5.3** acumulando **≤ 370 grados-hora (°C·h)** con
base 15.5 °C.

- Cámara 22–24 °C, HR 90–92 %, temperatura máxima **< 32.2 °C**.
- Medir pH a las 0 / 24 / 48 h. Si no hay pHmetro, ver [[pHmetro-no-disponible]].
- Llevar la cuenta de grados-hora: `Σ (T_°C − 15.5) × h`. Cruzar pH 5.3 **antes**
  de agotar el presupuesto de 370 °C·h.

> Si a las 48 h el pH sigue > 5.3 → activar runbook [[fermentacion-fallida]].

## 4. Secado y maduración

- Bajar a 12–14 °C, HR 78–82 %. Descenso gradual para evitar [[case-hardening]].
- Secar hasta **merma ≥ 30 %** respecto al peso fresco (a_w objetivo < 0.90).
- Inspección de superficie diaria; flora blanca deseable, verde/negra no
  (ver [[moho-indeseado]]).

## 5. Cierre de lote

- Registrar `nitrito_ppm`, `ph_final`, `merma_pct`, `grados_hora` en la nota del
  lote (plantilla: [[lote]]) y en el tracker.
- `scripts/validate.py` verifica que los cuatro valores respeten los umbrales
  antes de dar el lote por liberado.
