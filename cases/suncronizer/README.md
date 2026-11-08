# Suncronizer

Machetă pentru sursă 104 × 58 × 26 mm și convertitor 12 V → 5 V. Exterior **164 × 116 × 39,8 mm**.

![Exterior](renders/exterior.png)

[Vedere interioară](renders/interior.png)

## Imprimare

Plăci pregătite pentru P1S, duză 0,4 mm și strat de 0,20 mm, câte o culoare pe placă. [black ×5](print/plates/01-black-5.3mf) · [green ×7](print/plates/02-green-7.3mf)

3MF-urile includ toate exemplarele. Dacă imporți STL-urile, setează cantitățile de mai jos. [Instrucțiuni comune](../../docs/printing.md)

| Piesă STL | Filament | Exemplare |
|---|---|---:|
| [body](print/stl/black/01_body_x1.stl) | black | 1 |
| [solar-lid](print/stl/green/02_solar-lid_x1.stl) | green | 1 |
| [lid-screw](print/stl/green/03_lid-screw_x4.stl) | green | 4 |
| [cable-clamp](print/stl/green/04_cable-clamp_x2.stl) | green | 2 |
| [clamp-screw](print/stl/black/05_clamp-screw_x4.stl) | black | 4 |
| **Total** | | **12** |

## Proiectare și montaj

Machetă mecanică pentru prezentarea unui sistem de urmărire a soarelui, destinată expunerii fără alimentare la rețea. În interior sunt rezervate 110 × 65 × 32 mm pentru sursă și 50 × 30 × 20 mm pentru un convertitor ales ulterior. Pozițiile găurilor și prinderile PCB rămân de stabilit după componentele reale.

Cele 32 de raze sunt gravate în capacul plin. Marginea lui suprapune corpul pe aproximativ 5 mm. Porturile sunt deschise și carcasa nu are garnitură sau clasă IP. Păstrează macheta cu electronica ferită de ploaie.

Așază machetele componentelor în cele două zone, prinde cablurile demonstrative în bride și montează capacul cu cele patru șuruburi verzi. Imprimă capacul cu exteriorul pe pat, șuruburile pe cap și bridele pe fața plată.

[Fișier Blender](cad/assembly.blend) · [Generatorul geometriei](source/build.py) · [Rapoarte CAD](validation/) · [Metodă și limite](../../docs/method.md)
