#Import librerias
from OpenGL.GL import *
import glfw
import math
from Nave import *
from frutas.Manzana import *
from frutas.Uvas import *
from frutas.Papaya import *
from frutas.Sandia import *
from frutas.Mandarina import *
from frutas.Kiwi import *


tiempo_anterior = 0.0
window = None
nave = Nave()
manzana = Manzana()
sandia = Sandia()
uvas = Uvas()
papaya = Papaya()
mandarina = Mandarina()
kiwi = Kiwi()

def dibujar():
    global nave
    #Dibujar modelos por separado
    nave.dibujar()
    if nave.bala.disparando:
        nave.bala.dibujar()
    manzana.dibujar()
    uvas.dibujar()
    papaya.dibujar()
    mandarina.dibujar()
    kiwi.dibujar()
    sandia.dibujar()


def actualizar():
    global tiempo_anterior, window, nave
    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior

    #Actualizo mis modelos por separado
    nave.actualizar(window,tiempo_delta)
    if nave.bala.disparando:
        nave.bala.actualizar(window, tiempo_delta)
    manzana.actualizar(window,tiempo_delta)
    uvas.actualizar(window,tiempo_delta)
    papaya.actualizar(window,tiempo_delta)
    mandarina.actualizar(window,tiempo_delta)
    kiwi.actualizar(window,tiempo_delta)
    sandia.actualizar(window,tiempo_delta)
    tiempo_anterior = tiempo_actual

def inicializar():
    manzana.angulo = 270
    uvas.angulo = 270
    papaya.angulo = 270
    mandarina.angulo = 270
    kiwi.angulo = 270
    sandia.angulo = 270
def main():
    global window
    #Establece el tamaño de la ventana
    width=800
    height=800
    #Inicializar GLFW
    if not glfw.init():
        return
    #Declarar Ventana
    window= glfw.create_window(width,height,"manzanas", None,None)
    #Configuracuibes de OpenGL
    glfw.window_hint(glfw.SAMPLES,4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT,GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE,glfw.OPENGL_CORE_PROFILE)
    #Verificar la creacion de la ventana
    if not window:
        glfw.terminate()
        return
    #Establecer el contexto
    glfw.make_context_current(window)
    #imprimir version
    version=glGetString(GL_VERSION)
    print(version)
    #Establece valores iniciales
    inicializar()
    #Ciclo de dibujo (Draw Loop)
    while not glfw.window_should_close(window):
        #Establecer el viewport
        glViewport(0,0,width,height)
        #Establecer el color de borrado
        glClearColor(0.5,0.5,0.5,1.0)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #Dibujar
        dibujar()
        actualizar()
        #Polling de inputs
        glfw.poll_events()
        #Cambiar los buffers
        glfw.swap_buffers(window)
    #Acabar con procesos y uso de memoria
    glfw.destroy_window(window)
    glfw.terminate()
    
#Ejecutar el main
if __name__=="__main__":
    main()