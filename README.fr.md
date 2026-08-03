# ntp-nts-exploration

**Ajoutez ici votre serveur NTP ou NTS : il sera mesuré à notre prochaine campagne.**

*[English version](README.md)*

Nous mesurons les serveurs NTP et NTS publics d'Europe — et, de plus en plus, du monde
— depuis six points d'observation indépendants dans six systèmes autonomes différents,
et nous publions les résultats en données ouvertes. Ce dépôt est la façon d'y faire
entrer vos serveurs.

Un fichier par contributeur, dans [`servers/`](servers/). Copiez
[`servers/EXAMPLE.yml`](servers/EXAMPLE.yml), remplissez-le, ouvrez une pull request.
Votre fichier vous appartient : nous n'y touchons pas.

## Ce que contribuer veut dire

Ajouter un serveur ici est une **déclaration publique de son opérateur**. C'est
exactement ce dont nous avons besoin, et c'est tout ce que nous demandons : rien à
prouver, rien à installer, aucun lien retour. Mesurer est notre travail.

Concrètement, votre pull request nous dit trois choses à la fois :

1. **le serveur existe** et vous voulez qu'il soit mesuré ;
2. **vous autorisez la mesure** — nous enregistrons ce fichier comme la source de cette
   autorisation, et nous publions le lien à côté de chaque chiffre qui concerne votre
   serveur ;
3. **ce que vous annoncez servir** — NTS ou non, quelles familles IP, quelle politique
   d'accès.

Nous mesurons ensuite, et nous publions ce que nous observons réellement. **Si notre
mesure contredit votre déclaration, nous publions les deux.** L'écart est la partie
intéressante — c'est souvent ainsi qu'un opérateur découvre que son NTS-KE est tombé
depuis un mois.

## Ce que nous mesurons, et ce que « le NTS fonctionne » veut dire ici

Le NTS n'est pas un port, et ce n'est pas un certificat. C'est : *authentifie-toi, puis
va sur ce serveur avec ce jeton*. Donc :

- **NTP fonctionne** si et seulement si on récupère une heure **non authentifiée** (UDP/123).
- **NTS fonctionne** si et seulement si on récupère une heure **authentifiée** — la
  poignée NTS-KE complète (TCP/4460, ALPN `ntske/1`, certificat valide **pour le nom
  interrogé**), *puis* une réponse NTP authentifiée valide.

Les deux tiennent séparément. Un serveur peut servir du NTS sans répondre au NTP en
clair — Netnod le fait par conception. Un serveur peut avoir un NTS-KE impeccable et ne
servir aucune heure parce qu'UDP/123 est filtré : l'échange de clés a réussi, l'heure
n'est jamais arrivée.

Nous relevons aussi le stratum, les familles IP, le certificat et son ancre de
confiance, l'offset vu depuis chaque point d'observation, et les désaccords entre eux.

## Ce que nous ne faisons pas

**Nous ne recommandons aucun serveur.** Nous mesurons, vérifions et instrumentons, pour
cartographier le paysage NTP et NTS. Nos CSV et JSON publiés portent tout ce qu'il faut
pour filtrer — politique d'accès, familles, stratum, état NTS et sa preuve — et le choix
appartient au lecteur.

Nous ne publions pas non plus un stratum que vous déclareriez : un stratum est une
mesure, il change à la seconde où une source amont est perdue, et un fichier dans un
dépôt git ne suivra pas.

## Résultats

Campagnes mesurées, méthode, limites et désaccords entre points d'observation :
<https://ntp.rdem-systems.com/> — CSV et JSON sous CC BY 4.0, campagnes signées et
horodatées cryptographiquement.

## Fichiers

| | |
|---|---|
| [`servers/`](servers/) | un fichier YAML par contributeur — [`EXAMPLE.yml`](servers/EXAMPLE.yml) est le modèle |
| [`SCHEMA.md`](SCHEMA.md) | tous les champs, et ceux qui n'existent délibérément pas |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | comment soumettre, et comment contester une mesure |
| [`validate.py`](validate.py) | vérifie votre fichier avant d'ouvrir la pull request |

## Licence

Les déclarations de `servers/` appartiennent à leurs opérateurs. Nos mesures sont
publiées sous [CC BY 4.0](LICENSE), attribution : RDEM Systems.
