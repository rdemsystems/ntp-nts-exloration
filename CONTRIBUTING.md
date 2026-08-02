# Contributing / Contribuer

*English below the French.*

---

## Français

### Ajouter ou corriger votre service

1. Créez ou modifiez `operators/<votre-slug>.yml`. Le format est décrit dans
   [SCHEMA.md](SCHEMA.md), l'exemple complet est
   [`operators/rdem-systems.yml`](operators/rdem-systems.yml).
2. Si le fichier porte encore la ligne `# généré depuis les mesures RDEM Systems`,
   **supprimez-la** : c'est ce qui empêche toute régénération automatique ultérieure.
   Le fichier devient le vôtre.
3. Ouvrez une pull request. Les commits signés sont appréciés.

Nous ne demandons **aucune** vérification préalable de votre part : c'est notre travail
de mesurer, pas le vôtre de prouver. Votre déclaration est acceptée telle quelle, et la
mesure dira ce qu'elle dira.

### Ce que nous ne ferons pas

- Modifier votre fichier après que vous l'avez repris — sauf pour vous signaler par
  *issue* un écart entre déclaration et mesure.
- Remplir votre adresse de contact.
- Ajouter à votre fichier un serveur que vous n'avez pas publié.

### Contester une mesure

Ouvrez une *issue*, pas une pull request : `measurements/` n'est pas modifiable, les
campagnes sont signées et horodatées. Une mesure erronée est corrigée dans la campagne
suivante, en disant explicitement ce qui a changé — jamais par réécriture silencieuse.

Si vous pensez qu'une ACL, un rate-limit ou un filtrage nous a fait voir une panne qui
n'existe pas, dites-le : c'est précisément pour ça que nous sondons depuis six réseaux
différents, et le désaccord entre points d'observation est publié.

---

## English

### Add or fix your service

1. Create or edit `operators/<your-slug>.yml`. Format in [SCHEMA.md](SCHEMA.md), full
   example in [`operators/rdem-systems.yml`](operators/rdem-systems.yml).
2. If the file still carries the line `# généré depuis les mesures RDEM Systems`,
   **delete it**. That line is the only thing allowing automatic regeneration; without
   it the file is yours.
3. Open a pull request. Signed commits are appreciated.

We ask for **no** prior verification from you: measuring is our job, not your burden of
proof. Your declaration is taken as written, and the measurement will say what it says.

### What we will not do

- Touch your file once you have taken it over — other than opening an issue when
  declaration and measurement disagree.
- Fill in your contact address.
- Add a server to your file that you have not published.

### Disputing a measurement

Open an issue, not a pull request: `measurements/` is not editable, campaigns are signed
and timestamped. A wrong measurement is corrected in the next campaign, stating what
changed — never by silent rewrite.

If you believe an ACL, a rate limit or a filter made us see an outage that does not
exist, say so: that is exactly why we probe from six different networks, and
disagreement between vantage points is published.
