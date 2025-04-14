Hello dear python CAD dev!

This repository is supposed to act as a playground for your submission.

Before getting started, please make sure use this repository as a **template** and create your own **public** repository, on which you will commit and push your code. 
Once you are ready, please mail us back the link to your repository. 

Below, you will find the **Task** definition.

Happy Hacking :computer:

# Task

Write a python script to render in 3D a JSON file containing scaffold geometry and optionally to store the resulting geometry in a file. All the scaffolding parts are specified with their bounding boxes, as described in "File format" section below. All the geometry rendering for each part should be hollow box with lines for its edges, with some specific processing described in the "Command parameters" section below. 
There should be functionality to render the scaffold geometry with:
* additional translation by OX, OY, OZ axes and also rotation by OZ.
* rendering only the scaffold boxes or all the data (scaffold boxes + all the parts)
* rendering specific part type in red color and thicker line
* store the processed geometry in outpuf JSON file with the same format.

There is sample-scaffold.json input JSON file provided in this repo.

## File format

The input JSON file contains
```
{
    "parts": [
        {
            "name": "<part-type-id>",
            "ecsBox": [
                1.0,
                0.0,
                0.0,
                1.8699999999999999,
                0.0,
                1.0,
                0.0,
                0.45999999999999996,
                0.0,
                0.0,
                1.0,
                1.155,
                0.0,
                0.0,
                0.0,
                1.0
            ],
            "width": 1.5,
            "depth": 0.62,
            "height": 2.0
        },
        ...
    ],
}
```
Where:
* name is the part type identifier, which is "ScaffoldingBox" for scaffold boxes or a part-type ID number for all the scaffolding parts.
* width, depth, height are sizes of the part bounding box in meters
* ecsBox contains the 4x4 matrix of the 3D transformation of the center of the bounding box of this part


## Command Parameters
```
-f <filepath>  Input JSON file path-name
-o <filepath>  Output JSON file with applied settings specified by parameters: -h, -b, -tx, -ty, -tz, -rz
-h <name>      (optional) Highlight (render in red and thicker line box) the part type specified by its name in JSON data
-b             (optional) Render "ScaffoldingBox" items only
-tx <float>    (optional) Render the geometry with additional translation by OX
-ty <float>    (optional) Render the geometry with additional translation by OY
-tz <float>    (optional) Render the geometry with additional translation by OZ
-rz <float>    (optional) Render the geometry with additional rotation by OY (in degrees)
-vo            (optional) Render with orthographic view (default is perspective)
-vx            (optional) Render with view (camera) direction OX (positive)
-vy            (optional) Render with view (camera) direction OY (positive)
-vz            (optional) Render with view (camera) direction OZ (positive)
-p             (optional) Performance measurement to print time spent in data processing and rendering in "0.000000 sec" format.
```
Example:
>python render.py -f scaffold-1.json -h "ScaffoldingBox" -tx 15.5 -tz -1.2 -rz 90.0 -vo -vz
This should render the provided data from file scaffold-1.json, transforming it to 15.5 by OX, -1.2 by OZ, rotating by 90 degrees by OZ, and the rendered plot should be orthographic top view of the scaffold, with hightlighted "ScaffoldingBox" items.

# Goals

* correct processing in all the possible cases.
* clean code, minimal for the task, well structured and commented.
* best algorithmic design to achieve optimal data processing and rendering performance.
* do not use OS-specific libraries and tools.

# Solution

< Please describe in detail your solution here >