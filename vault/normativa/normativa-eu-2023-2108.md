---
id: normativa-eu-2023-2108
tipo: normativa
titulo: "Reglamento (UE) 2023/2108 — nitritos y nitratos"
estado: activo
tags: [normativa, nitrito, eu, legal]
creado: 2026-07-02
actualizado: 2026-07-02
fuente: "https://eur-lex.europa.eu/eli/reg/2023/2108/oj"
---

# Reglamento (UE) 2023/2108

Modifica el Anexo II del Reg. (CE) 1333/2008 y el Anexo del Reg. (UE) 231/2012
en cuanto al uso de **nitritos (E 249–E 250) y nitratos (E 251–E 252)** como
aditivos alimentarios. Reduce las cantidades máximas permitidas para bajar la
exposición a nitrosaminas, siguiendo la reevaluación de EFSA.

## Lo que importa para este vault

- **Nitrito de sodio (E 250)**: la cantidad **máxima *ingoing*** para productos
  cárnicos curados no tratados por calor baja a **80 mg/kg (≈ 80 ppm)** — desde
  los 150 mg/kg previos. Es el techo que documenta [[barreras-control]] y que
  se registra en el bloque `mediciones` de cada lote.
- Se razona sobre cantidad **añadida (ingoing)**, no residual: se controla en
  formulación, pesando el nitrito (ver [[Procedimiento-embutido]] paso 1).
- Períodos transitorios para agotar producto formulado bajo las reglas viejas;
  para lotes nuevos aplicamos el límite reducido directamente.

## Por qué 80 ppm y no menos

El nitrito es la barrera antibotulínica clave (ver [[barreras-control]]). El
reglamento busca el mínimo eficaz: suficiente para inhibir *C. botulinum* sin
excedente que derive en nitrosaminas. Bajar de ahí compromete la seguridad.

## Aplicación en el repo

Todo lote debe registrar `nitrito_ppm ≤ 80` en su frontmatter (plantilla
[[lote-00]]). El validador falla el lote si se supera.

> Nota: verificar siempre el texto consolidado en EUR-Lex; las cifras exactas por
> categoría de producto están en el Anexo. Este resumen es orientativo, no
> sustituye la lectura de la fuente.
