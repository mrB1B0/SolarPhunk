# SolarPhunk Core Principles

> **Status:** v0 draft — derived from the Solarpunk movement and the project
> mission. Meant to be argued with. Changes go through an ADR in
> [`docs/adr/`](adr/) once that folder exists.

## Mission

SolarPhunk is an open-source platform of projects that apply AI to Solarpunk-style
work: hacking together entirely new **tools, machines, art projects, and
inventions** from old, discarded, broken, donor, or natural materials. The core
platform is a multi-player, agentic, self-healing, secure, and environmentally
safe set of technology solutions.

## The principles

Seven principles. Each has a plain meaning and a **platform obligation** — how
the software is expected to embody or enforce it.

### 1. Sufficiency, then salvage
The best project is often no new object. Refuse what isn't needed, repair what
already exists, adapt what you have — and only then build. When you do build,
start from discarded, broken, donor, or naturally abundant material; newly
extracted or manufactured material is a last resort that must be named and
justified. Design things to come apart without destruction and to return their
materials to use or safely to nature.
**Platform obligation:** ideation proposes the smallest intervention first
(repair or adapt before build); a brief that leans on virgin material or that
duplicates a thing that already exists is flagged and must carry a written
rationale; every design records its disassembly and end-of-life paths.

### 2. Appropriate technology
Use the simplest technology that solves the problem: low power, low complexity,
maintainable by one person in their own workshop. AI is a tool in service of the
work, not the point of it — prefer small, local, or cached inference over
reaching for the largest model.
**Platform obligation:** agents default to small/local models and cached
results; heavier compute is justified per job and its energy is logged.

### 3. Safety and provenance are gates
Nothing harmful ships with a warning label. Before a project is blessed it
passes a hazard-and-lifecycle review — toxicity, emissions, fire/electrical/
mechanical risk, energy over lifetime, e-waste created versus diverted, effect
on land and water — and an honest-provenance review: every material has an
attributable, consensual source, with no theft, exploitation, or ecological
damage, including when harvesting natural material. Claims of "green,"
"circular," or "low-energy" — about a project or about the platform itself — are
backed by simple, auditable evidence.
**Platform obligation:** these reviews sit in the critical path and can block; a
blessed project carries signed review artifacts and links every claim to its
evidence.

### 4. An open knowledge commons
Designs, code, bills of materials, build logs, review artifacts, and failures
are shared so others can reproduce them and build on them. Knowledge is a
commons, not an asset.
**Platform obligation:** contributions are normalised into a shared, inspectable,
exportable store with a license, provenance, and enough detail to reproduce.
(License stance per artifact type — to be decided via ADR.)

### 5. Local-first and resilient
The platform runs offline, on modest hardware, next to the workbench. It
degrades gracefully and repairs itself. No hard dependency on a central service
or a single vendor.
**Platform obligation:** all core features work with no network; jobs are
resumable and idempotent; a supervisor retries, reroutes, and restores from
verified backups.

### 6. Many hands, human judgment
The platform is multi-player by design: projects are collaborative, and
contribution, credit, and governance are visible to everyone involved. Within
that, agents propose and people decide — especially on safety, ethics, and
aesthetics. Automation never removes accountability from a person.
**Platform obligation:** a facilitator coordinates human and agent participants;
an append-only decision log records who chose what and why; blessing, and any
irreversible or outward-facing action, requires a human checkpoint.

### 7. Built with care, made to delight
The safety, health, and cognitive load of the people doing the building are
designed in, and projects stay reachable across a range of bodies, budgets,
tools, and skill levels. And the result should be good to look at and good to
live with — craft, beauty, and how a thing makes people feel are goals on equal
footing with function.
**Platform obligation:** build plans state required PPE, ventilation, tools,
skill level, and time honestly; project briefs carry intent for form and
feeling, not only specification.

## How principles are used

- **Ideation** filters and ranks candidate projects against these principles,
  and proposes the smallest intervention first.
- **Review gates** (principle 3) turn the safety, provenance, and honest-claims
  obligations into pass / needs-changes / block verdicts with written findings.
- **Governance** changes to this document are proposed as ADRs and tagged with a
  version, so a blessed project can cite the principles it was reviewed under.
