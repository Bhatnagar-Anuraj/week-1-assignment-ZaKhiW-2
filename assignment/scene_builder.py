"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

#building_width = 3
building_height = 6
building_depth = 9
building_x = -7
building_z = 8

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)
    
cmds.move(building_x, building_height / 2.0, building_z, building)


tree_radius = 2
tree_height = 3
tree_x = -3
tree_z = 5

tree = cmds.polyCone(
    name="tree_01",
    radius=tree_radius,
    height=tree_height,
)
    
cmds.move(tree_x, tree_height / 2.0, tree_z, tree)


building_width = 1
building_height = 9
building_depth = 3
building_x = 12
building_z = 10

building = cmds.polyCube(
    name="building_02",
    width=building_width,
    height=building_height,
    depth=building_depth,
)
    
cmds.move(building_x, building_height / 2.0, building_z, building)


tree_radius = 2
tree_height = 1
tree_x = -10
tree_z = 21

tree = cmds.polyCone(
    name="tree_02",
    radius=tree_radius,
    height=tree_height,
)
    
cmds.move(tree_x, tree_height / 2.0, tree_z, tree)

building_radius = 7
building_height = 15
building_x = 11
building_z = -9

building = cmds.polyCylinder(
    name="building_03",
    radius=building_radius,
    height=building_height,
)
    
cmds.move(building_x, building_height / 2.0, building_z, building)

cmds.viewFit(allObjects=True)
print("Scene built successfully!")
