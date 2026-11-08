# AURA Compact 160

A metal-cased supply estimated at 110 × 98–100 × 35–36 mm from photographs. Assembled exterior **160 × 124 × 48.8 mm**.

**[Download the P1S print kit](https://github.com/vluncasu/power-supply-cases/releases/latest/download/aura-compact-160-print.zip)** · [Compare supply dimensions](../../docs/dimensions.md)

| Closed enclosure | Opposite end |
|---|---|
| ![Closed enclosure](renders/exterior.png) | ![Rear three-quarter view](renders/rear.png) |
| **Lid removed** | **Exploded assembly** |
| ![Metal housing envelope and independent cable clamps](renders/interior.png) | ![Lid and fasteners lifted from the body](renders/exploded.png) |

Metal housing envelope and independent cable clamps. The exploded view lifts the lid and its fasteners to show their relationship to the body.

## Edit the design

[Complete CAD kit](https://github.com/vluncasu/power-supply-cases/releases/latest/download/aura-compact-160-cad.zip) · [Edit all parts in Blender](cad/edit-parts.blend) · [Parametric clamp](cad/cable-clamp.FCStd) · [Clamp STEP](cad/cable-clamp.step) · [Lid STEP](cad/lid.step)

Open the Blender parts file to select an individual body, lid or fastener. Use the Dimensions object in FreeCAD to change the clamp width or screw clearances. [Step-by-step editing and STL export](../../docs/cad.md)

## Print on a Bambu Lab P1S

Designed for the **256 × 256 mm P1S bed, 0.4 mm nozzle, 0.20 mm Strength profile and supports disabled**. Each geometric 3MF contains all copies for one filament color. [Black plate (5 pieces)](print/plates/01-black-5.3mf) · [White plate (9 pieces)](print/plates/02-white-9.3mf)

Print the lid exterior face down. Place the body on its floor, screws on their heads and clamps flat side down. The separate STL files each contain one part. Use the quantities below when importing them individually. [Slicer setup and first-layer checks](../../docs/printing.md)

| Individual STL | Color | Quantity |
|---|---|---:|
| [Body](print/stl/black/01_body_x1.stl) | Black | 1 |
| [Wave lid](print/stl/white/02_wave-lid_x1.stl) | White | 1 |
| [Lid screw](print/stl/white/03_lid-screw_x4.stl) | White | 4 |
| [Cable clamp](print/stl/white/04_cable-clamp_x2.stl) | White | 2 |
| [Clamp screw](print/stl/black/05_clamp-screw_x4.stl) | Black | 4 |
| [Hold down screw](print/stl/white/06_hold-down-screw_x2.stl) | White | 2 |
| **Total** | | **14** |

### Fit and assembly

The estimated metal housing is **110 × 98–100 × 35–36 mm**. Length has the greatest uncertainty. CAD checks use two envelopes, 110 × 100 × 36 mm and **112 × 102 × 38 mm**. Allow for any terminals or screw heads projecting beyond the metal housing. The adjustable hold-down screws may raise the total height to **50.8 mm** with the tallest unit.

The compact layout reduces the footprint by 18.3% compared with the earlier 184 × 132 mm body. The maximum PSU envelope leaves approximately **13.7 mm at the terminal end** before the cable saddle. The DC corridor narrows to about **5.2 mm** beside the guides. Check the actual cable bend along the whole route. [CAD comparison](validation/comparison.json)

Place the metal-cased unit on the supports with its terminals toward the input. Fit both cable clamps and the four peripheral lid screws. The two short screws beside the lid vents take up vertical play. Their nominal contact points are X = ±48 mm and Y = −2 mm from the case center. Use them only where both tips meet solid housing metal. Mounting-hole spacing was estimated at 75–80 mm and was not used as a fixing datum.

The gray interior block represents the estimated housing envelope. Confirm wall clearance, contact points and cable retention on the physical assembly.

[Editable Blender file](cad/assembly.blend) · [CAD reports](validation/) · [Evidence and limitations](../../docs/method.md)
