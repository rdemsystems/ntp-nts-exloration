# ntp-registry — serveurs NTP/NTS déclarés, et ce que nous avons mesuré

*[English version](README.md)*

On confond couramment deux affirmations sur un serveur de temps :

- **ce que l'opérateur dit servir** — une déclaration ;
- **ce qu'un client en obtient réellement** — une mesure.

Ce dépôt les sépare, délibérément, dans deux répertoires qui ne s'écrasent jamais.

| | `operators/` | `measurements/` |
|---|---|---|
| contenu | un fichier YAML par opérateur, listant les serveurs qu'il publie | campagnes de mesure datées, telles que publiées |
| propriétaire | l'opérateur | RDEM Systems |
| modifié par | pull request | jamais — une campagne se rescelle, elle ne se retouche pas |

Quand les deux divergent, **la divergence est le résultat**. Un serveur annoncé en NTS
qui ne sert aucune heure authentifiée est un constat, pas une erreur à lisser.

## Ce que « le NTS fonctionne » veut dire ici

Le NTS n'est pas un port, et ce n'est pas un certificat. C'est : *authentifie-toi, puis
va sur ce serveur avec ce jeton*. Donc :

- **NTP fonctionne** si et seulement si on récupère une heure **non authentifiée** (UDP/123).
- **NTS fonctionne** si et seulement si on récupère une heure **authentifiée** — la
  poignée NTS-KE complète (TCP/4460, ALPN `ntske/1`, certificat valide **pour le nom
  interrogé**), *puis* une réponse NTP authentifiée valide.

Les deux colonnes sont auto-portantes. Un serveur peut servir du NTS sans répondre au
NTP en clair — c'est exactement ce que fait Netnod, par conception. Un serveur peut
avoir un NTS-KE impeccable et ne servir aucune heure, parce qu'UDP/123 est filtré :
l'échange de clés a réussi, l'heure n'est jamais arrivée. Celui-là est cassé.

## Méthode de mesure

Chaque serveur est interrogé depuis **six points d'observation indépendants, dans six
systèmes autonomes différents**. Un point unique ne sait pas distinguer une ACL, un
rate-limit ou une restriction géographique d'une vraie panne. Les fractions publiées
(`4/6`, `0/6`) permettent de recompter avec un seuil différent du nôtre.

Les campagnes sont signées et horodatées (signature OpenPGP, deux autorités RFC 3161,
OpenTimestamps). Les fichiers `.asc`, `.tsr` et `.ots` de `measurements/` sont ces
preuves. **Une campagne scellée ne se retouche jamais.** Une correction part dans la
campagne suivante, en disant ce qui a changé.

## Rapport avec jauderho/nts-servers

[jauderho/nts-servers](https://github.com/jauderho/nts-servers) et son compagnon
[public-ntp-servers](https://github.com/jauderho/public-ntp-servers) sont de la
**documentation** : des listes curatées qu'on recopie dans un `chrony.conf` ou un
`ntp.toml` pour configurer un client. Ils font référence pour cet usage, et une partie
de ce registre en a été amorcée.

Ce dépôt-ci a un autre usage : le **monitoring**. Ses entrées existent pour être
sondées, mois après mois, depuis six points d'observation, et produire un relevé daté
de ce que chaque serveur a réellement servi. Une liste faite pour être collée dans un
fichier de configuration et une liste faite pour être mesurée dans la durée ne sont pas
le même objet — d'où deux dépôts plutôt qu'une pull request chez eux.

À terme, ce registre a vocation à se reposer sur un ensemble de sources plus large
plutôt que de rester curaté à la main.

## Contribuer

Votre fichier vous appartient. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et
[SCHEMA.md](SCHEMA.md).

Les fichiers d'`operators/` portant la ligne `# généré depuis les mesures RDEM Systems`
ont été pré-remplis depuis nos mesures publiques pour amorcer la liste — ils n'ont
**aucune valeur d'attestation**. Supprimez cette ligne dans votre pull request et le
fichier ne sera plus jamais régénéré automatiquement.

Nous ne remplissons pas les adresses de contact, et nous n'ajouterons pas à votre
fichier un serveur que vous n'avez pas publié.

## Périmètre

Europe et zone de service RIPE, étendu au monde à mesure des campagnes. L'Europe
centrale et orientale n'est aujourd'hui échantillonnée que partiellement : c'est un
**trou connu, pas un fait mesuré**.

## Licence

Données sous [CC BY 4.0](LICENSE). Attribution : RDEM Systems.
Mesures : <https://ntp.rdem-systems.com/>
