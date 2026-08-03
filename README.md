# ntp-nts-exploration

**Add your NTP or NTS server here, and it will be measured in our next campaign.**

*[Version française](README.fr.md)*

We measure public NTP and NTS servers across Europe and, increasingly, worldwide —
from six independent vantage points in six different autonomous systems — and publish
the results as open data. This repository is how you get your servers into that
measurement.

One file per contributor, under [`servers/`](servers/). Copy
[`servers/EXAMPLE.yml`](servers/EXAMPLE.yml), fill it in, open a pull request. Your
file is yours: we do not edit it.

## What contributing means

Adding a server here is a **public declaration by its operator**. That is exactly what
we need, and it is the only thing we ask: we do not require you to prove anything, run
anything, or link back to us. Measuring is our job.

Concretely, your pull request tells us three things at once:

1. **the server exists** and you want it measured;
2. **you authorise the measurement** — we record this file as the source of that
   authorisation, and publish the link alongside every figure that involves your
   server;
3. **what you claim to serve** — NTS or not, which IP families, which access policy.

We then measure, and publish what we actually observe. **If our measurement disagrees
with your declaration, we publish both.** The disagreement is the interesting part, and
it is often how an operator discovers that their NTS-KE has been down for a month.

## What we measure, and what "NTS works" means here

NTS is not a port, and it is not a certificate. It is: *authenticate, then go to that
server with this token*. So:

- **NTP works** if and only if we obtain **unauthenticated** time (UDP/123).
- **NTS works** if and only if we obtain **authenticated** time — the full NTS-KE
  handshake (TCP/4460, ALPN `ntske/1`, certificate valid **for the queried name**),
  *and then* a valid authenticated NTP response.

Both stand on their own. A server can serve NTS without answering plain NTP — Netnod
does exactly that, by design. A server can have a flawless NTS-KE and serve no time at
all because UDP/123 is filtered: the key exchange succeeded, the clock never arrived.

We also record the stratum, the IP families, the certificate and its trust anchor, the
offset seen from each vantage point, and the disagreements between vantage points.

## How this differs from the existing lists

[jauderho/nts-servers](https://github.com/jauderho/nts-servers) and
[jauderho/public-ntp-servers](https://github.com/jauderho/public-ntp-servers), the
[mutin-sa gist](https://gist.github.com/mutin-sa/eea1c396b1e610a2da1e5550d94b0453) and
the [NTP.org public server registry](https://support.ntp.org/Servers/StratumOneTimeServers)
are **documentation**: curated lists you copy into a `chrony.conf` or an `ntp.toml` to
configure a client. They are the reference for that, and part of our own inventory was
bootstrapped from them — we credit them and re-read them at every campaign.

This repository is not that. It exists to **build our monitoring and speed up
discovery**. Its entries are not there to be copied into a config file; they are there
to be probed, month after month, from six vantage points, and to become a dated record
of what each server actually served.

That difference has practical consequences for you:

- **A list wants a server that works. We want a server that exists.** A server that is
  down, filtered, or that announces NTS without serving it belongs here — that is
  precisely the finding. It would be removed from a curated list.
- **We do not deduplicate you into a recommendation.** Declare four names for one
  machine and we will measure the four, tell you they are one machine, and count it
  once.
- **Adding your server here does not put it in a recommendation list.** It puts it in a
  measurement — and your server then appears in the published registry and on the map,
  with what we measured, whatever that turns out to be.

Concretely, contributing here saves us the slowest part of the work: finding servers.
Today we discover them by reading the upstream reference of other servers, by harvesting
the pool zones, and by reading operators' own pages — indirect routes that take weeks
and miss whoever never published anything. One pull request replaces all of that for
your infrastructure, and gets it measured in the next campaign rather than in six
months.

## What we do not do

**We do not recommend servers.** We measure, verify and instrument, to map the NTP and
NTS landscape. Our published CSV and JSON carry everything needed to filter — access
policy, families, stratum, NTS state and its evidence — and the choice is the reader's.

We also do not publish a stratum you declare: a stratum is a measurement, it changes
the moment an upstream source is lost, and a file in a git repository will not follow.

## Results

Measured campaigns, method, limits and per-vantage disagreements:

- **Europe** — [Time servers in Europe: who actually serves NTS?](https://ntp.rdem-systems.com/en/time-server-europe.php)
- **France** — [NTP servers in France](https://ntp.rdem-systems.com/en/ntp-server-france.php)
- **NTS explained** — [Securing NTP with TLS](https://ntp.rdem-systems.com/en/nts.php)

CSV and JSON under CC BY 4.0, campaigns cryptographically signed and timestamped.

## Files

| | |
|---|---|
| [`servers/`](servers/) | one YAML file per contributor — [`EXAMPLE.yml`](servers/EXAMPLE.yml) is the template |
| [`SCHEMA.md`](SCHEMA.md) | every field, and the ones that deliberately do not exist |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | how to submit, and how to contest a measurement |
| [`validate.py`](validate.py) | checks your file before you open the pull request |

## License

Declarations in `servers/` are contributed by their operators. Our measurements are
published under [CC BY 4.0](LICENSE), attribution: RDEM Systems.
