import glfw
from OpenGL.GL import *
import math
import time 


def main():
    # 1. Inicialização do GLFW
    if not glfw.init():
        print("Erro: Não foi possível inicializar o GLFW.")
        return

    # Configuração do Contexto OpenGL (Versão 2.1)
    # Esta é a versão mais recente que ainda suporta o pipeline fixo.
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)

    # 2. Criação da Janela de Aplicação
    window = glfw.create_window(200, 800, "Semáforo", None, None)
    if not window:
        glfw.terminate()    
        print("Erro: Não foi possível criar a janela GLFW.")
        return

    # Torna o contexto da janela o contexto atual do thread
    glfw.make_context_current(window)

    # 3. Configuração Inicial do Estado OpenGL
    # As matrizes de transformação são gerenciadas por aqui.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity() 
    glOrtho(0, 200, 0, 800, 0, 1) # Isso daqui foi um caos mas basicamente não ferra os meus circulos

    #Espeficamos as operações de viewport
    glViewport(0, 0, 200, 800)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    tempo_1 = time.time()


    # 4. Loop de Renderização Principal
    while not glfw.window_should_close(window):
        # Limpa o buffer de cor do frame anterior
        glClear(GL_COLOR_BUFFER_BIT)

        # Reseta a matriz para o estado inicial a cada frame.
        glLoadIdentity()
        tempo_2 = time.time()
        tempo = tempo_2 - tempo_1
        print(tempo)
        if tempo < 10:
            draw_circle(100,600,50,150,(1,0,0))
        elif tempo >= 10 and tempo < 20 :
            draw_circle(100,300,50,150,(1,1,0))
        else:
            draw_circle(100,100,50,150,(0,1,0))
        if tempo >= 30:
            tempo_1 = time.time()
        # Verifica e processa eventos da janela
        glfw.poll_events()
        # Troca os buffers front e back para exibir a imagem renderizada
        glfw.swap_buffers(window)

    # 5. Finalização
    glfw.terminate()

def draw_circle(x, y, radius, segments,color):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(*color)
    glVertex2f(x, y) # centro do círculo
    for i in range(segments + 1):
        angle = 2.0 * math.pi * i / segments
        dx = radius * math.cos(angle)
        dy = radius * math.sin(angle)
        glVertex2f(x + dx, y + dy)
    glEnd()


if __name__ == "__main__":
    main()
