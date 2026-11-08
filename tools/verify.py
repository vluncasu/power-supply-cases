"""Check the distribution against the BOM and the geometry of each print plate."""
import hashlib
import json
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

import numpy as np
import trimesh

ROOT = Path(__file__).resolve().parents[1]
NS = {"m": "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"}


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def verify_case(directory):
    """Compare each plate with its STL bill of materials in millimeters."""
    manifest = json.loads((directory / "print/manifest.json").read_text())
    meshes = {}
    for part in manifest["parts"]:
        mesh = trimesh.load_mesh(directory / part["file"], process=True)
        require(mesh.is_volume and len(mesh.split()) == 1, part["file"])
        require(abs(mesh.bounds[0, 2]) < 0.01, part["file"])
        meshes[part["id"]] = mesh
    for plate in manifest["plates"]:
        path = directory / plate["file"]
        with ZipFile(path) as archive:
            require(archive.testzip() is None, str(path))
            model = ET.fromstring(archive.read("3D/3dmodel.model"))
        require(model.get("unit") == "millimeter", str(path))
        objects = {o.get("id"): o for o in model.findall(".//m:object", NS)}
        counts = Counter()
        footprints = []
        for item in model.findall("m:build/m:item", NS):
            obj = objects[item.get("objectid")]
            part_id = int(obj.get("name")[:2])
            counts[part_id] += 1
            vertices = np.array([[float(v.get(k)) for k in "xyz"] for v in obj.findall(".//m:vertex", NS)])
            faces = np.array([[int(f.get(k)) for k in ("v1", "v2", "v3")] for f in obj.findall(".//m:triangle", NS)])
            # A 3MF build item can translate or rotate its mesh on the plate.
            if item.get("transform"):
                matrix = np.fromstring(item.get("transform"), sep=" ").reshape(4, 3)
                vertices = vertices @ matrix[:3] + matrix[3]
            mesh = trimesh.Trimesh(vertices, faces, process=False)
            original = meshes[part_id]
            require(np.isclose(mesh.volume, original.volume, rtol=2e-4), obj.get("name"))
            require(np.isclose(mesh.area, original.area, rtol=2e-4), obj.get("name"))
            lo, hi = mesh.bounds
            require(abs(lo[2]) < 0.01 and lo[:2].min() >= 0 and hi.max() <= 256, obj.get("name"))
            for lower, upper in footprints:
                overlap = np.minimum(hi[:2], upper) - np.maximum(lo[:2], lower)
                require(not (overlap > 0.01).all(), f"Footprint overlap in {path.name}")
            footprints.append((lo[:2], hi[:2]))
        expected = {p["id"]: p["quantity"] for p in manifest["parts"] if p["color"] == plate["color"]}
        require(counts == expected and counts.total() == plate["quantity"], f"BOM mismatch in {path}")
    return sum(p["quantity"] for p in manifest["parts"])


if __name__ == "__main__":
    for directory in sorted((ROOT / "cases").iterdir()):
        print(f"{directory.name}: {verify_case(directory)} pieces verified", flush=True)
    for line in (ROOT / "SHA256SUMS").read_text().splitlines():
        digest, name = line.split("  ", 1)
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name)
