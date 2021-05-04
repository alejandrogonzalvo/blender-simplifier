#!/usr/bin/env python
"""
Script that merges nearby node for mesh simplification
Copyright (C) 2021 Alejandro Gonzalvo, alejandrogonhid@protonmail.com

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

import bpy
from math import sqrt

max_distance = 1

# Aunque no exista interfaz, debemos cambiar el modo a "objeto" o
# "edicion" según corresponderia en la i.gráfica.
bpy.ops.object.mode_set(mode = 'OBJECT')
# El script está pensado para ser usado en complemento a la i.gráfica.
# Por tanto se selecciona el objeto seleccionado por el usuario:
obj = bpy.context.selected_objects[0]
verts = obj.data.vertices

i = 0
for vertice in verts: #Iteramos la distancia de cada vértice con el resto.
    i += 1
    bpy.ops.object.mode_set(mode = 'EDIT') 
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set(mode = 'OBJECT') 
    vertice.select = True
    for vertice2 in verts[i:]: #Con el rango optimizamos la iteración.
        distance = sqrt( #función de distancia
            (vertice.co[0] - vertice2.co[0])**2
            + (vertice.co[1] - vertice2.co[1])**2
            + (vertice.co[2] - vertice2.co[2])**2
        )
        print(distance)
        if distance < max_distance:
            vertice2.select = True
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.mesh.merge()
            break
