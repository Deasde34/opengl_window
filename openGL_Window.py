#Importar librerías
from OpenGL.GL import *
import glfw
import math

def dibujar_cielo():
    glBegin(GL_QUADS)
    glColor3f(0.0,0.7,5.0)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-0.5,0.0)
    glVertex3f(-1.0,-0.5,0.0)
    glEnd()

def dibujar_cesped():
    glBegin(GL_QUADS)
    glColor3f(0.13,0.69,0.29)
    glVertex3f(-1.0,-0.2,0.0)
    glVertex3f(1.0,-0.2,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()

def dibujar_casa():
    glBegin(GL_QUADS)
    glColor3f(0.72,0.47,0.34)
    glVertex3f(-0.1,0.5,0.0)
    glVertex3f(0.8,0.5,0.0)
    glVertex3f(0.8,-0.8,0.0)
    glVertex3f(-0.1,-0.8,0.0)
    glEnd()

def dibujar_techo():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(0.35,0.9,0.0)
    glVertex3f(-0.35,0.35,0.0)
    glVertex3f(1.06,0.35,0.0)
    glEnd()

def dibujar_puerta():
    glBegin(GL_QUADS)
    glColor3f(1.0,0.5,0.0)
    glVertex3f(0.1,-0.2,0.0)
    glVertex3f(0.3,-0.2,0.0)
    glVertex3f(0.3,-0.8,0.0)
    glVertex3f(0.1,-0.8,0.0)
    glEnd()
    
def dibujar_ventana():
    glBegin(GL_QUADS)
    glColor3f(0.5,0.1,0.0)
    glVertex3f(0.4,0.2,0.0)
    glVertex3f(0.7,0.2,0.0)
    glVertex3f(0.7,-0.3,0.0)
    glVertex3f(0.4,-0.3,0.0)
    glEnd()

def dibujar_ventana_palo1():
    glBegin(GL_QUADS)
    glColor3f(0.1,0.0,0.0)
    glVertex3f(0.54,0.2,0.0)
    glVertex3f(0.57,0.2,0.0)
    glVertex3f(0.57,-0.3,0.0)
    glVertex3f(0.54,-0.3,0.0)
    glEnd()

def dibujar_ventana_palo2():
    glBegin(GL_QUADS)
    glColor3f(0.1,0.0,0.0)
    glVertex3f(0.4,-0.00,0.0)
    glVertex3f(0.7,-0.00,0.0)
    glVertex3f(0.7,-0.05,0.0)
    glVertex3f(0.4,-0.05,0.0)
    glEnd()

def dibujar_tronco():
    glBegin(GL_QUADS)
    glColor3f(0.72,0.47,0.34)
    glVertex3f(-0.8,0.1,0.0)
    glVertex3f(-0.6,0.1,0.0)
    glVertex3f(-0.6,-0.9,0.0)
    glVertex3f(-0.8,-0.9,0.0)
    glEnd()

def dibujar_sol():
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(1.0, 0.8,0.0)
    circulo_x= -0.8
    circulo_y = 0.7
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.18 *math.cos(radianes)) + circulo_x, 0.3 * math.sin(radianes) +circulo_y, 0.0)
    glEnd()

def dibujar_arbol1():
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(0.0, 1.0,0.0)
    circulo_x= -0.8
    circulo_y = 0.15
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.15 *math.cos(radianes)) + circulo_x, 0.2 * math.sin(radianes) +circulo_y, 0.0)
    glEnd()

def dibujar_arbol2():
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(0.0, 1.0,0.0)
    circulo_x= -0.67
    circulo_y = 0.25
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.15 *math.cos(radianes)) + circulo_x, 0.2 * math.sin(radianes) +circulo_y, 0.0)
    glEnd()

def dibujar_arbol3():
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(0.0, 1.0,0.0)
    circulo_x= -0.55
    circulo_y = 0.1
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.15 *math.cos(radianes)) + circulo_x, 0.2 * math.sin(radianes) +circulo_y, 0.0)
    glEnd()

def dibujar_nube1():
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(1.0, 1.0,1.0)
    circulo_x= -0.3
    circulo_y = 0.7
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.18 *math.cos(radianes)) + circulo_x, 0.15* math.sin(radianes) +circulo_y, 0.0)
    glEnd()

def dibujar_nube2():
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(1.0, 1.0,1.0)
    circulo_x= -0.2
    circulo_y = 0.7
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.2 *math.cos(radianes)) + circulo_x, 0.15* math.sin(radianes) +circulo_y, 0.0)
    glEnd()

def dibujar_nube3():
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(1.0, 1.0,1.0)
    circulo_x= -0.25
    circulo_y = 0.85
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.1 *math.cos(radianes)) + circulo_x, 0.1* math.sin(radianes) +circulo_y, 0.0)
    glEnd()

def dibujar_perilla():
    glBegin(GL_TRIANGLE_FAN) 
    glColor3f(0.1,0.0,0.0)
    circulo_x= 0.13
    circulo_y = -0.5
    glVertex3f(0.0 +circulo_x, 0.0 +circulo_y, 0.0)
    for grados in range (0, 361, 10):
        radianes = grados * math.pi / 180.0
        glVertex3f((0.02 *math.cos(radianes)) + circulo_x, 0.04* math.sin(radianes) +circulo_y, 0.0)
    glEnd()

def main():
    #Establcer valores de ventana
    width = 800
    height = 400
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
        dibujar_cesped()
        dibujar_casa()
        dibujar_techo()
        dibujar_puerta()
        dibujar_ventana()
        dibujar_ventana_palo1()
        dibujar_ventana_palo2()
        dibujar_tronco()
        dibujar_sol()
        dibujar_arbol1()
        dibujar_arbol2()
        dibujar_arbol3()
        dibujar_nube1()
        dibujar_nube2()
        dibujar_nube3()
        dibujar_perilla()
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