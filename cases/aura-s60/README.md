# AURA S-60-12

The metal S-60-12 supply represented by the supplied 86 × 58.02 × 33.02 mm STEP assembly. Assembled exterior **148 × 88 × 42.8 mm**.

**[Download the P1S print kit](https://github.com/vluncasu/power-supply-cases/releases/latest/download/aura-s60-print.zip)** · [Compare supply dimensions](../../docs/dimensions.md)

| Closed enclosure | Opposite end |
|---|---|
| ![Closed enclosure](renders/exterior.png) | ![Rear three-quarter view](renders/rear.png) |
| **Lid removed** | **Exploded assembly** |
| ![Support pads, stops and clamps inside the empty enclosure](renders/interior.png) | ![Lid and fasteners lifted from the body](renders/exploded.png) |

Support pads, stops and clamps inside the empty enclosure. The exploded view lifts the lid and its fasteners to show their relationship to the body.

## Edit the design

[Complete CAD kit](https://github.com/vluncasu/power-supply-cases/releases/latest/download/aura-s60-cad.zip) · [Edit all parts in Blender](cad/edit-parts.blend) · [Parametric clamp](cad/cable-clamp.FCStd) · [Clamp STEP](cad/cable-clamp.step) · [Lid STEP](cad/lid.step)

Open the Blender parts file to select an individual body, lid or fastener. Use the Dimensions object in FreeCAD to change the clamp width or screw clearances. [Step-by-step editing and STL export](../../docs/cad.md)

## Print on a Bambu Lab P1S

Designed for the **256 × 256 mm P1S bed, 0.4 mm nozzle, 0.20 mm Strength profile and supports disabled**. Each geometric 3MF contains all copies for one filament color. [Graphite plate (5 pieces)](print/plates/01-graphite-5.3mf) · [Ivory plate (7 pieces)](print/plates/02-ivory-7.3mf)

Print the lid exterior face down. Place the body on its floor, screws on their heads and clamps flat side down. The separate STL files each contain one part. Use the quantities below when importing them individually. [Slicer setup and first-layer checks](../../docs/printing.md)

| Individual STL | Color | Quantity |
|---|---|---:|
| [Body](print/stl/graphite/01_body_x1.stl) | Graphite | 1 |
| [Wave lid](print/stl/ivory/02_wave-lid_x1.stl) | Ivory | 1 |
| [Lid screw](print/stl/ivory/03_lid-screw_x4.stl) | Ivory | 4 |
| [Cable clamp](print/stl/ivory/04_cable-clamp_x2.stl) | Ivory | 2 |
| [Clamp screw](print/stl/graphite/05_clamp-screw_x4.stl) | Graphite | 4 |
| **Total** | | **12** |

### Fit and assembly

The measured STEP envelope, including small projections, is **86 × 58.02 × 33.02 mm**. Those decimals describe the reference geometry. Check the metal housing and terminal location on the physical unit. The original reference contained 44 solids. [Reference interference check](validation/reference_fit.json)

Keep the original metal shell in place and orient the terminals toward the AC end. Four pads support the shell. Stops limit lateral travel, and the closed lid leaves about 0.18 mm nominal vertical play at the upper stops. This small allowance makes actual dimensions and print tolerance particularly important.

Both ports are on opposite ends. The DC route beside the housing was designed for approximately 5–8 mm cable. Secure each jacket with a clamp, check the bend at the terminals, then install the four lid screws. Side intakes and the wavy lid openings provide an air path. Load temperature has not been measured.

The interior view shows the printed supports and both clamps with the reference supply hidden. The editable Blender file contains the five printable parts at their print origins. The supplier STEP is excluded from distribution.

[Editable Blender file](cad/parts.blend) · [CAD reports](validation/) · [Evidence and limitations](../../docs/method.md)
