import glfw
from OpenGL.GL import *
import numpy as np
import math

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

    triangle_vertices = np.array([
    -0.5, -0.5, -1.0, 1.0, 0.0, 0.0, #V1
    0.5, -0.5, -1.0, 0.0, 1.0, 0.0, #V2
    0.0, 0.5, -1.0, 0.0, 0.0, 1.0 #V3
    ], dtype=np.float32)

    square_vertices = np.array([
    -0.3, -0.3, -2.0, 1.0, 0.5, 0.2, # T1 V1
    0.3, -0.3, -2.0, 1.0, 0.5, 0.2, # T1 V2
    0.3, 0.3, -2.0, 1.0, 0.5, 0.2, # T1 V3
    -0.3, -0.3, -2.0, 1.0, 0.5, 0.2, # T2 V1
    0.3, 0.3, -2.0, 1.0, 0.5, 0.2, # T2 V2
    -0.3, 0.3, -2.0, 1.0, 0.5, 0.2 # T2 V3
    ], dtype=np.float32)

    vao_tri, vbo_tri = setup_geometry(triangle_vertices)

    camera_pos = np.array([0.0, 0.0, 5.0], dtype=np.float32) #world pos
    camera_front = np.array([0.0, 0.0, -1.0], dtype=np.float32) #facing
    camera_up = np.array([0.0, 1.0, 0.0], dtype=np.float32) #up
    def get_view_matrix(camera_pos, camera_front, camera_up):
        z_axis = -camera_front / np.linalg.norm(camera_front)
        x_axis = np.cross(camera_up, z_axis)
        x_axis = x_axis / np.linalg.norm(x_axis)
        y_axis = np.cross(z_axis, x_axis)
        # Create view matrix (transpose)
        view = np.array([
        [x_axis[0], y_axis[0], z_axis[0], 0], #s
        [x_axis[1], y_axis[1], z_axis[1], 0], #u
        [x_axis[2], y_axis[2], z_axis[2], 0], #f
        [-np.dot(x_axis, camera_pos), -np.dot(y_axis, camera_pos), -np.dot(z_axis, camera_pos), 1]
        ], dtype=np.float32)
        return view

    #Espeficamos as operações de viewport
    glViewport(0, 0, 800, 600)

    fov=45.0 #degrees
    aspect= 800 / 600
    near=0.1 #z-distance
    far=100.0 #z-distance
    def get_projection_matrix(fov, aspect_ratio, near, far):
        f = 1.0 / math.tan(math.radians(fov) / 2.0)
        proj = np.zeros((4, 4), dtype=np.float32)
        # Create projection matrix (transpose)
        proj[0, 0] = f / aspect_ratio
        proj[1, 1] = f
        proj[2, 2] = (far + near) / (near - far)
        proj[2, 3] = -1.0
        proj[3, 2] = (2.0 * far * near) / (near - far)
        return proj

    projection_matrix = get_projection_matrix(fov,aspect,near,far)
    # Define a cor de fundo da janela
    glClearColor(0.3, 0.3, 0.3, 1.0)

    # 4. Loop de Renderização Principal
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        #Definicao da matriz de projeção


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
    stride = 6 * vertex.itemsize
    # Atributo 0: Posição (3 floats)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)
    # Atributo 1: Coordenadas de textura (2 floats)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(3 * vertex.itemsize))
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
