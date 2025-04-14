# 3D Scaffold Renderer — VERO CAD Task Submission

This repository contains a complete solution for the scaffold rendering task assigned by VERO Digital Solutions. It includes a single Python script that processes a JSON file describing scaffold parts and renders them in 3D using edge-based wireframes. The script supports transformations, filtering, highlighting, exporting, and visualization options.

## 📦 Contents

- `render.py`             – Main Python script
- `sample-scaffold.json`  – Example input JSON (provided by VERO)
- `output.json`           – Transformed output (optional)
- `README.md`             – You are here.

## 🛠️ Requirements

- Python 3.7+
- NumPy
- Matplotlib

Install dependencies with:

    pip install numpy matplotlib

## ▶️ How to Run

From terminal:

    python render.py -f sample-scaffold.json --highlight ScaffoldingBox -tx 15.5 -tz -1.2 -rz 90 -vo -vz -o output.json -p

This will:

- Load the scaffold data from `sample-scaffold.json`
- Highlight all parts named `"ScaffoldingBox"` in red with thicker lines
- Translate the geometry by +15.5 along X and -1.2 along Z
- Rotate the entire structure 90° around Z axis
- Display the scene in orthographic top view
- Export the transformed geometry to `output.json`
- Show processing time in seconds

## 📄 Input Format

The input JSON contains:

    {
      "parts": [
        {
          "name": "ScaffoldingBox",
          "ecsBox": [16 float values representing a 4x4 matrix],
          "width": 1.5,
          "depth": 0.62,
          "height": 2.0
        }
      ]
    }

- `name`: Part type identifier
- `ecsBox`: 4x4 transformation matrix as a flat list of 16 values (row-major order)
- `width`, `depth`, `height`: Size of the bounding box in meters

## 💾 Output

If the `-o` flag is used, a new JSON file is created containing the transformed versions of the input parts. The output format is identical to the input.

## ⚙️ CLI Options

| Flag                 | Description                                            |
|----------------------|--------------------------------------------------------|
| `-f`                 | Input JSON file (required)                             |
| `-o`                 | Output JSON file path (optional)                       |
| `--highlight <name>` | Highlight matching part(s) in red and bold             |
| `-b`                 | Only render parts named "ScaffoldingBox"               |
| `-tx`, `-ty`, `-tz`  | Global translation along X, Y, Z                       |
| `-rz`                | Global rotation around Z axis (degrees)                |
| `-vo`                | Use orthographic projection (default is perspective)   |
| `-vx`, `-vy`, `-vz`  | Set camera direction along X, Y, Z axis                |
| `-p`                 | Print time taken for processing                        |

## ✅ Solution

This solution consists of a single Python script (`render.py`) that fulfills all requirements specified in the task.

### Input Processing

The script accepts a JSON file containing scaffold geometry under the `parts` array. Each part includes a 4×4 transformation matrix (`ecsBox`) and dimensions (`width`, `depth`, `height`). The script reads this data using Python's built-in `json` module.

### Transformations

The following global transformations are supported and applied to all parts:

- Translation along X, Y, Z axes (`-tx`, `-ty`, `-tz`)
- Rotation around the Z-axis (`-rz`, in degrees)

Transformations are applied using NumPy matrix operations. The original `ecsBox` matrix of each part is multiplied by a global rotation matrix and offset by a translation vector.

### Filtering and Highlighting

- If the `-b` flag is provided, only parts with `"name": "ScaffoldingBox"` are rendered.
- If `--highlight <name>` is specified, all parts with that name are rendered in red with thicker lines.

### Rendering

Using `matplotlib`'s 3D plotting tools:

- Each part is rendered as a hollow box using only its 12 edge lines.
- The corner coordinates of the box are computed based on dimensions and the transformed `ecsBox`.
- The viewer can choose orthographic or perspective projection (`-vo`), and set camera direction (`-vx`, `-vy`, `-vz`).

### Output Export

If the `-o` flag is provided, the transformed parts list is saved to a new JSON file in the same structure as the input.

### Performance Measurement

The script supports benchmarking via the `-p` flag, which prints elapsed time in seconds after processing.

### Tools and Design Notes

- Language: Python 3.7+
- Libraries used: `argparse`, `json`, `numpy`, `matplotlib`
- No OS-specific libraries or tools used.
- Code is modular, readable, and fully commented for clarity.

Thanks for the opportunity!  
Submission by **Dino (Uğur Akalp)**
