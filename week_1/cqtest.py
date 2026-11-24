import cadquery as cq
#from cadquery.vis import show

height = 60.0
width = 80.0
thickness = 10.0
diameter = 22.0 
padding = 12.0 

# make the base
result = (
    cq.Workplane("XY")
    .box(height, width, thickness)
    .faces(">Z")
    .workplane()
    .hole(diameter)
    .faces(">Z")
    .workplane()
    .rect(height - padding, width - padding, forConstruction=True)
    .vertices()
    .cboreHole(2.4, 4.4, 2.1)
    .edges("|Z")
    .fillet(10.0)
    .edges("|Y")
    .fillet(1.0)
   # .edges("|Y")
    #.fillet(1.0)
   
)


# Render the solid
#show(result)
result.export("tut2.step")