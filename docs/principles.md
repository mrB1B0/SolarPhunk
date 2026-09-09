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

Each principle has a plain meaning and a **platform obligation** — how the
software is expected to embody or enforce it.

### 1. Salvage first
Every project starts from what already exists: discarded, broken, donor, or
naturally abundant material. Newly extracted or manufactured material is a last
resort and must be named and justified in the project brief.
**Platform obligation:** the material inventory is an input to ideation; a brief
that depends on virgin material is flagged and must carry a written rationale.

### 2. Repair, reuse, regenerate
Prefer designs that extend the life of things, come apart without destruction,
and return their materials to use or safely to nature. No planned obsolescence,
no permanent lamination of dissimilar materials.
**Platform obligation:** designs record disassembly and end-of-life paths; these
are part of the ecology review.

### 3. Appropriate technology
Use the simplest technology that solves the problem. Favour low power, low
complexity, and things a person can maintain in their own workshop. AI is a
tool in service of the work, not the point of it.
**Platform obligation:** default to small/local models and cached results;
heavier compute must be justified per job.

### 4. Open by default
Designs, code, bills of materials, build logs, review artifacts, and failures
are shared under permissive or copyleft licenses. Knowledge is a commons.
**Platform obligation:** contributions are normalised into the shared commons
with a license, provenance, and enough detail to reproduce.

### 5. Local-first and resilient
The platform runs offline, on modest hardware, next to the workbench. It
degrades gracefully and repairs itself. No hard dependency on a central service
or a single vendor.
**Platform obligation:** all core features work with no network; jobs are
resumable; a supervisor retries, reroutes, and restores from backup.

### 6. Ecological safety is a gate, not a feature
Every project passes a hazard and lifecycle review — toxicity, emissions,
energy, e-waste, effect on land and water — before it is "blessed." Projects
that are unsafe or net-harmful are rejected, not shipped with a warning.
**Platform obligation:** the ecology/safety review can block; a blessed project
always carries a signed review artifact.

### 7. Consent and provenance for materials
Materials are tracked to their source. Nothing enters a project through theft,
exploitation, or ecological damage. Respect the land and the people who steward
it, including when harvesting natural materials.
**Platform obligation:** every inventory item has a provenance record; the
provenance/ethics review checks it before design work proceeds.

### 8. Many hands
The platform is multi-player by design. Projects are collaborative;
contribution, credit, and governance are visible to everyone involved.
**Platform obligation:** a facilitator coordinates human and agent
participants, and an append-only decision log records who chose what and why.

### 9. Humans decide
Agents propose; people decide — especially on safety, ethics, and aesthetics.
Automation never removes accountability from a person.
**Platform obligation:** making agents can only produce proposals; blessing,
and any irreversible action, requires a human checkpoint.

### 10. Beauty counts
Solarpunk is hopeful and beautiful. Craft, delight, and how a thing makes
people feel are goals on equal footing with function.
**Platform obligation:** project briefs carry intent for form and feel, not
only specification.

### 11. Care for makers
The safety, health, and cognitive load of the people doing the building are
designed in. Projects are reachable across a range of bodies, budgets, tools,
and skill levels.
**Platform obligation:** build plans state required PPE, ventilation, tools,
skill level, and time honestly.

### 12. Measure honestly
Claims about "green," "circular," or "low-energy" are backed by simple,
auditable evidence. No greenwashing, including about the platform itself.
**Platform obligation:** energy and material claims link to the data behind
them; the platform logs its own compute and energy use.

## How principles are used

- **Ideation** filters and ranks candidate projects against these principles.
- **Review gates** (ecology/safety, provenance/ethics, security) turn the
  starred obligations into pass/fail checks with written findings.
- **Governance** changes to this document are proposed as ADRs and need
  maintainer consensus; the version is tagged so older projects cite the
  principles they were blessed under.
