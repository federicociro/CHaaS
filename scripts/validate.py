#!/usr/bin/env python3
"""Validador del vault Chass.

Verifica, sobre cada nota Markdown de vault/:
  1. Frontmatter YAML presente y con las claves requeridas.
  2. `id` == nombre del archivo (stem) y único en todo el vault.
  3. Wikilinks [[destino]] resuelven a una nota existente.
  4. Umbrales de seguridad (barreras) en el bloque `mediciones` de los lotes.

Umbrales (ver vault/tecnica/barreras-control.md):
  - Nitrito ingoing ....... <= 80 ppm
  - pH final .............. <= 5.3
  - Merma ................. >= 30 %
  - Grados-hora (°F·h) .... <= 665

Salida: reporte legible + exit code 1 si hay cualquier error.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

# --- Umbrales de barreras -------------------------------------------------
LIMITE_NITRITO_PPM = 80.0     # máx. ingoing (Reg. UE 2023/2108)
LIMITE_PH = 5.3               # techo del pH final de fermentación
LIMITE_MERMA_PCT = 30.0       # mínimo de pérdida de peso
LIMITE_GRADOS_HORA = 665.0    # máx. °F·h hasta pH 5.3 (AMI)

# --- Config ---------------------------------------------------------------
VAULT = Path(__file__).resolve().parent.parent / "vault"
CLAVES_REQUERIDAS = {"id", "tipo", "titulo", "estado", "tags", "creado", "actualizado"}
TIPOS_VALIDOS = {"lote", "tecnica", "procedimiento", "runbook", "normativa", "referencia"}
ESTADOS_VALIDOS = {"borrador", "activo", "archivado"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
# [[destino]] | [[destino|alias]] | [[destino#seccion]] — captura solo el destino
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


class Nota:
    def __init__(self, path: Path, meta: dict, cuerpo: str):
        self.path = path
        self.meta = meta
        self.cuerpo = cuerpo

    @property
    def stem(self) -> str:
        return self.path.stem

    def rel(self) -> str:
        return str(self.path.relative_to(VAULT.parent))


def cargar_notas(errores: list[str]) -> list[Nota]:
    notas: list[Nota] = []
    for path in sorted(VAULT.rglob("*.md")):
        texto = path.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(texto)
        if not m:
            errores.append(f"{path.relative_to(VAULT.parent)}: sin frontmatter YAML")
            continue
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            errores.append(f"{path.relative_to(VAULT.parent)}: YAML inválido ({e})")
            continue
        if not isinstance(meta, dict):
            errores.append(f"{path.relative_to(VAULT.parent)}: frontmatter no es un mapa")
            continue
        notas.append(Nota(path, meta, m.group(2)))
    return notas


def validar_frontmatter(nota: Nota, errores: list[str]) -> None:
    faltan = CLAVES_REQUERIDAS - set(nota.meta)
    if faltan:
        errores.append(f"{nota.rel()}: faltan claves {sorted(faltan)}")

    if nota.meta.get("id") != nota.stem:
        errores.append(
            f"{nota.rel()}: id '{nota.meta.get('id')}' != nombre de archivo '{nota.stem}'"
        )

    tipo = nota.meta.get("tipo")
    if tipo is not None and tipo not in TIPOS_VALIDOS:
        errores.append(f"{nota.rel()}: tipo '{tipo}' inválido (usar {sorted(TIPOS_VALIDOS)})")

    estado = nota.meta.get("estado")
    if estado is not None and estado not in ESTADOS_VALIDOS:
        errores.append(f"{nota.rel()}: estado '{estado}' inválido (usar {sorted(ESTADOS_VALIDOS)})")

    tags = nota.meta.get("tags")
    if tags is not None and not isinstance(tags, list):
        errores.append(f"{nota.rel()}: 'tags' debe ser una lista")


def validar_ids_unicos(notas: list[Nota], errores: list[str]) -> None:
    vistos: dict[str, str] = {}
    for nota in notas:
        nid = nota.meta.get("id")
        if not nid:
            continue
        if nid in vistos:
            errores.append(f"{nota.rel()}: id duplicado '{nid}' (ya en {vistos[nid]})")
        else:
            vistos[nid] = nota.rel()


def validar_wikilinks(notas: list[Nota], errores: list[str]) -> None:
    conocidos = {nota.stem for nota in notas}
    for nota in notas:
        for destino in WIKILINK_RE.findall(nota.cuerpo):
            destino = destino.strip()
            if destino not in conocidos:
                errores.append(f"{nota.rel()}: wikilink roto -> [[{destino}]]")


def validar_umbrales(notas: list[Nota], errores: list[str]) -> int:
    """Valida el bloque `mediciones` de las notas de lote. Devuelve nº de lotes OK."""
    checks = [
        ("nitrito_ppm", lambda v: v <= LIMITE_NITRITO_PPM, f"<= {LIMITE_NITRITO_PPM} ppm"),
        ("ph_final", lambda v: v <= LIMITE_PH, f"<= {LIMITE_PH}"),
        ("merma_pct", lambda v: v >= LIMITE_MERMA_PCT, f">= {LIMITE_MERMA_PCT} %"),
        ("grados_hora", lambda v: v <= LIMITE_GRADOS_HORA, f"<= {LIMITE_GRADOS_HORA} °F·h"),
    ]
    lotes_ok = 0
    for nota in notas:
        if nota.meta.get("tipo") != "lote":
            continue
        med = nota.meta.get("mediciones")
        if not isinstance(med, dict):
            errores.append(f"{nota.rel()}: lote sin bloque 'mediciones'")
            continue
        fallo = False
        for campo, ok, desc in checks:
            if campo not in med:
                errores.append(f"{nota.rel()}: mediciones sin '{campo}'")
                fallo = True
                continue
            valor = med[campo]
            if not isinstance(valor, (int, float)):
                errores.append(f"{nota.rel()}: mediciones.{campo} no es numérico")
                fallo = True
                continue
            if not ok(valor):
                errores.append(
                    f"{nota.rel()}: umbral fuera de rango mediciones.{campo}={valor} (debe ser {desc})"
                )
                fallo = True
        if not fallo:
            lotes_ok += 1
    return lotes_ok


def main() -> int:
    if not VAULT.is_dir():
        print(f"ERROR: no existe el vault en {VAULT}", file=sys.stderr)
        return 1

    errores: list[str] = []
    notas = cargar_notas(errores)

    for nota in notas:
        validar_frontmatter(nota, errores)
    validar_ids_unicos(notas, errores)
    validar_wikilinks(notas, errores)
    lotes_ok = validar_umbrales(notas, errores)

    print(f"Notas analizadas : {len(notas)}")
    print(f"Lotes en umbral  : {lotes_ok}")
    print(
        "Umbrales         : "
        f"nitrito<={LIMITE_NITRITO_PPM}ppm, pH<={LIMITE_PH}, "
        f"merma>={LIMITE_MERMA_PCT}%, grados-hora<={LIMITE_GRADOS_HORA}"
    )

    if errores:
        print(f"\n{len(errores)} error(es):")
        for e in errores:
            print(f"  ✗ {e}")
        return 1

    print("\n✓ Todo OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
