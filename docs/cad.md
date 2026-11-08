# Editing and regenerating the geometry

Open the Blender file in the case's cad folder. Assembly scenes contain editable meshes, illustrative objects, materials and cameras. The S-60-12 parts scene stores its five printable components at their print origins. For fabrication, use the oriented files in print/.

Each case includes nominal settings in source/parameters_v2.json. Feature dimensions also appear in source/build.py. To regenerate the individual parts, use Blender 4.2 with Python 3.11, NumPy and manifold3d 3.5.4. Use a wheel compatible with your Blender architecture and Python installation. From the case directory:

```sh
python3.11 -m pip install --no-deps --target source/vendor manifold3d==3.5.4
blender --background --python-exit-code 1 --python source/build.py
```

Generated meshes appear in final/stl/. Packaged plate positions and quantities are separate distribution data. The S-60-12 generator builds the enclosure without the commercial reference STEP.

To verify the packaged files from the repository root with Python 3.14:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r tools/requirements.txt
.venv/bin/python tools/verify.py
```

The verifier checks STL solids, 3MF units, area and volume correspondence, color-plate quantities, bed contact and nonoverlapping bounding rectangles within 256 × 256 mm. It also checks SHA256SUMS for the distributed case files. [Automated verification](https://github.com/vluncasu/power-supply-cases/actions)
