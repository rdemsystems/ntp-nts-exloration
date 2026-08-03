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

## En quoi c'est différent des listes existantes

[jauderho/nts-servers](https://github.com/jauderho/nts-servers) et
[jauderho/public-ntp-servers](https://github.com/jauderho/public-ntp-servers), le
[gist de mutin-sa](https://gist.github.com/mutin-sa/eea1c396b1e610a2da1e5550d94b0453)
et le [registre public NTP.org](https://support.ntp.org/Servers/StratumOneTimeServers)
sont de la **documentation** : des listes curatées qu'on recopie dans un `chrony.conf`
ou un `ntp.toml` pour configurer un client. Ils font référence pour cet usage, et une
partie de notre inventaire en a été amorcée — nous les créditons et nous les relisons à
chaque campagne.

Ce dépôt n'est pas ça. Il existe pour **construire notre monitoring et accélérer la
découverte**. Ses entrées ne sont pas là pour être recopiées dans un fichier de
configuration, elles sont là pour être sondées, mois après mois, depuis six points
d'observation, et devenir un relevé daté de ce que chaque serveur a réellement servi.

Cette différence a des conséquences concrètes pour vous :

- **Une liste veut un serveur qui marche. Nous voulons un serveur qui existe.** Un
  serveur en panne, filtré, ou qui annonce du NTS sans en servir a toute sa place ici —
  c'est précisément le constat. Une liste curatée l'en retirerait.
- **Nous ne vous dédoublonnons pas en recommandation.** Déclarez quatre noms pour une
  machine : nous mesurerons les quatre, nous dirons que c'est une seule machine, et
  nous la compterons une fois.
- **Ajouter votre serveur ici ne le met dans aucune liste de recommandation.** Ça le met
  dans une mesure — et votre serveur figure alors dans le registre publié et sur la
  carte, avec ce que nous avons mesuré, quel que soit le résultat.

Concrètement, contribuer ici nous épargne la partie la plus lente du travail : trouver
les serveurs. Aujourd'hui nous les découvrons en lisant la source amont d'autres
serveurs, en moissonnant les zones du pool et en lisant les pages des opérateurs — des
chemins indirects qui prennent des semaines et qui ratent ceux qui n'ont jamais rien
publié. Une pull request remplace tout ça pour votre infrastructure, et la fait mesurer
à la prochaine campagne plutôt que dans six mois.

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
