from OpenGL.GL import *
import glfw
import math
from Bala import *

class Nave:
    x = 0.0
    y = 0.0
    angulo = 0.0
    velocidad_giro = 180.0
    velocidad = 1.3
    desfase = 90.0
    bala = Bala()

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0.0)
        glRotate(self.angulo, 0.0,0.0,1.0)
        glBegin(GL_TRIANGLE_STRIP)
        glColor3f(0.58,0.40,0.23)
        glVertex3f(-0.28,-0.8,0.0)
        glVertex3f(0.14,-0.8,0.0)
        glVertex3f(-0.16,-0.95,0.0)
        glVertex3f(0.02,-0.95,0.0)
        glEnd()
        glPopMatrix()

    def actualizar(self,window,tiempo_delta):
        estado_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
        estado_espacio = glfw.get_key(window, glfw.KEY_SPACE)
        estado_derecha = glfw.get_key(window, glfw.KEY_RIGHT)



        if estado_izquierda == glfw.PRESS:
            self.x -= self.velocidad * tiempo_delta
        if estado_derecha == glfw.PRESS:
            self.x += self.velocidad * tiempo_delta
        

        if self.x > 1.0 or self.x < -1.0:
            self.x = -self.x
        if self.y > 1.0 or self.y < -1.0:
            self.y = -self.y
        
        if estado_espacio == glfw.PRESS:
            self.disparar()

    def disparar(self):
        if not self.bala.disparando:
            self.bala.x = self.x
            self.bala.y = self.y
            self.bala.angulo = self.angulo + self.desfase
            self.bala.disparando = True