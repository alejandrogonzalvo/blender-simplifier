import bpy
from math import sqrt

max_distance = 1

bpy.ops.object.mode_set(mode = 'OBJECT') 
obj = bpy.context.active_object
verts = obj.data.vertices

i = 0
for vertice in verts:
    i += 1
    bpy.ops.object.mode_set(mode = 'EDIT') 
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set(mode = 'OBJECT') 
    vertice.select = True
    for vertice2 in verts[i:]:
        distance = sqrt(
            (vertice.co[0] - vertice2.co[0])**2
            + (vertice.co[1] - vertice2.co[1])**2
            + (vertice.co[2] - vertice2.co[2])**2
        )
        if distance < max_distance:
            vertice2.select = True
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.merge(type='CENTER')
