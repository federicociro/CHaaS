---
id: barreras-control
tipo: tecnica
titulo: "Tecnología de barreras (hurdle) para embutido curado-fermentado"
estado: activo
tags: [tecnica, seguridad, barreras, hurdle]
creado: 2026-07-02
actualizado: 2026-07-02
---

# Tecnología de barreras (hurdle technology)

La inocuidad del embutido crudo-curado no depende de una sola barrera sino del
**efecto combinado** de varias sub-letales. Ninguna alcanza por sí sola para
estabilizar el producto; juntas hacen inviable el crecimiento de patógenos y la
producción de toxina.

## Las barreras y sus umbrales

| Barrera | Umbral operativo | Controla |
|---|---|---|
| Nitrito de sodio (E250) | ≤ **80 ppm** ingoing | *C. botulinum*, color, oxidación |
| Acidificación | pH final ≤ **5.3** | *S. aureus*, enterobacterias |
| Grados-hora fermentación | ≤ **370 °C·h** hasta pH 5.3 (base 15.5 °C) | toxina estafilocócica |
| Deshidratación (merma) | ≥ **30 %** de peso | a_w → estabilidad microbiológica |

Los umbrales viven en esta nota y en la ficha de cada lote (bloque
`mediciones`); el CI valida forma (frontmatter, wikilinks), no números.

### Por qué estos números

- **80 ppm de nitrito** es el máximo *ingoing* para embutidos curados no tratados
  por calor según [[normativa-eu-2023-2108]] (bajó desde 150 ppm). Suficiente para
  el efecto antibotulínico sin excederse en nitrosaminas.
- **pH 5.3** es el techo por debajo del cual *Staphylococcus aureus* no produce
  enterotoxina en condiciones de fermentación. Es el objetivo de la fase de
  fermentación descrita en [[Procedimiento-embutido]].
- **370 grados-hora (°C·h)** es la traducción métrica del límite del AMI
  (American Meat Institute) — originalmente 665 °F·h con base 60 °F — para la
  fase de fermentación cuando la temperatura máxima se mantiene por debajo de
  32.2 °C. Se define como `Σ (T_°C − 15.5) × h` hasta alcanzar pH 5.3.
  Superarlo permite crecimiento de *S. aureus* aunque el pH final sea correcto.
- **30 % de merma** es el mínimo de pérdida de peso que lleva la a_w a la zona
  estable (< 0.90) para un salame de calibre medio.

## Secuencia temporal de barreras

1. **Embutido / t=0**: nitrito + sal + cultivo iniciador. Barrera química arranca.
2. **Fermentación (24–72 h)**: el cultivo baja el pH. Acumular ≤ 370 °C·h hasta
   cruzar pH 5.3. Ver [[fermentacion-fallida]] si no acidifica.
3. **Secado (semanas)**: merma progresiva → cae la a_w. Riesgo de
   [[case-hardening]] si el gradiente de humedad es muy agresivo.
4. **Maduración**: flora de superficie deseada; controlar [[moho-indeseado]].

Registro de datos por lote: ver [[lote]] como plantilla y `tracker/registro-lotes.xlsx`.

## Barrera transversal: higiene

La higiene y desinfección funcionan como **PPC transversal** — no aparecen en
la tabla de umbrales del lote pero condicionan a todas las demás. Ver
[[higiene-desinfeccion]] para producto, dilución, tiempo de contacto y
frecuencia por superficie/equipo.
