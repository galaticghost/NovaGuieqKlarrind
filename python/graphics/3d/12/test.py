import glfw
from OpenGL.GL import *
import numpy as np


def main():
    # 1. Initialize GLFW
    if not glfw.init():
        print("Erro: Não foi possível inicializar o GLFW.")
        return

    # Request OpenGL Core Profile 3.3
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    # glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.TRUE)  # Uncomment if needed (MacOS)

    # 2. Criação da Janela de Aplicação
    window = glfw.create_window(800, 600, "Esqueleto OpenGL Core (2D)", None, None)
    if not window:
        glfw.terminate()
        print("Erro: Não foi possível criar a janela GLFW.")
        return

    # Torna o contexto da janela o contexto atual do thread
    glfw.make_context_current(window)

    # Dados do Triângulo (Posicionado à Esquerda)
    tri_vertices = np.array([
    -0.7, -0.5,
    0.0, -0.5,
    -0.35, 0.5,
    ], dtype=np.float32)
    # Dados do Quadrado (Posicionado à Direita)
    sq_vertices = np.array([
    0.2, -0.5,
    0.7, -0.5,
    0.7, 0.5,
    0.2, -0.5,
    0.7, 0.5,
    0.2, 0.5,
    ], dtype=np.float32)

    VAO_tri, VBO_tri = setup_geometry(tri_vertices)
    VAO_sq, VBO_sq = setup_geometry(sq_vertices)

    seila = np.array([
        0.4,0.5,1.0,1.0,1.0,
        0.9,0.5,0.5,0.5,1.0,
        0.25,-0.5,0.0,1.0,1.0
    ],dtype=np.float32)

    matrix_proj = np.identity(4, dtype=np.float32)

    #Espeficamos as operações de viewport
    glViewport(0, 0, 800, 600)

    # Define a cor de fundo da janela
    glClearColor(0.3, 0.3, 0.3, 1.0)

    # 4. Loop de Renderização Principal
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glBindVertexArray(VAO_tri)
        glDrawArrays(GL_TRIANGLES,0,3)
        glBindVertexArray(0)

        glBindVertexArray(VAO_sq) # Ativa o estado de leitura do Quadrado
        glDrawArrays(GL_TRIANGLES, 0, 6) # O quadrado tem 6 vértices (2 triângulos)
        glBindVertexArray(0) #unbing

        # Verifica e processa eventos da janela
        glfw.poll_events()

        # Troca os buffers front e back para exibir a imagem renderizada
        glfw.swap_buffers(window)


    # 5. Finalização
    glfw.terminate()
    #Também será necessário limpar os VAOs/VBOs e Program/Shaders

def setup_geometry(vertices):
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)
    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * vertices.itemsize ,
    ctypes.c_void_p(0))
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)
    return vao, vbo

if __name__ == "__main__":
    main()
