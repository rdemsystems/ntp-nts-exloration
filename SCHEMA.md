# Schema — `operators/*.yml`

One file per operator. Filename is a slug of the operator name; it has no meaning
beyond being unique. See [`operators/rdem-systems.yml`](operators/rdem-systems.yml) for
a fully worked example.

## Top level

| field | required | meaning |
|---|---|---|
| `operator` | yes | display name, as you want to be credited |
| `country` | no | default country for every server in the file |
| `website` | no | page documenting your time service |
| `contact` | no | address for us to reach you about a measurement. We never fill this in |
| `asn` | no | your own AS number, if you have one |
| `servers` | yes | list, see below |

## Per server

| field | required | values |
|---|---|---|
| `hostname` | yes | the name a client would configure |
| `kind` | no | `server`, `academic`, `metrology`, `operator`, `community`, `anycast`, `pool`, `alias` |
| `country` | no | overrides the file-level `country` — use it when a machine sits elsewhere |
| `location` | no | free text: city, region, or scope for anycast |
| `asn` | no | number, or list of numbers when several transits serve the machine |
| `nts` | yes | `true` / `false` / `null`. **What you announce**, not what we measured. `null` = no claim |
| `access` | no | `public`, `public-notify`, `on-request`, `restricted`, `closed` |
| `alias_of` | no | canonical hostname, when this name points at a machine already listed |

## Fields that deliberately do not exist

**`stratum`.** A stratum is a measurement, not a property you can announce: it changes
the moment an upstream source is lost, and a file in a git repository will not follow.
It belongs in `measurements/`, where it carries a date.

**Any status, uptime or accuracy field.** Same reason. This file says what you *offer*;
the measurements say what a client *got*.

## Counting rules used against this data

They matter, because they decide whether your servers are counted once or five times.

1. **Deduplicate by resolved IP, not by hostname.** Several names for one machine is one
   machine. `alias_of` makes this explicit rather than leaving it to a DNS lookup.
2. **`kind: pool` entries are not counted as machines.** A round-robin or load-balanced
   name is an entry point. This is an accounting rule, not a judgement: a pool with a
   central NTS-KE works, and we have measured one.
3. **A transient DNS failure never promotes an alias into a server** — a name that stops
   resolving keeps the flag it had, so totals cannot inflate on their own.
