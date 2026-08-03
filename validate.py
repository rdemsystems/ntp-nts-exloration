#!/usr/bin/env python3
"""
validate.py — Vérifie un fichier de `servers/` avant d'ouvrir la pull request.

Ce script est VOLONTAIREMENT permissif : seul `hostname` est obligatoire, et une
valeur inconnue produit un avertissement, pas une erreur. Nous préférons un fichier
incomplet à un contributeur découragé — le reste, nous le mesurons.

Il refuse en revanche ce qui rendrait la donnée fausse plutôt qu'incomplète :
un nom d'hôte invalide, un champ qui n'existe pas dans le schéma (souvent une faute
de frappe qui serait silencieusement ignorée), ou un `stratum` déclaré — un stratum
est une mesure, pas une déclaration.

Usage :  ./validate.py servers/*.yml
"""
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML requis :  pip install pyyaml   (ou apt install python3-yaml)")

TOP = {"operator", "country", "website", "contact", "asn", "servers"}
SRV = {"hostname", "kind", "country", "location", "nts", "ipv4", "ipv6",
       "access", "asn", "alias_of", "notes"}
KINDS = {"server", "academic", "metrology", "cybersecurity", "operator", "hyperscaler",
         "service", "community", "anycast", "pool", "alias"}
ACCESS = {"public", "public-notify", "on-request", "restricted", "closed"}
HOST = re.compile(r"^(?=.{1,253}$)([a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}$", re.I)
# Refusé explicitement : ces champs sont des MESURES. Les accepter laisserait croire
# qu'on publie ce qu'un opérateur affirme de son propre service.
MEASURED = {"stratum", "uptime", "accuracy", "offset", "jitter", "reachable", "status"}


def check(path):
    errors, warns = [], []
    try:
        doc = yaml.safe_load(open(path, encoding="utf-8"))
    except Exception as e:
        return [f"YAML illisible : {e}"], []
    if not isinstance(doc, dict):
        return ["le fichier doit contenir un dictionnaire YAML"], []

    for k in doc:
        if k in MEASURED:
            errors.append(f"champ `{k}` refusé : c'est une MESURE, pas une déclaration")
        elif k not in TOP:
            warns.append(f"champ de premier niveau inconnu : `{k}` (faute de frappe ?)")

    servers = doc.get("servers")
    if not isinstance(servers, list) or not servers:
        return errors + ["`servers` doit être une liste non vide"], warns

    seen = set()
    for i, s in enumerate(servers, 1):
        p = f"servers[{i}]"
        if not isinstance(s, dict):
            errors.append(f"{p} : doit être un dictionnaire")
            continue
        h = str(s.get("hostname") or "").strip().lower()
        if not h:
            errors.append(f"{p} : `hostname` est obligatoire")
        elif not HOST.match(h):
            errors.append(f"{p} : `{h}` n'est pas un nom d'hôte valide")
        elif h in seen:
            errors.append(f"{p} : `{h}` en double dans ce fichier")
        else:
            seen.add(h)

        for k in s:
            if k in MEASURED:
                errors.append(f"{p} : champ `{k}` refusé — c'est une mesure")
            elif k not in SRV:
                warns.append(f"{p} : champ inconnu `{k}` (faute de frappe ?)")

        if s.get("kind") and s["kind"] not in KINDS:
            warns.append(f"{p} : `kind: {s['kind']}` inconnu — accepté, mais vérifiez")
        if s.get("access") and s["access"] not in ACCESS:
            warns.append(f"{p} : `access: {s['access']}` inconnu — accepté, mais vérifiez")
        if "nts" in s and s["nts"] not in (True, False, None):
            errors.append(f"{p} : `nts` doit valoir true, false ou null")
        for fam in ("ipv4", "ipv6"):
            if fam in s and s[fam] not in (True, False, None):
                errors.append(f"{p} : `{fam}` doit valoir true, false ou null")
    return errors, warns


def main():
    paths = [p for p in sys.argv[1:] if not p.endswith("EXAMPLE.yml")]
    if not paths:
        sys.exit("usage : ./validate.py servers/*.yml")
    bad = 0
    for p in paths:
        errors, warns = check(p)
        if errors:
            bad += 1
            print(f"✗ {p}")
            for e in errors:
                print(f"    ERREUR  {e}")
        elif warns:
            print(f"~ {p}")
        else:
            print(f"✓ {p}")
        for w in warns:
            print(f"    note    {w}")
    print(f"\n{len(paths)} fichier(s), {bad} en erreur")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
