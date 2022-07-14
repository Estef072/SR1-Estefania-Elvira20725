
# Estefania Elvira 20725
# Ejercicio 1 SR-points
# Fecha 13.07.22
from gl import Renderer,vector2, color

width = 960
height = 540

rend = Renderer(width, height)


rend.glClearColor(0.01, 0, 0.3)
rend.glClear()

rend.glColor(1, 1, 1)

rend.glViewPort(100, 100, 740, 480)

rend.glVertex(0,0)
rend.glVertex(1,1)
rend.glVertex(-1,-1)

# estas son  las lineas curvas
rend.glLine(vector2(600, 300), vector2(400, 200), color(1, 1, 1))
rend.glLine(vector2(600, 300), vector2(400, 200), color(1, 1, 1))
rend.glLine(vector2(200, 300), vector2(400, 400), color(1, 1, 1))

#  estas son las lineas rectas
rend.glLine(vector2(200, -10), vector2(200, 400), color(1, 1, 1))
rend.glLine(vector2(400, 0), vector2(400, 400), color(1, 1, 1))
rend.glLine(vector2(600, 0), vector2(600, 400), color(1, 1, 1))

rend.glFinish("output.bmp")
