---
id: curado-directo
tipo: tecnica
titulo: "Curado directo (sin fermentación) — barreras y umbrales"
estado: activo
tags: [tecnica, seguridad, barreras, curado, sin-fermentacion]
creado: 2026-07-03
actualizado: 2026-07-03
---

# Curado directo (sin fermentación)

Producto crudo-curado **sin cultivo iniciador ni fase de fermentación**: chorizo
y longaniza al estilo mediterráneo curados en seco lento. A diferencia del
crudo-curado-fermentado de [[Procedimiento-embutido]], **no hay caída rápida de
pH** — la pieza queda en pH ~5.6–6.0. Eso elimina una de las barreras de
[[barreras-control]], y hay que compensarla con las demás.

## Qué barrera se pierde y cómo se compensa

Sin acidificación desaparece el freno temprano a *S. aureus* y enterobacterias
mientras la a_w todavía es alta. La estabilidad se sostiene entonces en:

| Barrera | Umbral (curado-directo) | Rol reforzado |
|---|---|---|
| Nitrito ingoing | ≤ **80 ppm** | igual; anti-*C. botulinum* — [[normativa-eu-2023-2108]] |
| Sal | **≥ 2,8 %** | barrera química desde t=0, no hay pH que ayude |
| Merma | ≥ **35 %** | +5 pts vs. fermentado: baja más la a_w para cubrir el pH ausente |
| Temp. máx. de secado | ≤ **15 °C** | frena crecimiento mientras la a_w cae; reemplaza el rol de los grados-hora |
| a_w (si se mide) | ≤ **0.90** | objetivo final de estabilidad |

Estos son los checks que `scripts/validate.py` aplica cuando el lote lleva
`proceso: curado-directo`. **No** se exige `ph_final` ni `grados_hora`: pedirlos
no tendría sentido en un producto que no fermenta.

## Regla de oro: frío desde t=0

No hay estufado cálido. Nada de cámara a 22–24 °C (eso es fase fermentativa y sin
cultivo que acidifique favorece flora indeseada). Se va **directo a secadero a
12–14 °C, HR 78–82 %**, con descenso suave para evitar [[case-hardening]].

## Formulación de referencia (chorizo, por kg de masa)

| Ingrediente | g/kg | Nota |
|---|---|---|
| Carne + grasa | 1000 | cabeza de lomo (bondiola) sola es viable; grasa intramuscular blanda → menos vida útil |
| Sal | 28 | ≥ 2,8 % |
| Sal de cura #2 (6,25 % NaNO₂ + 4 % NaNO₃) | 1,25 | ≈ 78 ppm nitrito ingoing; el nitrato da liberación lenta en curado largo |
| Pimentón dulce | 20 | define el perfil |
| Pimentón picante / ají | 3 | a gusto |
| Pimienta negra | 2 | — |
| Ajo en polvo | 3 | deshidratado, no fresco (agua + flora) |
| Vino seco | 25 | el alcohol evapora |

**Sin dextrosa**: no hay cultivo que la fermente (opcional solo por color/perfil).
Pesar la cura en balanza de precisión — el nitrito no se estima a ojo.

## Proceso

1. Molido frío (≤ 4 °C), grasa definida.
2. Amasar con sal + cura + especias + vino; **reposo 24–48 h en heladera**.
3. Embutir sin bolsas de aire; registrar peso fresco por pieza.
4. Secadero 12–14 °C / HR 78–82 % directo, sin fase cálida.
5. Secar hasta **merma ≥ 35 %**; vigilar [[case-hardening]] y [[moho-indeseado]].
6. Cierre: registrar `nitrito_ppm`, `merma_pct`, `temp_secado_max_c` (y `aw` si se
   mide) en la nota de lote (plantilla [[lote-00]]).

## Advertencia

El curado directo es **menos indulgente** que el fermentado: sin la caída de pH,
la única defensa en la ventana inicial es nitrito + sal + frío. Higiene estricta,
temperatura baja constante y no apurar el secado.
