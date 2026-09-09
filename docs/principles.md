# SolarPhunk Core Principles

> **Status:** v0 draft, written in the voice of a manifesto because that is the
> tradition it comes from. Derived from the Solarpunk movement (see
> [Sources](#sources-and-influences)) and the project mission. Argue with it.
> Changes go through an ADR in [`docs/adr/`](adr/) once that folder exists.

## Mission

SolarPhunk is an open-source platform of projects that apply AI to Solarpunk-style
work: hacking together entirely new **tools, machines, art projects, and
inventions** from old, discarded, broken, donor, or natural materials. The core
platform is a multi-player, agentic, self-healing, secure, and environmentally
safe set of technology solutions.

## Preamble

The alternatives to hope are denial and despair, and we are not interested in
either. Solarpunk asks what a just, regenerative civilization looks like and how
we get there from where we stand. SolarPhunk is one small answer: people and AI
agents building real things out of what the world threw away. These seven
principles say what we will and won't build — and they hold the platform to the
same standard as the projects it helps make.

## The principles

Each principle is followed by **In the platform:** — the obligation it places on
the software itself.

### 1. Hope, made real
We build our way forward, we don't only write our way forward. The deliverable
is a small thing that works, can be repaired, and can be shared — and it should
be beautiful, because beauty is part of what makes a future worth wanting.
**In the platform:** every project ends in something reproducible — a bill of
materials, a build plan, a photo of the finished thing — never a document that
stops at intent.

### 2. Sufficiency first
The best project is often no new object. Refuse what isn't needed, repair what
exists, adapt what you have, build from salvage — and only as a justified last
resort, from new material. What we make is designed to come apart without
destruction and to return to use or safely to the ground. We decide in
generations, not quarters.
**In the platform:** ideation proposes the smallest intervention before the
largest; a brief that needs virgin material, or repeats a thing that already
exists, is flagged and must argue for itself; every design records its
disassembly and end-of-life paths.

### 3. Regenerate, don't just spare
"Less harm" is not the bar. A project should leave its place — the land, the
water, the air, the people around it — better than it found it. Safety and
honest provenance are hard gates: nothing toxic, stolen, or extracted through
exploitation gets through, and no claim of "green" or "circular" ships without
evidence, including claims about this platform.
**In the platform:** the hazard-and-lifecycle review and the provenance review
sit in the critical path and can block; a blessed project carries signed review
artifacts and links every environmental claim to its data.

### 4. Appropriate, legible technology
Use the simplest tool that meets the real need: low power, low part count,
fixable by one person in their own workshop, and taking its cues from how nature
already solves the problem. You should be able to see how it works — no black
boxes, ours included. AI is a tool here, not the point: prefer small and local
models, and always show the working.
**In the platform:** agents default to small/local models and cached results;
heavier compute is justified per job and its energy logged; every agent output
carries its reasoning and its sources.

### 5. Knowledge is a commons
Designs, code, build logs, review artifacts, and failures are shared so anyone
can reproduce them and build further. We favour mutual aid and the gift over
ownership and enclosure. Methods are plural: Indigenous and non-Western
practice, jugaad, and folk repair knowledge belong here, and are credited to
the people and traditions they come from.
**In the platform:** contributions are normalised into a shared, inspectable,
exportable store with a license, provenance, and enough detail to reproduce.
(License stance per artifact type — to be decided via ADR.)

### 6. Nothing radical is out of reach
If it is inaccessible to the poor, it is neither radical nor revolutionary. A
project has to be reachable across income, body, language, tools, and skill, and
it should dismantle hierarchies of race, class, gender, and ability rather than
quietly route around them. That care extends to the maker: their health, their
safety, and their attention are part of the design.
**In the platform:** build plans state cost, required PPE and ventilation,
tools, skill level, and time honestly; accessibility gaps are named in the
review, not left for the builder to hit later.

### 7. No chokepoints
Horizontal, decentralized, multi-player. No single authority — human or machine
— sits between a person and the work. Agents propose; people decide; the
decisions are logged in the open. The platform runs offline on modest hardware
and repairs itself, so no server, vendor, or gatekeeper can switch it off.
**In the platform:** an append-only decision log records who chose what and why;
blessing and any irreversible action need a human checkpoint; all core features
work with no network; jobs are resumable and idempotent; a supervisor retries,
reroutes, and restores from verified backups.

## How principles are used

- **Ideation** filters and ranks candidate projects against these principles and
  proposes the smallest intervention first.
- **Review gates** (principle 3) turn the safety, provenance, and honest-claims
  obligations into pass / needs-changes / block verdicts with written findings.
- **Governance** changes to this document are proposed as ADRs and tagged with a
  version, so a blessed project can cite the principles it was reviewed under.

## Sources and influences

- [A Solarpunk Manifesto](https://re-des.org/a-solarpunk-manifesto/) — ReDes /
  Regenerative Design
- Adam Flynn, *Solarpunk: Notes toward a manifesto* (Project Hieroglyph, 2014)
- [Designing for Beauty, Sufficiency, and Collective Care](https://jesseturri.com/designing-for-beauty-sufficiency-and-collective-care-part-2b-what-is-solarpunk/)
  — Jesse Turri
- [Appropedia: Solarpunk](https://www.appropedia.org/Solarpunk) — appropriate
  technology, DIY, repair
- [In solarpunk cities of the future, tech follows nature's lead](https://aeon.co/essays/in-solarpunk-cities-of-the-future-tech-follows-natures-lead)
  — Aeon
- [Solarpunk: Refuturing our Imagination](https://www.oneearth.org/solarpunk/) —
  One Earth (Indigenous knowledge, seventh-generation thinking)
- Solarpunk community writing on anarchism, ecology, and justice; mutual aid and
  horizontalism
