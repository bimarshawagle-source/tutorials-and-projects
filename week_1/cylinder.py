import cadquery as cq
from cadquery import show
result = cq.Workplane("XY").box(1,2,3)
show(result)