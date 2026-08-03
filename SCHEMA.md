# Schema — `servers/*.yml`

One YAML file per contributor. The filename is yours to choose; it has no meaning
beyond being unique. See [`servers/EXAMPLE.yml`](servers/EXAMPLE.yml).

**Only `hostname` is required.** Everything else improves the measurement, and an empty
field is always better than an invented one — we would rather record "unknown" than
publish a guess about your infrastructure.

## Top level

| field | meaning |
|---|---|
| `operator` | display name, as you want to be credited in our publications |
| `country` | default country for every server in the file |
| `website` | page documenting your time service, if you have one |
| `contact` | address for us to reach you about a measurement. **Never published** |
| `asn` | your AS number, if you have one |
| `servers` | list, see below |

## Per server

| field | values | why we want it |
|---|---|---|
| `hostname` | **required** | the name a client would configure — the name we probe, and the name whose certificate must be valid for NTS |
| `kind` | `server`, `academic`, `metrology`, `operator`, `community`, `anycast`, `pool`, `alias` | lets the map distinguish an institute from a volunteer |
| `country` | overrides the file-level value | a machine may sit elsewhere than its operator |
| `location` | free text: city, region, or scope for an anycast | |
| `nts` | `true` / `false` / `null` | **what you announce.** `null` means no claim, and that is a fine answer |
| `ipv4`, `ipv6` | `true` / `false` | which families you intend to serve — we measure them separately and will report a family that is down |
| `access` | `public`, `public-notify`, `on-request`, `restricted`, `closed` | published as data. It does not gate inclusion: a restricted server belongs on the map as much as an open one |
| `asn` | a number, or a list | AS diversity is one of the things the map shows |
| `alias_of` | canonical hostname | prevents one machine being counted several times |

## What ends up in our published data

Your declaration lands in the `nts_documented`, `access`, `operator`, `country`, `type`
and `alias_of` columns of the published CSV, and in the matching JSON fields — always
next to what we **measured**, never instead of it. Your file's URL is recorded as
`access_source`: every figure that involves your server carries the link to the
declaration that authorised the measurement.

## Fields that deliberately do not exist

**`stratum`.** A stratum is a measurement, not a property you can announce: it changes
the moment an upstream source is lost, and a file in a git repository will not follow.
We measure it and publish it with a date.

**Any status, uptime or accuracy field.** Same reason. This file says what you *offer*;
our campaigns say what a client *got*, from six networks, on a given day.

## Counting rules applied to this data

They decide whether your servers are counted once or five times.

1. **Deduplication is by resolved IP, not by hostname.** Several names for one machine
   is one machine. `alias_of` makes it explicit rather than leaving it to a DNS lookup.
2. **A round-robin name is not counted; its members are.** If `ntp.example.org` answers
   with two distinct machines, we count `ntp1` and `ntp2` and list the round-robin as
   what it is. Same for `kind: pool`.
3. **A transient DNS failure never promotes an alias into a server** — a name that
   stops resolving keeps the flag it had, so totals cannot inflate on their own.
