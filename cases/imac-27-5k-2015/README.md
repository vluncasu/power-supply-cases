# Delta iMac 27″ Late 2015 Power Supply

![Open iMac enclosure with the lid and four lid screws beside the base](renders/delta-imac-27-2015-power-supply-case.png)

Enclosure for the **Delta ADP-300AF T**, the 300 W power supply in the 27-inch Retina 5K iMac (Late 2015). The board mounts on four adjustable shoes. The finished case measures **190 × 166 × 50 mm**, including the feet.

[Print ZIP](https://github.com/vluncasu/power-supply-cases/releases/latest/download/imac-27-5k-2015-print.zip) · [CAD + print ZIP](https://github.com/vluncasu/power-supply-cases/releases/latest/download/imac-27-5k-2015-cad.zip) · [Graphite plate ×13](print/plates/01-graphite-13.3mf) · [Ivory plate ×11](print/plates/02-ivory-11.3mf)

| Bare base | Interior with supports and clamps |
|---|---|
| ![Bare enclosure floor](renders/base.png) | ![Fitted base](renders/interior.png) |

Four printed feet lock the sliding PCB supports from below. The raised strips along the sidewalls shield the vent openings. Each end has a saddle and two threaded posts for the cable clamp.

### How the iMac board is held

| Lid post | Board mount | Cable saddle |
|---|---|---|
| ![Lid screw aligned with the lid recess and corner post](renders/lid-post.png) | ![Nut, sliding shoe, floor and locking foot](renders/pcb-mount.png) | ![Two screws, clamp and cable saddle](renders/cable-saddle.png) |

The **locking foot (05)** threads into the shoe from beneath the floor. Align all four shoes before tightening the feet. The PCB mounting ring sits between the shoe shoulder and **nut (06)**. The gaps in these exploded views are enlarged for visibility.

| Lid screw · 03 | Sliding shoe · 04 | Locking foot · 05 |
|---|---|---|
| ![Lid screw](renders/lid-screw.png) | ![Sliding shoe](renders/sliding-shoe.png) | ![Locking foot](renders/locking-foot.png) |
| **PCB nut · 06** | **Cable clamp · 07** | **Clamp screw · 08** |
| ![PCB nut](renders/pcb-nut.png) | ![Cable clamp](renders/cable-clamp.png) | ![Clamp screw](renders/clamp-screw.png) |

Part numbers match the STL filenames. The lid screws have 14 mm heads and 3 mm pitch. The longer clamp screws have 11 mm heads and 1.2 mm pitch. Two screws draw each clamp down onto the cable jacket.

| Closed | Opposite end | Lid removed from posts |
|---|---|---|
| ![Closed case](renders/exterior.png) | ![Rear three-quarter view](renders/rear.png) | ![Exploded enclosure](renders/exploded.png) |

## Edit the design

[Complete CAD kit](https://github.com/vluncasu/power-supply-cases/releases/latest/download/imac-27-5k-2015-cad.zip) · [Edit all parts in Blender](cad/edit-parts.blend) · [Parametric clamp](cad/cable-clamp.FCStd) · [Clamp STEP](cad/cable-clamp.step) · [Lid STEP](cad/lid.step)

Open the Blender parts file to select an individual body, lid or fastener. Use the Dimensions object in FreeCAD to change the clamp width or screw clearances. [Step-by-step editing and STL export](../../docs/cad.md)

## Print on a Bambu Lab P1S

Designed for the **256 × 256 mm P1S bed, 0.4 mm nozzle, 0.20 mm Strength profile and supports disabled**. Each geometric 3MF contains all copies for one filament color. [Graphite plate (13 pieces)](print/plates/01-graphite-13.3mf) · [Ivory plate (11 pieces)](print/plates/02-ivory-11.3mf)

Print the sculpted lid **relief side up**. Set PCB shoes on their square bases, nuts on a flat face, feet and screws on their heads, and clamps with their ribs up. The separate STL files each contain one part. Use the quantities below when importing them individually. [Slicer setup and first-layer checks](../../docs/printing.md)

| Individual STL | Color | Quantity |
|---|---|---:|
| [Base](print/stl/graphite/01_base_x1.stl) | Graphite | 1 |
| [Relief lid](print/stl/ivory/02_relief-lid_x1.stl) | Ivory | 1 |
| [Lid screw](print/stl/ivory/03_lid-screw_x4.stl) | Ivory | 4 |
| [Xy pcb support](print/stl/ivory/04_xy-pcb-support_x4.stl) | Ivory | 4 |
| [Locking foot](print/stl/graphite/05_locking-foot_x4.stl) | Graphite | 4 |
| [Pcb nut](print/stl/graphite/06_pcb-nut_x4.stl) | Graphite | 4 |
| [Cable clamp](print/stl/ivory/07_cable-clamp_x2.stl) | Ivory | 2 |
| [Clamp screw](print/stl/graphite/08_clamp-screw_x4.stl) | Graphite | 4 |
| **Total** | | **24** |

### Board dimensions and mounting coordinates

Identify the supply by its manufacturer label before printing. Apple identifies the host computer as iMac17,1. The supplier lists Apple part 661-03524 for both Delta ADP-300AF T and Lite-On PA-1311-2A supplies. Mechanical fit was studied for the Delta board only. [Apple model identification](https://support.apple.com/en-gb/108054) · [Supplier part record](https://beetstech.com/product/imac-27-inch-a1419-300w-power-supply-661-03524)

The photographic estimate is **163 ± 1 mm long, 132 ± 2 mm wide and 30 ± 5 mm high**. The design envelope allows 164 × 134 mm in plan and 35 mm above the mounting plane. Check the tallest heatsink and the solder joints below the board independently.

The 99 mm dimension is the vertical distance between mounting rows. The 3.4 mm underside gap is measured from the inner floor surface to the PCB support plane.

| Mount | X from left edge (mm) | Y from top edge (mm) |
|---|---:|---:|
| A | 12 | 3 |
| B | 160 | 3 |
| C | 5 | 102 |
| D | 158 | 102 |

The estimated uncertainty is ±2 mm per coordinate. Horizontal hole spacing is 148 mm in the upper row and 153 mm in the lower row. The rows are 99 mm apart vertically. Estimated hole diameters are 3.5–4 mm with an approximately 8 mm outer mounting ring. The four sliding shoes have 3.2 mm printed studs and 9 mm support pads.

### Height, airflow and material

The board plane is 5.8 mm above the exterior floor. The height budget is **5.8 + 35 + 5 = 45.8 mm** to the inner ceiling. The lid frame and feet bring the total to 50 mm. Above the 2.4 mm floor, the nominal underside gap is 3.4 mm. It is a mechanical allowance and requires checking against actual solder projections and electrical requirements.

Two rows of chevron slots feed baffled side passages. The 44 slots have a combined nominal opening of about 1,380 mm². The passages above the baffles provide about 1,040 mm². Airflow and operating temperatures have not been measured. The 20 curved lid tiles rise 1.2 mm above the skin. Total CAD solid volume is 249.93 cm³, a 33.18% reduction from the earlier SCULPT design. Sliced filament use depends on toolpaths. [CAD comparison](validation/comparison.json)

### Assembly sequence

1. Place the four shoes in their guides. Engage the locking feet from beneath and leave them loose enough to align.
2. Check each support against the actual board. Confirm that the underside clears the floor and that each pad contacts only a mounting area. Secure the feet and printed nuts gently. The short printed threads are sensitive to printer tolerances.
3. Place one jacketed cable on each saddle. Turn each clamp ribs-down and tighten its two screws evenly. The entry and exit are on opposite ends. CAD checks cover round jackets of 4, 6, 8, 10 and 12 mm through 12.6 mm ports. The renders illustrate 12 mm cables. Pull-out resistance has not been measured.
4. Fit the lid with its four recessed screws. Keep the side vents clear.

[Editable Blender file](cad/assembly.blend) · [CAD reports](validation/) · [Evidence and limitations](../../docs/method.md)
