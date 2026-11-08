# Editare și reproducere

Deschide fișierul Blender din directorul cad al carcasei. Scenele includ geometriile editabile și, pentru ansambluri, obiectele ilustrative. Pentru imprimare folosește fișierele din print/. Fiecare carcasă are propriile cote în source/parameters_v2.json și propriul generator în source/build.py. Unele dimensiuni de detaliu se află direct în generator.

Generatorul folosește Blender 4.2 cu Python 3.11, NumPy și manifold3d 3.5.4. Instalează manifold3d pentru platforma și versiunea Python ale Blender. Un director source/vendor local este acceptat de generator. Pe o instalare cu Python 3.11 compatibil, din directorul carcasei:

```sh
python3.11 -m pip install --no-deps --target source/vendor manifold3d==3.5.4
blender --background --python-exit-code 1 --python source/build.py
```

Blender scrie geometriile individuale în final/stl/. Cantitățile și aranjarea plăcilor distribuite sunt descrise în print/manifest.json. Regenerarea geometriei și alegerea culorilor sunt operațiuni independente. Pentru S-60-12, generatorul include doar geometria pieselor imprimate. Fișierul STEP original nu este necesar pentru regenerare.

Din rădăcina depozitului, verificarea distribuției se poate rula separat cu Python 3.14:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r tools/requirements.txt
.venv/bin/python tools/verify.py
```

Verificarea citește STL-urile și XML-ul din plăcile 3MF. Controlează volumele și ariile pieselor, cantitățile pe culori, atingerea planului patului și lipsa suprapunerilor între dreptunghiurile care încadrează piesele. Ultima etapă compară amprentele SHA-256 ale fișierelor distribuite.
