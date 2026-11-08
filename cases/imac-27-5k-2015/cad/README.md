# Editable case files

| Open this file | Purpose |
|---|---|
| [edit-parts.blend](edit-parts.blend) | All printable parts in a single layout. Select by name or filament collection. |
| [assembly.blend](assembly.blend) | Placement reference with assembled components and render cameras. |
| [cable-clamp.FCStd](cable-clamp.FCStd) | Native FreeCAD clamp with dimensions and a Part Design feature tree. |
| [lid.step](lid.step) | Full lid solid in millimeters. Planar regions are merged where possible and curved regions retain mesh facets. |
| [cable-clamp.step](cable-clamp.step) | Exchange the finished clamp as a single AP214 solid. |

This case uses a **34 × 10 mm** clamp, a 3 mm plate, 22 mm screw spacing and 7 mm clearance holes. Three rounded ribs add 0.3 mm at their peaks. In FreeCAD, select **Dimensions** and expand the **Data** properties to change the fit.

The distributed Blender working file was reopened and each individual mesh exported back to STL at the origin. The resulting meshes were checked against the production STL for bounding box, solid volume, surface area and connectedness. The FreeCAD clamp was recomputed with a 7.2 mm trial hole and its original STEP export reopened as one solid.

[Modification and export guide](../../../docs/cad.md) · [Case dimensions and assembly](../README.md) · [Print plates and individual STL files](../print/)
