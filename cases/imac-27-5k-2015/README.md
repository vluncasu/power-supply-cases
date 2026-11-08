# ARC Slim Grip

Delta ADP-300AF T, iMac 27″ Retina 5K Late 2015. Exterior **190 × 166 × 50 mm**.

![Exterior](renders/exterior.png)

[Vedere interioară](renders/interior.png)

## Imprimare

Plăci pregătite pentru P1S, duză 0,4 mm și strat de 0,20 mm, câte o culoare pe placă. [graphite ×13](print/plates/01-graphite-13.3mf) · [ivory ×11](print/plates/02-ivory-11.3mf)

3MF-urile includ toate exemplarele. Dacă imporți STL-urile, setează cantitățile de mai jos. [Instrucțiuni comune](../../docs/printing.md)

| Piesă STL | Filament | Exemplare |
|---|---|---:|
| [base](print/stl/graphite/01_base_x1.stl) | graphite | 1 |
| [relief-lid](print/stl/ivory/02_relief-lid_x1.stl) | ivory | 1 |
| [lid-screw](print/stl/ivory/03_lid-screw_x4.stl) | ivory | 4 |
| [xy-pcb-support](print/stl/ivory/04_xy-pcb-support_x4.stl) | ivory | 4 |
| [locking-foot](print/stl/graphite/05_locking-foot_x4.stl) | graphite | 4 |
| [pcb-nut](print/stl/graphite/06_pcb-nut_x4.stl) | graphite | 4 |
| [cable-clamp](print/stl/ivory/07_cable-clamp_x2.stl) | ivory | 2 |
| [clamp-screw](print/stl/graphite/08_clamp-screw_x4.stl) | graphite | 4 |
| **Total** | | **24** |

## Proiectare și montaj

Placa Delta are un gabarit nominal estimat de 163 × 132 mm. Proiectul admite până la 164 × 134 mm și componente înalte de 35 mm. Identifică producătorul pe eticheta sursei. Varianta Lite-On apare în cataloage sub același cod de piesă Apple și nu a fost verificată geometric aici.

**De ce are 50 mm înălțime.** Planul plăcii se află la 5,8 mm de fundul exterior. Pentru componente de 35 mm rămân 5 mm până la plafonul situat la 45,8 mm. Rama capacului și cele patru picioare completează înălțimea totală. Sub PCB, față de podeaua de 2,4 mm, sunt nominal 3,4 mm. Verifică separat proeminențele lipiturilor.

![Plan cotat al prinderilor și secțiune verticală](renders/mounting-plan.svg)

| Gaură | X de la stânga (mm) | Y de sus (mm) |
|---|---:|---:|
| A | 12 | 3 |
| B | 160 | 3 |
| C | 5 | 102 |
| D | 158 | 102 |

Coordonatele sunt estimări fotografice cu incertitudine de circa ±2 mm. Diametrul găurilor a fost estimat la 3,5–4 mm. Cele patru suporturi mobile permit reglaj independent în ambele direcții. Strânge ușor picioarele inferioare după aliniere, apoi piulițele PCB pe zonele de montaj. Filetele imprimate sunt personalizate. Dacă PCB-ul se îndoaie sau suportul atinge componente, oprește montajul.

**Ventilație și cabluri.** Cele 44 de fante laterale însumează circa 1.380 mm² în CAD. Șicanele interioare lasă pasaje de circa 1.040 mm². Debitul și temperatura în sarcină rămân nemăsurate. Intrarea și ieșirea sunt pe capete opuse. Fiecare bridă prinde mantaua unui cablu rotund. Verificările de interferență acoperă Ø4, 6, 8, 10 și 12 mm. Cablurile vizibile în randări ilustrează Ø12 mm.

Capacul se imprimă **cu relieful în sus**. Șuruburile stau pe cap, suporturile pe talpa pătrată, piulițele pe o față și bridele cu nervurile în sus. La montaj, întoarce bridele cu nervurile către manta. Strânge alternativ cele două șuruburi ale fiecărei bride.

**Justificarea reliefului.** Capacul folosește 20 de suprafețe curbe cu relief de 1,2 mm. Volumul solid cumulat al celor 24 de piese este 249,93 cm³, față de 374,03 cm³ pentru revizia SCULPT. Reducerea calculată este de 33,18%. Consumul și durata efective depind de feliere. [Comparația CAD](validation/comparison.json)

Apple identifică sistemul ca iMac17,1. Catalogul Beetstech asociază codul Apple 661-03524 cu sursa de 300 W și codurile Delta ADP-300AF T și Lite-On PA-1311-2A. Aceste referințe stabilesc identitatea piesei. Cotele de mai sus provin din estimările proiectului. [Apple, identificarea modelului](https://support.apple.com/en-gb/108054) · [Beetstech, catalogul sursei](https://beetstech.com/product/imac-27-inch-a1419-300w-power-supply-661-03524)

[Fișier Blender](cad/assembly.blend) · [Generatorul geometriei](source/build.py) · [Rapoarte CAD](validation/) · [Metodă și limite](../../docs/method.md)
