from OpenGL.GL import *
import glfw
import math

class Bala:
    x = 0.0
    y = 0.0
    angulo = 0.0
    velocidad = 2.0
    disparando = False

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0.0)
        glBegin(GL_TRIANGLE_STRIP)
        glVertex3f(-0.01, -0.01, 0.00)
        glVertex3f(-0.01, 0.01,0.0)
        glVertex3f(0.01, -0.01,0.0)
        glVertex3f(0.01, 0.01,0.0)
        glEnd()
        glPopMatrix()

    def actualizar(self,window,tiempo_delta):
        self.x = self.x + (math.cos(self.angulo  * math.pi / 180) * self.velocidad * tiempo_delta)
        self.y = self.y + (math.sin(self.angulo  * math.pi / 180) * self.velocidad * tiempo_delta)

        if self.x >= 1.0 or self.y >= 1.0 or self.x <= -1.0 or self.y <= -1.0:
            self.disparando = False
