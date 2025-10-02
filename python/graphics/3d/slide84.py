import glfw
from OpenGL.GL import *


def main():
    if not glfw.init():
        print("Erro: Não foi possível inicializar o GLFW.")
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)

    window = glfw.create_window(800, 600, "Translate", None, None)
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
    glOrtho(-1, 1, -1, 1, -1, 1) # A projeção ortogonal é usada em 2D

    #Espeficamos as operações de viewport
    glViewport(0, 0, 800, 600)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Define a cor de fundo da janela
    glClearColor(0.3, 0.3, 0.3, 1.0)
    
    # 4. Loop de Renderização Principal
    while not glfw.window_should_close(window):
        # Limpa o buffer de cor do frame anterior
        glClear(GL_COLOR_BUFFER_BIT)

        # Reseta a matriz para o estado inicial a cada frame.
        glLoadIdentity()

        glBegin(GL_TRIANGLES)

        # Vertice 1: Inferior esquerdo
        glColor3f(1, 0, 0)
        glVertex2f(-0.5, -0.5)
        
        # Vertice 2: Inferior direito
        glColor3f(0, 0, 1)
        glVertex2f(0.5, -0.5)
       
        # Vertice 3: Superior direito
        glColor3f(0, 1, 0)
        glVertex2f(0, 0)
        
        glEnd() # Finaliza a primitiva

        glTranslatef(0,-0.75,0)

        glBegin(GL_QUADS)
        # Vertice 1: Inferior esquerdo
        glColor3f(1, 0, 0)
        glVertex2f(-0.25, 0.25)
        
        # Vertice 2: Inferior direito
        glColor3f(0, 1, 0)
        glVertex2f(-0.25, 0.75)
        
        # Vertice 3: Superior direito
        glColor3f(0, 0, 1)
        glVertex2f(0.25, 0.75)
        
        # Vertice 4: Superior esquerdo
        glColor3f(1, 1, 1)
        glVertex2f(0.25, 0.25)
        glEnd() 


        # Verifica e processa eventos da janela
        glfw.poll_events()
        # Troca os buffers front e back para exibir a imagem renderizada
        glfw.swap_buffers(window)

    # 5. Finalização
    glfw.terminate()


if __name__ == "__main__":
    main()
