# Printing on the Bambu Lab P1S

All four case kits are designed for a **Bambu Lab P1S with a 256 × 256 mm plate and a 0.4 mm nozzle**. Each color has its own arranged 3MF. The intended setup is PLA, the **0.20 mm Strength** process and supports disabled. These files have passed digital bed-layout checks. Physical printing remains untested.

[Compare the four assembled cases and their interiors](../README.md)

1. Identify the supply and check its dimensions, terminal projections and cable route against the [fit guide](dimensions.md).
2. Download the matching print kit from [Releases](https://github.com/vluncasu/power-supply-cases/releases/latest) and extract it. Open one file from the plate folder at a time. For direct downloads from GitHub file pages, use **Download raw file**.
3. In your slicer select the P1S, 0.4 mm nozzle, build surface and actual filament. Import the plate at 100% in millimeters. The 3MF stores the geometry and copy counts. Select the process in the slicer and generate toolpaths locally.
4. Preserve the supplied orientation. Check that every object starts on the bed and preview the short bridges in the screwdriver slots, head recesses and threaded parts. Check clear space before adding a brim.
5. Print one plate per color. Change the spool between plates. The supplied layout needs no in-print color change. For replacements, each individual STL contains one part. Its xN suffix specifies the quantity for one complete enclosure.
6. Use the model-specific assembly order. Bring printed screws up gently by hand and check fit with an unpowered assembly.

| Case | Lid on the print bed | Plate 1 | Plate 2 |
|---|---|---:|---:|
| [Delta iMac 27″ Late 2015 Power Supply](../cases/imac-27-5k-2015/) | Flat underside on bed, sculpted face up | 13 graphite | 11 ivory |
| [AURA S-60-12](../cases/aura-s60/) | Exterior face down | 5 graphite | 7 ivory |
| [AURA Compact 160](../cases/aura-compact-160/) | Exterior face down | 5 black | 9 white |
| [Suncronizer](../cases/suncronizer/) | Engraved face down, skirt up | 5 black | 7 green |

Bodies print floor-down, screws head-down and cable clamps flat-side-down. Installed clamps face the jacket with their rounded ribs. For ARC, print the PCB shoes on the square bases and the nuts on a flat face. Separate printed hardware from different kits by model, even where the parts look similar.
