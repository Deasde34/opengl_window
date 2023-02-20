#Importar librerías
from OpenGL.GL import *
import glfw
import math


def dibujar_cielo():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.7, 1.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glColor3f(0.4, 0.7, 1.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()

# Define a function to draw a mountain
def dibujar_montana():
    glBegin(GL_TRIANGLES)
    glColor3f(0.3, 0.3, 0.3)
    glVertex3f(-0.5, -0.7, 0.0)
    glVertex3f(-0.2, 0.3, 0.0)
    glVertex3f(0.1, -0.7, 0.0)
    glVertex3f(0.1, -0.2, 0.0)
    glVertex3f(-0.2, -0.2, 0.0)
    glVertex3f(-0.2, -0.7, 0.0)
    glVertex3f(-0.5, -0.7, 0.0)
    glEnd()

# Define a function to draw a tree
def dibujar_arbol():
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.3, 0.1)
    glVertex3f(-0.2, -0.7, 0.0)
    glVertex3f(-0.1, -0.7, 0.0)
    glVertex3f(-0.1, -0.2, 0.0)
    glVertex3f(-0.2, -0.2, 0.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.1, 0.6, 0.1)
    glVertex3f(-0.2, -0.2, 0.0)
    glVertex3f(-0.1, -0.2, 0.0)
    glVertex3f(-0.15, -0.1, 0.0)
    glEnd()

def dibujar_circulos():
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(0.23,0.05,0.32)
    circulo_x= 0.4
    circulo_y = 0.3
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.1 *math.cos(radianes)) + circulo_x, 0.1 *math.sin(radianes) +circulo_y, 2.0)
    glEnd()
    #manzana
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(0.56,0.08,0.06)
    circulo_x= -0.4
    circulo_y = 0.1
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.1 *math.cos(radianes)) + circulo_x, 0.1 *math.sin(radianes) +circulo_y, 2.0)
    glEnd()
    #manzana verde
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(0.24,0.70,0.06)
    circulo_x= -0.2
    circulo_y = 0.6
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.1 *math.cos(radianes)) + circulo_x, 0.1 *math.sin(radianes) +circulo_y, 2.0)
    glEnd()
    #SOL
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(0.89,0.92,0.24)
    circulo_x= -1
    circulo_y = 1
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((1 *math.cos(radianes)) + circulo_x, 1 *math.sin(radianes) +circulo_y, 2.0)
    glEnd()
    #canasta
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(0.58,0.40,0.23)
    circulo_x= 0.5
    circulo_y = -0.8
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.4 *math.cos(radianes)) + circulo_x, 0.1 *math.sin(radianes) +circulo_y, 2.0)
    glEnd()
    #naranja
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(0.98,0.45,0.09)
    circulo_x= -0.5
    circulo_y = 0.8
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.12 *math.cos(radianes)) + circulo_x, 0.12 *math.sin(radianes) +circulo_y, 2.0)
    glEnd()
    #sandia
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(0,0.37,0.05)
    circulo_x= -0.5
    circulo_y = 0.3
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.2 *math.cos(radianes)) + circulo_x, 0.1 *math.sin(radianes) +circulo_y, 2.0)
    glEnd()
    
def dibujar_suelo():
    glBegin(GL_QUADS)
    glColor3f(0.14,0.09,0.05)
    glVertex3f(-1.0,-0.7,0.0)
    glVertex3f(1.0,-0.7,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()
def dibujar_suelo2():
    glBegin(GL_QUADS)
    glColor3f(0.27,0.16,0.09)
    glVertex3f(-1.0,-0.9,0.0)
    glVertex3f(1.0,-0.9,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()


def main():
    #Establcer valores de ventana
    width = 472
    height = 378
    #Inicializar GLFW
    if not glfw.init():
        return
    #Declarar ventana
    window = glfw.create_window(width, height, "Mi ventana", None, None)
    #Configuración de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw. OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    #Verificar la creación de la ventana
    if not window:
        glfw.terminate()
        return
    #Establecer el contexto
    glfw.make_context_current(window)
    #Imprimir versión
    version = glGetString(GL_VERSION)
    print(version)
    #Ciclo de dibujo (Draw loop)
    while not glfw.window_should_close(window):
        #Estavkecer ek viewport
        glViewport(0, 0, width, height)
        #Establecer el color de borrado
        glClearColor(0.5, 0.5, 0.5, 1.0)
        #Establecer el color del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #Dibujar
        dibujar_cielo()
        dibujar_suelo()
        dibujar_suelo2()
        dibujar_montana()
        dibujar_arbol()
        dibujar_circulos()

        

        #Polling de inputs
        glfw.poll_events()
        #Cambiar los buffer
        glfw.swap_buffers(window)
    #Acabar con procesos y uso de memoria
    glfw.destroy_window(window)
    glfw.terminate()
    
#Ejecutar el main
if __name__ == "__main__":
    main()