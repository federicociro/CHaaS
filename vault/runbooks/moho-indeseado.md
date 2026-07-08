---
id: moho-indeseado
tipo: runbook
titulo: "Runbook — moho indeseado en superficie"
estado: activo
tags: [runbook, maduracion, moho, defecto]
creado: 2026-07-02
actualizado: 2026-07-09
---

# Runbook — Moho indeseado

**Síntoma**: mohos verdes, negros, azulados o peludos en la superficie durante
maduración. Distinto del moho blanco/gris deseado (*Penicillium nalgiovense* y
similares) que forma una capa fina y aterciopelada.

## Clasificación rápida

| Aspecto | Interpretación | Acción |
|---|---|---|
| Blanco/gris, fino, seco | Flora deseada | Ninguna |
| Verde intenso | *Penicillium* toxigénico posible | Retirar / descartar |
| Negro | *Cladosporium* / *Aspergillus* | Descartar |
| Peludo, húmedo | Exceso de HR + poca ventilación | Corregir cámara |

## Fotos de referencia

Las imágenes viven en `vault/runbooks/attachments/`. Se irán agregando a
medida que aparezcan casos reales en el taller (ver
[[attachments/README|convenciones de attachments]] para nombre, escala y
formato).

### Deseado — velo blanco parejo (*P. nalgiovense*)

> Superficie cubierta por una capa fina, blanca y aterciopelada. No penetra,
> no es peluda, no tiene manchas de color. Es lo que buscamos: ocupa el
> nicho e inhibe a los indeseados.

_Pendiente foto: `moho-blanco-deseado-01.jpg`._
<!-- ![[moho-blanco-deseado-01.jpg|400]] -->

### Indeseado — verde (*Penicillium* verde)

> Colonias verde intenso, pulverulentas, con halo. Aparecen con HR excesiva o
> ventilación insuficiente. Riesgo de micotoxinas → descartar la pieza si
> está extendido o penetrante.

_Pendiente foto: `moho-verde-01.jpg`._
<!-- ![[moho-verde-01.jpg|400]] -->

### Indeseado — negro (*Cladosporium* / *Aspergillus niger*)

> Manchas negras, secas o algo grasas, que suelen aparecer sobre corteza
> húmeda o zonas de condensación. Descartar la pieza; revisar cámara.

_Pendiente foto: `moho-negro-01.jpg`._
<!-- ![[moho-negro-01.jpg|400]] -->

### Indeseado — peludo largo (mucor / rhizopus)

> Filamentos largos, algodonosos, blanco-grisáceos, que crecen visiblemente
> "hacia afuera". Delatan HR alta y aire estancado. Corregir cámara y
> evaluar pieza a pieza.

_Pendiente foto: `moho-peludo-01.jpg`._
<!-- ![[moho-peludo-01.jpg|400]] -->

> Fotografiar con fondo neutro, luz difusa y regla/moneda para escala. Ver
> convenciones en `vault/runbooks/attachments/README.md`.

## Acción

1. **Aislar** la pieza afectada de las sanas.
2. Moho superficial leve y localizado: cepillar/frotar con salmuera o vinagre.
3. Moho verde/negro extendido o penetrante: **descartar la pieza** (micotoxinas
   difunden al interior, no basta con limpiar la corteza).
4. Revisar cámara: bajar HR a 78–82 %, mejorar circulación de aire, limpiar y
   desinfectar superficies (ver [[higiene-desinfeccion]]).

## Prevención

- Inóculo de moho noble en superficie para ocupar el nicho (competencia — es una
  de las barreras de [[barreras-control]]).
- HR y ventilación según [[Procedimiento-embutido]] paso 6.
- Evitar bolsas de aire y condensación; no amontonar piezas.

Relacionado: [[case-hardening]]

