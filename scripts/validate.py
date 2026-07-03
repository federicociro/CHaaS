#!/usr/bin/env python3
"""Validador del vault CHaaS.

Sobre cada nota Markdown de vault/ verifica:
  1. Frontmatter YAML presente con las claves requeridas.
  2. `id` == nombre del archivo (stem) y único en todo el vault.
  3. Wikilinks [[destino]] resuelven a una nota existente.

Los umbrales de inocuidad (nitrito, pH, merma, grados-hora) se documentan en
vault/tecnica/barreras-control.md y se auditan sobre la planilla de lotes,
no acá.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

VAULT = Path(__file__).resolve().parent.parent / "vault"
CLAVES_REQUERIDAS = {"id", "tipo", "titulo", "estado", "tags", "creado", "actualizado"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
# [[destino]] | [[destino|alias]] | [[destino#seccion]] — captura solo el destino
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def main() -> int:
    if not VAULT.is_dir():
        print(f"ERROR: no existe el vault en {VAULT}", file=sys.stderr)
        return 1

    errores: list[str] = []
    notas: list[tuple[Path, dict, str]] = []

    for path in sorted(VAULT.rglob("*.md")):
        rel = path.relative_to(VAULT.parent)
        texto = path.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(texto)
        if not m:
            errores.append(f"{rel}: sin frontmatter YAML")
            continue
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            errores.append(f"{rel}: YAML inválido ({e})")
            continue
        if not isinstance(meta, dict):
            errores.append(f"{rel}: frontmatter no es un mapa")
            continue

        faltan = CLAVES_REQUERIDAS - set(meta)
        if faltan:
            errores.append(f"{rel}: faltan claves {sorted(faltan)}")
        if meta.get("id") != path.stem:
            errores.append(f"{rel}: id '{meta.get('id')}' != archivo '{path.stem}'")

        notas.append((path, meta, m.group(2)))

    ids: dict[str, Path] = {}
    for path, meta, _ in notas:
        nid = meta.get("id")
        if not nid:
            continue
        if nid in ids:
            errores.append(f"{path.relative_to(VAULT.parent)}: id duplicado '{nid}' (ya en {ids[nid]})")
        else:
            ids[nid] = path.relative_to(VAULT.parent)

    conocidos = {path.stem for path, _, _ in notas}
    for path, _, cuerpo in notas:
        rel = path.relative_to(VAULT.parent)
        for destino in WIKILINK_RE.findall(cuerpo):
            destino = destino.strip()
            if destino not in conocidos:
                errores.append(f"{rel}: wikilink roto -> [[{destino}]]")

    print(f"Notas analizadas: {len(notas)}")
    if errores:
        print(f"\n{len(errores)} error(es):")
        for e in errores:
            print(f"  ✗ {e}")
        return 1

    print("✓ Todo OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
