# Modify a part

| Goal | File to open | What can be edited |
|---|---|---|
| Move a wall face, change a slot or add a recess | **cad/edit-parts.blend** | One mesh object per printable part, laid out side by side and grouped by filament color. Flat regions are simplified where the mesh checks allow it. |
| Inspect component positions and clearances | **cad/assembly.blend** | The assembled scene with reference objects where available. For AURA S-60-12, use the interior and exploded views and cad/parts.blend for the original part geometry. |
| Adjust the printed cable clamp numerically | **cad/cable-clamp.FCStd** | A native FreeCAD feature tree with plate, corner rounds, two clearance holes and three rounded ribs. |
| Modify the lid in a STEP-capable CAD application | **cad/lid.step** | A closed boundary-representation solid reconstructed from the printable lid. Curved and sculpted regions retain facets. |
| Use the clamp as a solid in another mechanical CAD application | **cad/cable-clamp.step** | One solid in STEP AP214 with planar and curved faces. The FreeCAD file retains the dimension controls. |
| Print an original part or replace a single screw | **print/stl/** or **print/plates/** | Millimeter STL files contain one part each. The 3MF plates include all copies in print orientation. |

## Edit a housing or lid in Blender

1. Open **cad/edit-parts.blend** in Blender 4.2 or later and save a working copy. Objects are named with the same numeric IDs as the STL files. The body is on the left, the lid on the right and the hardware below. The custom properties record the distributed STL path and required quantity.
2. Select the part in the Outliner and use **Frame Selected**. Use **Tab → Edit Mode → Face Select** for local changes. For example, select a flat exterior region, inset it and extrude a shallow recess for a label. Measure the remaining wall thickness before exporting. Holding a nominal wall at 2.4 mm and removing 0.4 mm leaves 2.0 mm locally.
3. Keep the mating geometry in mind. Moving a lid post also requires moving the matching lid hole. Preserve the screw pitch and the clearance between mating threads. Recheck the supply envelope, vents and cable path where the change approaches them.
4. Return to Object Mode, duplicate the finished part and set the duplicate's location to **0, 0, 0** to remove the display-layout offset. Export the selected duplicate as STL with **Selection Only**, scale **1.0** and **Scene Unit** disabled. Each model coordinate already represents one millimeter. Check the resulting bounding box in the slicer before printing.
5. Use the original plate as an orientation reference. Replace the intended part and set its quantity from the bill of materials. An edited STL does not automatically update the supplied 3MF plate.

## Edit the clamp in FreeCAD

Open the case-specific **cable-clamp.FCStd** file. Select **Dimensions**, open the **Data** tab and expand the **Dimensions** group. Save a copy before changing a value.

| Property | Default | Mechanical effect |
|---|---|---|
| Width | 10 mm for ARC and S-60-12, 8.8 mm for Compact and Suncronizer | Changes the plate width about its centerline |
| HoleSpacing | 22 mm | Sets the distance between screw axes, moving them symmetrically |
| HoleDiameter | 7 mm | Changes both screw clearance holes together |
| RibSpacing | 3 mm or 2.8 mm, depending on the case | Locates the two outer ribs relative to the center rib |

A checked example is changing **HoleDiameter from 7.0 to 7.2 mm** and recomputing. Both holes grow by 0.1 mm radially while their centers stay fixed. Select **Body** to export the finished solid to STEP or STL. If you change HoleSpacing, the printed body's clamp posts must match the new spacing. Actual jacket retention still requires a physical test.

For local changes to the lid, import **lid.step** as a solid and use a planar face or a datum plane to sketch a cut. Check the result with the original plate and lid screws. Detailed curved surfaces and threads can have many faces in a mesh-derived solid. For global changes to the sculpted relief, the Blender part layout is generally more convenient. Body and threaded fastener geometry is delivered in Blender and STL. The clamp STEP uses analytic surfaces. The nominal surfaces of the FreeCAD clamp use analytical cylinders and fillets; the print meshes approximate those curves with facets. For the distributed dimensions, solid volumes agree within 0.05%.

## Distribution checks

The verification workflow checks printed part quantities, geometry, bed contact, plate spacing and SHA-256 hashes. Run it locally with Python 3.14:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r tools/requirements.txt
.venv/bin/python tools/verify.py
```

[Print setup](printing.md) · [Dimensions and allowances](dimensions.md) · [Verification limits](method.md)
