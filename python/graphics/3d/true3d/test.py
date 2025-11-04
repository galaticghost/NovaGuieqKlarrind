import glfw
from OpenGL.GL import *
import numpy as np
import cv2

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

    texture = cv2.imread('texture.webp',cv2.IMREAD_COLOR)
    texture = cv2.cvtColor(texture, cv2.COLOR_BGR2RGB)
    texture = cv2.flip(texture, 0)

    vertices = np.array([
    # Posição # Textura Coords (U, V)
    # Triângulo 1
    0.5, 0.5, 0.0, 1.0, 1.0, # Canto superior direito
    0.5, -0.5, 0.0, 1.0, 0.0, # Canto inferior direito
    -0.5, -0.5, 0.0, 0.0, 0.0,  # Canto inferior esquerdo
    # Triângulo 2
    -0.5, -0.5, 0.0, 0.0, 0.0,  # Canto inferior esquerdo
    -0.5, 0.5, 0.0, 0.0, 1.0, # Canto superior esquerdo
    0.5, 0.5, 0.0, 1.0, 1.0, # Canto superior direito
    ], dtype=np.float32)

    vao_trin, vbo_trin = setup_geometry(vertices)

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D,texture_id)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,640,587,0,GL_RGB, GL_UNSIGNED_BYTE,texture)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    vshader = create_shader(GL_VERTEX_SHADER,'shader7.vert')
    fshader = create_shader(GL_FRAGMENT_SHADER,'shader78.frag')
    
    shader_program = glCreateProgram()
    glAttachShader(shader_program,vshader)
    glAttachShader(shader_program,fshader)
    glLinkProgram(shader_program)


    glUseProgram(shader_program)
    texture_loc = glGetUniformLocation(shader_program, "frameColor")
    glUniform1i(texture_loc, 0) # Texture unit 0

    #Espeficamos as operações de viewport
    glViewport(0, 0, 800, 600)

    proj_matrix = np.identity(4,np.float32)

    # Define a cor de fundo da janela
    glClearColor(0.3, 0.3, 0.3, 1.0)

    # 4. Loop de Renderização Principal
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        #Definicao da matriz de projeção


        glUseProgram(shader_program)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glUniform1i(texture_loc, 0)
        glBindVertexArray(vao_trin)
        glDrawArrays(GL_TRIANGLES,0,6)
        glBindTexture(GL_TEXTURE_2D, 0)
        glBindVertexArray(0)        

        glUseProgram(0)


        # Desvincular VAOs/VBOs
        # Desvincular o programa (shaders)

        glfw.swap_buffers(window)
        # Verifica e processa eventos da janela
        glfw.poll_events()

        # Troca os buffers front e back para exibir a imagem renderizada


    # 5. Finalização
    glfw.terminate()
    #Também será necessário limpar os VAOs/VBOs e Program/Shaders

def setup_geometry(vertex):

    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)
    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertex.nbytes, vertex, GL_STATIC_DRAW)
    # Stride = 5 floats (Posição + Textura) * 4 bytes/float = 20 bytes
    stride = 5 * vertex.itemsize
    # Atributo 0: Posição (3 floats)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)
    # Atributo 1: Coordenadas de textura (2 floats)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(3 * vertex.itemsize))
    glEnableVertexAttribArray(1)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return vao,vbo

def create_shader(shader_type,path):
    shader = glCreateShader(shader_type)
    with open(path,'r') as file:
        glShaderSource(shader,file.read())
    glCompileShader(shader)
    print(glGetShaderiv(shader, GL_COMPILE_STATUS))
    return shader

if __name__ == "__main__":
    main()
