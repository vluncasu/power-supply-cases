# Evidence and verification limits

| Design | Dimensional input | Digital check | Physical question |
|---|---|---|---|
| Delta iMac 27″ Late 2015 Power Supply | Photographic estimates of the Delta PCB | Mount travel, mating threads and isolated cable clamps | Actual hole coordinates, solder clearance and jacket retention |
| AURA S-60-12 | Supplied STEP assembly with 44 solids | Interference between enclosure parts and the reference metal supply | Production unit variation |
| AURA Compact 160 | Estimated metal housing dimensions | Two rectangular envelopes and adjustable hold-downs | Solid contact points and full cable bend |
| Suncronizer | Estimated supply and provisional converter size | Separation of two reserved volumes from body and lid | Converter selection, PCB mounting and water protection |

A zero common volume in a modeled position indicates no volumetric collision at the calculation precision. Near-zero residuals can occur at tangent faces. Friction, printer tolerances, thread strength and cable pull-out force require measurements. Cable checks use rigid local representations. Clearance at the port does not establish a viable route to the terminals.

Reported material comparisons sum CAD solid volumes multiplied by part quantities. Filament and print time depend on the slicer, wall count, infill, speeds and generated toolpaths. Slot and baffle areas describe geometry. Airflow and temperature under load were not measured.

## Mains and environmental limits

The iMac supply is an exposed mains assembly. Capacitors can retain charge after disconnection. Use the models for unpowered mechanical evaluation. Operation requires assessment of electrical isolation, access to live parts, protective earth where applicable, cable retention, temperatures and material suitability. Suncronizer is an unpowered demo with open ports and no assigned ingress rating. [iFixit power supply removal guide](https://www.ifixit.com/Guide/iMac+Intel+27-Inch+Retina+5K+Display+Power+Supply+Replacement/30530)

## Distribution checks

Each case includes JSON design reports and a print manifest recording the part ID, quantity, color and distribution path. The repository verifier reads the delivered STL and 3MF geometry, checks plate contents and compares published file hashes. [Verification script](../tools/verify.py) · [How to run it](cad.md)
