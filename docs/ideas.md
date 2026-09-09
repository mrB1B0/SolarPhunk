# Seed Ideas

> **Status:** v0 seed list to prime the Ideator. Add freely. An idea is cheap;
> it becomes a *project* only after it clears the [principles](principles.md)
> filter and the review gates.

Each idea names likely **donor/natural materials** and the **AI angle** — the
part where an agent earns its keep. Difficulty is a rough 1–5.

## Energy & power

| Idea | Materials | AI angle | Diff |
|---|---|---|---|
| Parabolic solar cooker / small kiln | Scratched CDs/DVDs, broken mirror, e-waste reflectors, scrap sheet metal | Compute facet layout and aim from disk sizes; predict stagnation temp | 2 |
| 18650 harvest powerwall | Laptop/tool battery packs, PSU housings | Vision + IR grading of salvaged cells from photos; pack topology + BMS plan; **mandatory safety review** | 4 |
| Washing-machine-motor micro wind/hydro | Donor BLDC motor, bike wheel, pipe offcuts | Match motor curve to local wind/flow data; generate rectifier + charge-control BOM | 3 |
| Pedal-power workshop hub | Car alternator, flywheel from brake disc, bike frame | Model flywheel energy vs. tool draw; size the drivetrain | 3 |

## Tools & machines

| Idea | Materials | AI angle | Diff |
|---|---|---|---|
| Bike-part low-precision CNC / plotter | Donated drivetrains, drawer slides, steppers from printers | Measure backlash, emit GRBL config; adapt toolpaths to slop | 4 |
| PET-bottle filament extruder | PET bottles, donor stepper, toaster heating element | Closed-loop diameter control; tune temp/pull from a cheap sensor | 3 |
| Loom from bed frames + bike wheels | Steel bed rails, spokes, salvaged cord | Generate weave drafts and a cut list from a photo of the scrap pile | 2 |
| Field-repair oracle | (software + your parts bin) | Point phone at a broken appliance; propose fixes using parts you already have | 3 |

## Art & sound

| Idea | Materials | AI angle | Diff |
|---|---|---|---|
| Kinetic sound sculpture | HDD voice-coils, stepper motors, relays | Compose for and drive salvaged actuators as instruments | 2 |
| Living pigments & bioplastics notebook | Kitchen/garden waste, foraged minerals | Guide recipes, log reproducibility, predict colour-fastness | 2 |
| Reclaimed-glass light installation | Broken window/bottle glass, LED strips from signage | Optimise cut/arrangement for a target caustic pattern | 3 |

## Habitat, water & growing

| Idea | Materials | AI angle | Diff |
|---|---|---|---|
| Rain/greywater irrigation controller | Reflashed old router or SBC, salvaged valves | Schedule from weather + soil sensors; run on constrained hardware | 3 |
| Salvaged-glass solar still / desalinator | Broken windows, scrap timber, food-safe liner | Optimise geometry for local sun angle and yield | 2 |
| Pollinator habitat + monitor | Drilled scrap hardwood, donor webcam | Edge model IDs visitors; suggests habitat tweaks | 2 |
| Bottle-cap anemometer / weather station | Bottle caps, reed switches, magnet, old phone | Auto-calibrate against nearby public stations | 2 |

## Assistive & everyday

| Idea | Materials | AI angle | Diff |
|---|---|---|---|
| Donor-material assistive device fitter | Open assistive-device designs, salvaged plastics/metal | Adapt a published design to donor stock and a body scan | 4 |
| Cob / earthbag structure planner | Site soil, reclaimed windows and doors | Size a small structure from a soil test + a salvaged-openings inventory | 3 |

## Platform primitives (ideas that make other ideas easier)

- **E-waste teardown catalog** — a shared, agent-maintained reference: "what
  useful parts are inside this common discarded device, and what they're worth
  in a build." Feeds the Scout and Designer agents directly.
- **Salvaged-part variance library** — measured tolerances and failure modes of
  common donor components, so Designer agents can plan around real-world slop.
- **Local material map** — opt-in, privacy-respecting index of who has what
  scrap to share.

## Idea template

```
### <name>
- **Problem / intent:** what it does, and the form/feel it's going for
- **Materials:** donor and natural sources, with substitutes
- **AI angle:** the specific judgement or computation an agent provides
- **Principle check:** salvage-first? end-of-life path? maker safety? honest claims?
- **Unknowns / risks:** what could make this unsafe, wasteful, or not work
```
