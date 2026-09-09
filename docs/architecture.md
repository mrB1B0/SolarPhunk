# Platform Architecture

> **Status:** v0 draft for discussion. Describes the target shape; the repo
> today contains only the agent scaffold (`solarphunk/`).

## Constraints (from the [principles](principles.md))

| Principle | Architectural consequence |
|---|---|
| 1 Hope, made real | Every project run terminates in a reproducible artifact set (BOM, build plan, photos), not just a brief. |
| 2 Sufficiency first | Ideation proposes the smallest intervention first; every design records disassembly and end-of-life paths. |
| 3 Regenerate, don't just spare | Safety + provenance reviews are in the critical path and can block; signed artifacts; every claim linked to evidence. |
| 4 Appropriate, legible technology | Model-agnostic; prefer small/local inference; log compute and energy; every agent output carries its reasoning and sources. |
| 5 Knowledge is a commons | Commons uses open, inspectable, exportable formats; content-addressed; license + provenance per contribution. |
| 6 Nothing radical is out of reach | Build plans state cost / PPE / skill / time; accessibility gaps are surfaced in the review. |
| 7 No chokepoints | Decentralized, offline-first, self-healing; append-only decision log; human checkpoint for irreversible actions; sandboxed least-privilege agents; no vendor lock-in. |

## Layers

```mermaid
flowchart TB
    subgraph IF[Interface]
      CLI[Local CLI / TUI]
      WEB[Local web UI — later]
      FED[Peer federation — later]
    end
    subgraph OR[Orchestration]
      TG[Task graph + human checkpoints]
      DL[(Append-only decision log)]
      RT[Agent runtime — deepagents / LangGraph]
    end
    subgraph AG[Agents]
      PROP[Propose: Scout, Ideator, Designer, Fab Planner, Mentor]
      GATE[Gates: Ecology/Safety, Provenance/Ethics, Security]
      PLAT[Platform: Steward, Curator, Facilitator]
    end
    subgraph KN[Knowledge & policy]
      CM[(Knowledge commons - content addressed)]
      MG[(Material graph + provenance ledger)]
      POL[Policy as code: safety, ecology, ethics, security]
    end
    subgraph INF[Runtime / infra]
      SUP[Self-healing supervisor]
      CKPT[(Job checkpoints - SQLite)]
      SBX[Sandboxed tool execution]
      SEC[Secrets - local, encrypted]
      SCHED[Carbon/energy-aware scheduler]
    end
    IF --> OR --> AG
    AG --> KN
    OR --> INF
    AG --> INF
    GATE --> POL
    PLAT --> CM
```

### Interface
Local CLI/TUI is the v0 control surface (the `solarphunk` command). A local web
UI and opt-in peer federation come later. Federation shares the commons as
signed bundles between peers — no central authority.

### Orchestration
An agent runtime (currently `deepagents` on LangGraph) executes a **task graph**
with explicit human-in-the-loop checkpoints. Every decision — human or agent —
is written to an append-only **decision log**.

### Agents
The roles in [agent-roles.md](agent-roles.md), each a configurable agent with a
**least-privilege** tool grant. Propose-tier agents can only read the commons
and write artifacts; Gate-tier agents can block and sign; Platform-tier agents
run the system and are audited by Security.

### Knowledge & policy
- **Knowledge commons** — content-addressed store of briefs, designs, BOMs,
  build logs, and review artifacts. Local SQLite index; exportable bundles.
- **Material graph** — inventory of materials and parts with condition,
  location, and a link into the **provenance ledger** (append-only, signed).
- **Policy as code** — the gate checks, versioned alongside the principles they
  enforce. A blessed project stores the policy version it passed.

### Runtime / infra
Local-first nodes. The **self-healing supervisor** owns job health: idempotent
steps, checkpoint/resume, retry, reroute around a degraded node, backup and
verify. Tool execution is **sandboxed**. Secrets live in an encrypted local
store, never in the repo. A **carbon/energy-aware scheduler** batches heavy
compute into low-impact windows and prefers cached results.

## Core data model (sketch)

```
Material        id, type, condition, qty, location, provenance_ref
ProvenanceEntry id, subject_ref, source, consent, method, signed_by, ts   (append-only)
Idea            id, intent, materials[], ai_angle, principle_check
ProjectBrief    id, idea_ref, goal, form_intent, constraints, status
Design          id, brief_ref, bom[], models[], tolerances, eol_paths
BuildPlan       id, design_ref, steps[], tools[], ppe, skill, time_est
ReviewArtifact  id, project_ref, kind(ecology|ethics|security), verdict,
                findings[], policy_version, signed_by, ts
Contribution    id, project_ref, author, license, ts
Decision        id, session_ref, actor(human|agent), choice, rationale, ts   (append-only)
Node            id, capabilities, health, last_seen
```

## Cross-cutting

- **Security:** least privilege per agent; signed gate artifacts; append-only
  logs; supply-chain verification of code/models/tools; sandboxed `execute`.
- **Self-healing:** supervised, idempotent jobs; checkpoint/resume; health
  probes; automatic retry and reroute; periodic backup + restore test.
- **Environmental safety of the platform itself:** default to small/local
  models; schedule for low-carbon windows; log energy per job; cache
  aggressively; make the platform's own footprint visible.

## Roadmap

| Phase | Scope |
|---|---|
| **0 — Foundation** | These docs. Agent scaffold. Local SQLite commons + material inventory. Scout + Ideator producing briefs. |
| **1 — Pipeline** | Designer + Fabrication Planner. Ecology/Safety and Provenance/Ethics gates as advisory, then blocking. Human `bless` writes signed artifacts. |
| **2 — Platform** | Steward self-healing, Curator normalisation, Facilitator multi-player sessions, Security audit loop. Local web UI. |
| **3 — Federation** | Signed commons bundles shared between peer nodes; no central service. |
