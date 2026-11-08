# Metodă și domeniul rezultatelor

| Model | Originea datelor geometrice | Verificare efectuată | Necunoscut relevant înainte de montaj |
|---|---|---|---|
| ARC Slim Grip | Cote estimate din fotografii pentru placa Delta | Verificări CAD ale deplasării suporturilor și îmbinărilor filetate | Pozițiile reale ale găurilor și înălțimea lipiturilor |
| AURA Compact 160 | Gabarit exterior estimat de utilizator | Două volume dreptunghiulare de control și reglajul prinderilor | Zonele solide de contact și raza de curbură a cablului |
| AURA S-60-12 | Model STEP furnizat pentru proiect, 44 de solide | Intersecția carcasei imprimate cu modelul de referință | Abaterile unității fizice față de STEP |
| Suncronizer | Gabarit estimat pentru sursă și volum rezervat convertitorului | Intersecția carcasei cu cele două volume | Modelul convertitorului, găurile PCB și fixarea |

## Interpretarea rapoartelor

Un volum comun nul în configurația verificată exclude o coliziune geometrică în acea poziție, în limita preciziei numerice. Valorile reziduale foarte mici pot apărea la suprafețe tangente. Condiția nu descrie frecarea în filet, contracția plasticului sau comportamentul sub sarcină. Verificările de cablu folosesc geometrii rigide. Pentru iMac, geometria fantei și a șicanei descrie o cale posibilă pentru aer. Debitul necesită condiții termice și măsurători.

Volumele comparative provin din geometria solidă și includ multiplicarea pieselor. Un slicer calculează materialul după perimetre, umplere, capace și trasee. Datele de aici nu susțin o estimare experimentală a consumului sau a duratei.

## Identificarea sursei iMac

Apple asociază iMac17,1 cu iMac Retina 5K de 27″ Late 2015. Beetstech asociază sistemul A1419 și codul 661-03524 cu surse Delta și Lite-On de 300 W. Punctele de montaj și cotele de gabarit au fost estimate separat pentru varianta Delta. [Apple Support](https://support.apple.com/en-gb/108054) · [Beetstech](https://beetstech.com/product/imac-27-inch-a1419-300w-power-supply-661-03524)

Pentru manipularea sursei deschise, ghidul iFixit descrie riscul contactului cu condensatoarele. Verificarea CAD nu stabilește că o incintă din PLA protejează o sursă alimentată la rețea. Folosește modelele pentru evaluare mecanică fără tensiune. Validarea unei instalații alimentate implică verificări separate privind izolarea, protecția la atingere, împământarea unde este aplicabilă, retenția cablului și temperatura. [iFixit, înlocuirea sursei iMac 27″ Retina 5K](https://www.ifixit.com/Guide/iMac+Intel+27-Inch+Retina+5K+Display+Power+Supply+Replacement/30530)

Rapoartele JSON din fiecare director validation păstrează numele fișierelor originale ale proiectării. Fișierul print/manifest.json identifică fiecare piesă prin același prefix numeric și precizează numele distribuit, culoarea și cantitatea. Scriptul tools/verify.py verifică pachetul pregătit pentru publicare.
