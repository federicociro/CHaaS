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

| Barrera | Umbral operativo | Controla | Constante en `validate.py` |
|---|---|---|---|
| Nitrito de sodio (E250) | ≤ **80 ppm** ingoing | *C. botulinum*, color, oxidación | `LIMITE_NITRITO_PPM` |
| Acidificación | pH final ≤ **5.3** | *S. aureus*, enterobacterias | `LIMITE_PH` |
| Grados-hora fermentación | ≤ **665 °F·h** hasta pH 5.3 | toxina estafilocócica | `LIMITE_GRADOS_HORA` |
| Deshidratación (merma) | ≥ **30 %** de peso | a_w → estabilidad microbiológica | `LIMITE_MERMA_PCT` |

Los cuatro umbrales están codificados como constantes en
`scripts/validate.py` y se verifican contra el bloque `mediciones` de cada nota de lote.

### Por qué estos números

- **80 ppm de nitrito** es el máximo *ingoing* para embutidos curados no tratados
  por calor según [[normativa-eu-2023-2108]] (bajó desde 150 ppm). Suficiente para
  el efecto antibotulínico sin excederse en nitrosaminas.
- **pH 5.3** es el techo por debajo del cual *Staphylococcus aureus* no produce
  enterotoxina en condiciones de fermentación. Es el objetivo de la fase de
  fermentación descrita en [[Procedimiento-embutido]].
- **665 grados-hora** es el límite del AMI (American Meat Institute) para la
  fase de fermentación cuando la temperatura máxima se mantiene por debajo de
  32.2 °C (90 °F). Se define en °F·h: `Σ (T_°F − 60) × h` hasta alcanzar pH 5.3.
  Superarlo permite crecimiento de *S. aureus* aunque el pH final sea correcto.
- **30 % de merma** es el mínimo de pérdida de peso que lleva la a_w a la zona
  estable (< 0.90) para un salame de calibre medio.

## Secuencia temporal de barreras

1. **Embutido / t=0**: nitrito + sal + cultivo iniciador. Barrera química arranca.
2. **Fermentación (24–72 h)**: el cultivo baja el pH. Acumular ≤ 665 °F·h hasta
   cruzar pH 5.3. Ver [[fermentacion-fallida]] si no acidifica.
3. **Secado (semanas)**: merma progresiva → cae la a_w. Riesgo de
   [[case-hardening]] si el gradiente de humedad es muy agresivo.
4. **Maduración**: flora de superficie deseada; controlar [[moho-indeseado]].

Registro de datos por lote: ver [[lote-00]] como plantilla y `tracker/registro-lotes.xlsx`.
