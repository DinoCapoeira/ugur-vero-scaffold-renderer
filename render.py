import json
import argparse
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# Argument parser for command-line options
parser = argparse.ArgumentParser(description="3D Scaffold Renderer")
parser.add_argument("-f", required=True, help="Input JSON file")
parser.add_argument("-o", help="Output JSON file")
parser.add_argument("--highlight", dest="highlight", help="Highlight part name")
parser.add_argument("-b", action="store_true", help="Only render ScaffoldingBox parts")
parser.add_argument("-tx", type=float, default=0.0, help="Translate along X")
parser.add_argument("-ty", type=float, default=0.0, help="Translate along Y")
parser.add_argument("-tz", type=float, default=0.0, help="Translate along Z")
parser.add_argument("-rz", type=float, default=0.0, help="Rotate around Z axis (degrees)")
parser.add_argument("-vo", action="store_true", help="Use orthographic view")
view = parser.add_mutually_exclusive_group()
view.add_argument("-vx", action="store_true", help="Camera along +X")
view.add_argument("-vy", action="store_true", help="Camera along +Y")
view.add_argument("-vz", action="store_true", help="Camera along +Z (top)")
parser.add_argument("-p", action="store_true", help="Show processing time")
args = parser.parse_args()

start = time.time()

# Load input JSON data
with open(args.f, "r") as f:
    data = json.load(f)

parts = data["parts"]
if args.b:
    parts = [p for p in parts if p["name"] == "ScaffoldingBox"]

# Create global transformation matrix
theta = math.radians(args.rz)
Rz = np.array([
    [math.cos(theta), -math.sin(theta), 0],
    [math.sin(theta),  math.cos(theta), 0],
    [0,               0,                1]
])
T = np.array([args.tx, args.ty, args.tz])

transformed = []

# Setup matplotlib 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
if args.vo:
    ax.set_proj_type("ortho")
if args.vx:
    ax.view_init(elev=0, azim=-90)
elif args.vy:
    ax.view_init(elev=0, azim=180)
elif args.vz:
    ax.view_init(elev=90, azim=-90)

# Process and draw each part
for part in parts:
    mat = np.array(part["ecsBox"]).reshape(4, 4)
    R = mat[:3, :3]
    t = mat[:3, 3]
    R_new = Rz @ R
    t_new = Rz @ t + T
    M_new = np.eye(4)
    M_new[:3, :3] = R_new
    M_new[:3, 3] = t_new

    transformed.append({
        "name": part["name"],
        "ecsBox": [round(x, 6) for x in M_new.flatten()],
        "width": part["width"],
        "depth": part["depth"],
        "height": part["height"]
    })

    # Define box corner points in local coordinates
    w, d, h = part["width"], part["depth"], part["height"]
    box = np.array([
        [w/2,  d/2,  h/2, 1], [-w/2,  d/2,  h/2, 1],
        [-w/2, -d/2,  h/2, 1], [w/2, -d/2,  h/2, 1],
        [w/2,  d/2, -h/2, 1], [-w/2,  d/2, -h/2, 1],
        [-w/2, -d/2, -h/2, 1], [w/2, -d/2, -h/2, 1]
    ])
    box_world = (M_new @ box.T).T

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    color = "red" if args.highlight == part["name"] else "black"
    lw = 2 if args.highlight == part["name"] else 1

    for i, j in edges:
        xs = [box_world[i][0], box_world[j][0]]
        ys = [box_world[i][1], box_world[j][1]]
        zs = [box_world[i][2], box_world[j][2]]
        ax.plot(xs, ys, zs, color=color, linewidth=lw)

# Save updated JSON output if requested
if args.o:
    with open(args.o, "w") as out:
        json.dump({"parts": transformed}, out, indent=4)
    print(f"Output saved to: {args.o}")

# Show processing time
if args.p:
    print(f"{time.time() - start:.6f} sec")

# Finalize and display plot
plt.title("3D Scaffold Renderer")
ax.set_box_aspect([1, 1, 1])
plt.tight_layout()
plt.show()
