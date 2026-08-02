# ntp-registry — declared NTP/NTS servers, and what we measured

*[Version française](README.fr.md)*

Two kinds of statements about a time server are routinely confused:

- **what the operator says it serves** — a declaration;
- **what a client actually gets from it** — a measurement.

This repository keeps them apart, on purpose, in two directories that never overwrite
each other.

| | `operators/` | `measurements/` |
|---|---|---|
| content | one YAML file per operator, listing the servers they publish | dated measurement campaigns, as published |
| owner | the operator | RDEM Systems |
| changed by | pull request | never — a campaign is sealed and reissued, not edited |

When the two disagree, **the disagreement is the result**. A server announced with NTS
that serves no authenticated time is a finding, not an error to be smoothed over.

## What "NTS works" means here

NTS is not a port, and it is not a certificate. It is: *authenticate, then go to that
server with this token*. So:

- **NTP works** if and only if we obtain **unauthenticated** time (UDP/123).
- **NTS works** if and only if we obtain **authenticated** time — the full NTS-KE
  handshake (TCP/4460, ALPN `ntske/1`, valid certificate **for the queried name**),
  *and then* a valid authenticated NTP response.

The two columns stand on their own. A server can serve NTS without answering plain NTP
— Netnod does exactly that, by design. A server can have a flawless NTS-KE and serve no
time at all, because UDP/123 is filtered: the key exchange succeeded, the clock never
arrived. That one counts as broken.

## Measurement method

Every server is queried from **six independent vantage points in six different
autonomous systems**. A single observation point cannot tell an ACL, a rate limit or a
geographic restriction from a real outage. The published fractions (`4/6`, `0/6`) let
you recount with a different threshold than ours.

Campaigns are cryptographically signed and timestamped (OpenPGP signature, two RFC 3161
timestamp authorities, OpenTimestamps). Files ending in `.asc`, `.tsr` and `.ots` in
`measurements/` are those proofs. **A sealed campaign is never edited.** A correction
goes into the next campaign, with the change stated.

## Relation to jauderho/nts-servers

[jauderho/nts-servers](https://github.com/jauderho/nts-servers) and its companion
[public-ntp-servers](https://github.com/jauderho/public-ntp-servers) are **documentation**:
curated lists you copy into a `chrony.conf` or an `ntp.toml` to configure a client. They
are the reference for that, and part of this registry was bootstrapped from them.

This repository has a different purpose: **monitoring**. Its entries exist to be probed,
month after month, from six vantage points, and to produce a dated record of what each
server actually served. A list meant to be pasted into a config file and a list meant to
be measured over time are not the same object — hence two repositories rather than a
pull request against theirs.

Over time this registry is intended to fall back on a broader set of sources rather than
remain hand-curated.

## Contributing

Your file is yours. See [CONTRIBUTING.md](CONTRIBUTING.md) and [SCHEMA.md](SCHEMA.md).

Files under `operators/` carrying the line `# généré depuis les mesures RDEM Systems`
were pre-filled from our public measurements to bootstrap the list — they carry **no
attestation value whatsoever**. Delete that line in your pull request and the file will
never be regenerated automatically again.

We do not fill in contact addresses, and we will not add a server to your file that you
have not published.

## Scope

Europe and the RIPE service region, extended worldwide as measurements allow. Central
and Eastern Europe is currently sampled only partially — that is a **known gap, not a
measured fact**.

## License

Data under [CC BY 4.0](LICENSE). Attribution: RDEM Systems.
Measurements: <https://ntp.rdem-systems.com/>
