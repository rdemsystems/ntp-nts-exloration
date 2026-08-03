# Contributing / Contribuer

*English below the French.*

---

## Français

### Ajouter vos serveurs

1. Copiez [`servers/EXAMPLE.yml`](servers/EXAMPLE.yml) sous le nom de votre
   organisation, par exemple `servers/mon-organisation.yml`.
2. Remplissez-le. **Seul `hostname` est obligatoire.** Le format est décrit dans
   [SCHEMA.md](SCHEMA.md).
3. Vérifiez : `./validate.py servers/mon-organisation.yml`
4. Ouvrez une pull request. Les commits signés sont appréciés, pas exigés.

Nous ne demandons **aucune** vérification préalable de votre part : mesurer est notre
travail, pas votre charge de preuve. Votre déclaration est prise telle qu'écrite, et la
mesure dira ce qu'elle dira.

### Ce que nous ne ferons pas

- Modifier votre fichier. Il est à vous. Si notre mesure contredit votre déclaration,
  nous ouvrons une *issue* — nous ne corrigeons pas votre texte.
- Publier votre adresse de contact.
- Ajouter à votre fichier un serveur que vous n'avez pas déclaré.
- Vous demander un lien retour, une inscription, ou quoi que ce soit en échange.

### Retirer un serveur

Ouvrez une pull request qui le supprime, ou une *issue* si vous préférez. Nous
cesserons de le sonder à la campagne suivante. Les campagnes déjà publiées ne sont pas
réécrites : elles sont signées et horodatées, et une mesure passée reste vraie pour la
date où elle a été faite.

### Contester une mesure

Ouvrez une *issue*. Une mesure erronée est corrigée dans la campagne suivante, en
disant explicitement ce qui a changé — jamais par réécriture silencieuse.

Si vous pensez qu'une ACL, un rate-limit ou un filtrage nous a fait voir une panne qui
n'existe pas, dites-le : c'est précisément pour ça que nous sondons depuis six réseaux
différents, et le désaccord entre points d'observation est publié tel quel.

---

## English

### Add your servers

1. Copy [`servers/EXAMPLE.yml`](servers/EXAMPLE.yml) to your organisation's name, e.g.
   `servers/my-organisation.yml`.
2. Fill it in. **Only `hostname` is required.** Format in [SCHEMA.md](SCHEMA.md).
3. Check it: `./validate.py servers/my-organisation.yml`
4. Open a pull request. Signed commits are appreciated, not required.

We ask for **no** prior verification: measuring is our job, not your burden of proof.
Your declaration is taken as written, and the measurement will say what it says.

### What we will not do

- Edit your file. It is yours. If our measurement contradicts your declaration we open
  an issue — we do not rewrite your text.
- Publish your contact address.
- Add a server to your file that you have not declared.
- Ask for a backlink, a signup, or anything in return.

### Removing a server

Open a pull request removing it, or an issue if you prefer. We stop probing it at the
next campaign. Published campaigns are not rewritten: they are signed and timestamped,
and a past measurement stays true for the date it was made.

### Disputing a measurement

Open an issue. A wrong measurement is corrected in the next campaign, stating what
changed — never by silent rewrite.

If you believe an ACL, a rate limit or a filter made us see an outage that does not
exist, say so: that is exactly why we probe from six different networks, and
disagreement between vantage points is published as-is.
