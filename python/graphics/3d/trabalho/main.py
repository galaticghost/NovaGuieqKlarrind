from OpenGL.GL import *
from fps import FPSCounter
from utils import *
import glfw
import numpy as np
import math
import cv2
import time

def main():
    #Globais da camera e da rotação
    global camera_pos,camera_front,camera_up,window,first_mouse,yaw,pitch,last_x,last_y,rot_x,rot_y
    #Globais do model
    global translation_m,rotation_x,rotation_y,rotation_z,scale_m,shader_program,time_checker_status,gray_color_bool

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
    window_width = 1920
    window_height = 1080

    window = glfw.create_window(window_width, window_height, "Quadrado", None, None)
    if not window:
        glfw.terminate()
        print("Erro: Não foi possível criar a janela GLFW.")
        return

    # Torna o contexto da janela o contexto atual do thread
    glfw.make_context_current(window)
    # Prepara os callbacks
    glfw.set_input_mode(window,glfw.CURSOR,glfw.CURSOR_DISABLED)
    glfw.set_cursor_pos_callback(window, mouse_callback) # Callback da camera
    glfw.set_mouse_button_callback(window, mouse_button_callback) # Callback dos controles do mouse
    glfw.set_key_callback(window,keys_callback) # Callback dos kernels
    #glfw.swap_interval(0) # Descomenta para fps enormes(esse quebrar velocidade tbm())

    # 3. Váriaveis e afins

    # Quadrado
    quadrado_vertex = np.array([0.3, 0.3, -1.0, 1.0, 1.0, # T1 V1
                        0.3, -0.3, -1.0, 1.0, 0.0, # T1 V2
                        -0.3, -0.3, -1.0, 0.0, 0.0, # T1 V3
                        -0.3, -0.3, -1.0, 0.0, 0.0, # T2 V1
                        -0.3, 0.3, -1.0, 0.0, 1.0, # T2 V2
                        0.3, 0.3, -1.0, 1.0, 1.0, # T2 V3
    ],dtype=np.float32)

    vao_qua, vbo_qua = setup_geometry_uv(quadrado_vertex)

    # Textura
    texture = cv2.imread('texture.jpg',cv2.IMREAD_COLOR)
    texture = cv2.cvtColor(texture, cv2.COLOR_BGR2RGB)
    texture = cv2.flip(texture, 0) # Inverte verticalmente
    tex_height, tex_width , _ = texture.shape

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D,texture_id)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,tex_width,tex_height,0,GL_RGB, GL_UNSIGNED_BYTE,texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    # Matrizes do model
    scale_m = create_scale(2.0, 1.5, 1.0)
    rotation_x = create_rotation(0.0,"x")
    rotation_y = create_rotation(0.0,"y")
    rotation_z = create_rotation(0.0,"z")
    rotation_m = rotation_x @ rotation_y @ rotation_z
    translation_m = create_translation(0.0, 0.0, 1.0)
    model = translation_m @ rotation_m @ scale_m

    # Matriz da câmera
    camera_pos = np.array([0.0, 0.0,3.0], dtype=np.float32) #world pos
    camera_front = np.array([0.0, 0.0, -1.0], dtype=np.float32) #facing
    camera_up = np.array([0.0, 1.0, 0.0], dtype=np.float32) #up
    view = create_view(camera_pos,camera_front,camera_up)

    # Matriz de projeção
    projection = create_projection(45.0,window_width/window_height,0.1,100.0)

    # Criação dos shaders
    mvpshader = create_shader(GL_VERTEX_SHADER,"shadermvp.vert")
    fragshader = create_shader(GL_FRAGMENT_SHADER,"convolution.frag")

    shader_program = glCreateProgram()
    glAttachShader(shader_program,mvpshader)
    glAttachShader(shader_program,fragshader)
    glLinkProgram(shader_program)

    glUseProgram(shader_program)
    model_loc = glGetUniformLocation(shader_program,"model")
    view_loc = glGetUniformLocation(shader_program,"view")
    proj_loc = glGetUniformLocation(shader_program,"projection")
    glUniformMatrix4fv(model_loc,1,GL_FALSE,model.T.flatten())
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view.flatten())
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection.flatten())

    # variáveis para a convolução
    size_loc = glGetUniformLocation(shader_program,"texSize") #Tamanho da textura
    texture_loc = glGetUniformLocation(shader_program, "frameColor") # TODO COMMENTS
    use_kernel_loc = glGetUniformLocation(shader_program,"useKernel") # Se terá efeito
    grey_color_loc = glGetUniformLocation(shader_program,"greyColor") # Determina se a textura será cinza ou não
    glUniform1i(texture_loc, 0)
    glUniform1i(use_kernel_loc,False)
    glUniform1f(grey_color_loc,0.0)
    glUniform2fv(size_loc,1,np.array([1.0/tex_width,1.0/tex_height],dtype=np.float32))

    #Espeficamos as operações de viewport
    glViewport(0, 0, window_width, window_height)

    # Variáveis iniciais para a camera com o mouse
    first_mouse = True
    yaw = -90.0
    pitch = 0
    last_y = 300
    last_x = 400
    rot_x = rot_y = 0.0
    gray_color_bool = False
    time_checker_status = False

    # Comento depois TODO
    glEnable(GL_DEPTH_TEST)

    fps_counter = FPSCounter(average_over=30, stats_interval=5.0)
    fps_counter.initialize_text_rendering(window_width, window_height)
    fps_counter.enable_stats_printing(False)

    # Define a cor de fundo da janela
    glClearColor(0.3, 0.3, 0.3, 1.0)

    # 4. Loop de Renderização Principal
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        fps_counter.update()
        
        keys_input()

        #Definicao da matriz de projeção
        glUseProgram(shader_program)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D,texture_id)
        glUniform1i(texture_loc,0)

        #Refazer a rotação TODO or not TODO (seilá se é para ser assim)
        rotation_x = create_rotation(rot_x,"x")
        rotation_y = create_rotation(rot_y,"y")
        rotation_z = create_rotation(0.0,"z")
        rotation_m = rotation_x @ rotation_y @ rotation_z

        model = translation_m @ rotation_m @ scale_m
        view = create_view(camera_pos, camera_front, camera_up)
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model.T.flatten())
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view.flatten())
        
        glBindVertexArray(vao_qua)
        time_checker()
        glDrawArrays(GL_TRIANGLES,0,6)
        glBindTexture(GL_TEXTURE_2D,0)
        glBindVertexArray(0)

        fps_counter.render_fps(x=10, y=window_height - 30, size=2.0, color=(1.0, 1.0, 0.0))
        glUseProgram(0)

        # Troca os buffers front e back para exibir a imagem renderizada
        glfw.swap_buffers(window)
        # Verifica e processa eventos da janela
        glfw.poll_events()


    # 5. Finalização
    glfw.terminate()
    glDeleteVertexArrays(1,vao_qua)
    glDeleteBuffers(1,vbo_qua)
    glDeleteTextures(1,[texture_id])
    glDeleteProgram(shader_program)
    glDeleteShader(mvpshader)
    glDeleteShader(fragshader)

def keys_input():
    """
    Essa função é basicamente o que controla os inputs da camera
    Ela não é um callback devido não ser possível se mover repetidamente
    com um uníco aperto da tecla
    """
    global camera_pos,camera_front,camera_up,window,rot_x,rot_y
    camera_speed = 0.05

    w = glfw.get_key(window,glfw.KEY_W)
    s = glfw.get_key(window,glfw.KEY_S)
    a = glfw.get_key(window,glfw.KEY_A)
    d = glfw.get_key(window,glfw.KEY_D)
    space = glfw.get_key(window,glfw.KEY_SPACE)
    shift = glfw.get_key(window,glfw.KEY_LEFT_SHIFT)
    up = glfw.get_key(window,glfw.KEY_UP)
    down = glfw.get_key(window,glfw.KEY_DOWN)
    left = glfw.get_key(window,glfw.KEY_LEFT)
    right = glfw.get_key(window,glfw.KEY_RIGHT)

    if w == glfw.PRESS:
        camera_pos += camera_speed * camera_front
    if s == glfw.PRESS:
        camera_pos -= camera_speed * camera_front
    if a == glfw.PRESS:
        left_matrix = np.cross(camera_front,camera_up)
        camera_pos -= left_matrix / np.linalg.norm(left_matrix) * camera_speed
    if d == glfw.PRESS:
        right_matrix = np.cross(camera_front,camera_up)
        camera_pos += right_matrix / np.linalg.norm(right_matrix) * camera_speed
    if space == glfw.PRESS:
        camera_pos -= camera_speed * camera_up
    if shift == glfw.PRESS:
        camera_pos += camera_speed * camera_up
    if up == glfw.PRESS:
        rot_x += 0.05
    if down == glfw.PRESS:
        rot_x -= 0.05
    if left == glfw.PRESS:
        rot_y += 0.05
    if right == glfw.PRESS:
        rot_y -= 0.05

def mouse_callback(window,xpos,ypos):
    """
    Callback da câmera. 
    """
    global first_mouse, camera_front,yaw,pitch,last_x,last_y
    
    #Checagem inicial
    #
    if (first_mouse):
        last_x = xpos
        last_y = ypos
        first_mouse = False

    # o offset vai ser usado para mudar a posição da camera
    x_offset = xpos - last_x
    y_offset = last_y - ypos
    last_y = ypos
    last_x = xpos

    sensitivity = 0.1
    #Multiplica pela sensitividade para gerenciar a velocidade da camera
    x_offset *= sensitivity
    y_offset *= sensitivity

    #Yaw é a esquerda e a direita e o pitch cima e baixo
    yaw += x_offset
    pitch += y_offset

    # ifs para evitar dar um 360 
    if pitch > 89.0:
        pitch = 89.0
    if pitch < -89.0:
        pitch = -89.0

    x = math.cos(math.radians(yaw)) * math.cos(math.radians(pitch))
    y = math.sin(math.radians(pitch))
    z = math.sin(math.radians(yaw)) * math.cos(math.radians(pitch))
    direction = np.array([x, y, z], dtype=np.float32)
    # Normaliza para evitar lentidão ao olhar por um ângulo
    camera_front = direction / np.linalg.norm(direction)

def keys_callback(window,key,scancode,action,mods):
    """
    Callback do kernel
    """
    global shader_program,start_time,time_checker_status

    if action == glfw.PRESS:
        use_kernel_loc = glGetUniformLocation(shader_program,"useKernel")
        if key == glfw.KEY_R: # Reset básico apenas do kernel
            glUseProgram(shader_program)
            glUniform1i(use_kernel_loc,False)
            glUseProgram(0)
        else:
            match(key): # gerencia os filtros (Coloca eles no frag shader e inicia o tempo)
                case glfw.KEY_1:
                    kernel = np.array([[1/16,1/8,1/16],[1/8,1/4,1/8],[1/16,1/8,1/16]],
                      dtype=np.float32) # Blur Gaussian 
                    print("Kernel:kernel blur")
                case glfw.KEY_2:
                    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],dtype=np.float32) # Sharpen
                    print("Kernel:kernel sharpen")
                case glfw.KEY_3:
                    kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],dtype=np.float32) # Edge detection
                    print("Kernel:kernel edge detection")
                case glfw.KEY_4:
                    kernel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]], # Sobel Kernel
                      dtype=np.float32)
                    print("Kernel:kernel sobel")
                case glfw.KEY_5:
                    kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]], # High boost
                      dtype=np.float32)
                    print("Kernel:kernel high boost")
                case _:
                    return
            glUseProgram(shader_program)
            glUniform1i(use_kernel_loc,True)
            kernel_loc = glGetUniformLocation(shader_program,"kernel")
            glUniformMatrix3fv(kernel_loc,1,GL_FALSE,kernel)
            glUseProgram(0)
            time_checker_status = True
            start_time = time.time()

def mouse_button_callback(window,button,action,mods):
    """
    Callback dos botões do mouse
    """

    global translation_m,rotation_x,rotation_y,rotation_z,scale_m,camera_pos,camera_front,camera_up
    global first_mouse,yaw,pitch,last_x,last_y,rot_x,rot_y,shader_program,gray_color_bool

    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS: # Tons de cinza
        grey_color_loc = glGetUniformLocation(shader_program,"greyColor")
        glUseProgram(shader_program)
        if gray_color_bool:
            glUniform1f(grey_color_loc,0.0)
            gray_color_bool = False
        else:
            glUniform1f(grey_color_loc,1.0)
            gray_color_bool = True
        glUseProgram(0)
    if button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.PRESS: # Reset completo
            # Matrizes do model
            scale_m = create_scale(2.0, 1.5, 1.0)
            rotation_x = create_rotation(0.0,"x")
            rotation_y = create_rotation(0.0,"y")
            rotation_z = create_rotation(0.0,"z")
            translation_m = create_translation(0.0, 0.0, 1.0)
            
            # Câmera
            camera_pos = np.array([0.0, 0.0,3.0], dtype=np.float32) #world pos
            camera_front = np.array([0.0, 0.0, -1.0], dtype=np.float32) #facing
            camera_up = np.array([0.0, 1.0, 0.0], dtype=np.float32) #up

            first_mouse = True
            yaw = -90.0
            pitch = 0
            last_y = 300
            last_x = 400
            rot_x = rot_y = 0.0

            glUseProgram(shader_program)
            use_kernel_loc = glGetUniformLocation(shader_program,"useKernel")
            glUniform1i(use_kernel_loc,False)
            glUseProgram(0)

def time_checker():
    """
    É uma função que calcula o tempo em que um filtro é aplicado em uma textura
    """
    global start_time,time_checker_status
    if time_checker_status:
        print(f"{(time.time() - start_time)} segundos para o nosso algoritmo")
        time_checker_status = False
if __name__ == "__main__":
    main()
