import cadquery as cq
sides = 10.0
cube = cq.Workplane("XY").box(sides, sides, sides)
cube.export("cube.step")