import glfw
from OpenGL.GL import *
import numpy as np
import math
from fps import FPSCounter
import cv2

def main():
    global camera_pos, camera_front, camera_up, window, first_mouse,yaw,pitch,last_x,last_y,rot_x,rot_y
    # 1. Initialize GLFW
    if not glfw.init():
        print("Erro: Não foi possível inicializar o GLFW.")
        return
    rot_x = rot_y = 0.0
    # Request OpenGL Core Profile 3.3
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    # glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.TRUE)  # Uncomment if needed (MacOS)

    # 2. Criação da Janela de Aplicação
    window = glfw.create_window(800, 600, "Quadrado", None, None)
    if not window:
        glfw.terminate()
        print("Erro: Não foi possível criar a janela GLFW.")
        return

    # Torna o contexto da janela o contexto atual do thread
    glfw.make_context_current(window)
    glfw.set_input_mode(window,glfw.CURSOR,glfw.CURSOR_DISABLED)
    glfw.set_cursor_pos_callback(window, mouse_callback)

    texture = cv2.imread('texture.webp',cv2.IMREAD_COLOR)
    texture = cv2.cvtColor(texture, cv2.COLOR_BGR2RGB)
    texture = cv2.flip(texture, 0)

    quadrado = np.array([0.3, 0.3, -1.0, 1.0, 1.0, # T1 V1
                        0.3, -0.3, -1.0, 1.0, 0.0, # T1 V2
                        -0.3, -0.3, -1.0, 0.0, 0.0, # T1 V3
                        -0.3, -0.3, -1.0, 0.0, 0.0, # T2 V1
                        -0.3, 0.3, -1.0, 0.0, 1.0, # T2 V2
                        0.3, 0.3, -1.0, 1.0, 1.0, # T2 V3
    ],dtype=np.float32)

    vao_qua, vbo_qua = setup_geometry(quadrado)

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D,texture_id)

    glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,640,587,0,GL_RGB, GL_UNSIGNED_BYTE,texture)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    

    camera_pos = np.array([0.0, 0.0,3.0], dtype=np.float32) #world pos
    camera_front = np.array([0.0, 0.0, -1.0], dtype=np.float32) #facing
    camera_up = np.array([0.0, 1.0, 0.0], dtype=np.float32) #up

    scale_m = create_scale(1.0, 1.0, 1.0)
    rotation_x = create_rotation(0.0,"x")
    rotation_y = create_rotation(0.0,"y")
    rotation_z = create_rotation(0.0,"z")
    rotation_m = rotation_x @ rotation_y @ rotation_z
    translation_m = create_translation(0.0, 0.0, 0.0)
    model = translation_m @ rotation_m @ scale_m
    view = create_view(camera_pos,camera_front,camera_up)
    projection = create_projection(45.0,800/600,0.1,100.0)

    mvpshader = create_shader(GL_VERTEX_SHADER,"shadermvp.vert")
    fragshader = create_shader(GL_FRAGMENT_SHADER,"shaderfrag.frag")

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

    texture_loc = glGetUniformLocation(shader_program, "frameColor")
    glUniform1i(texture_loc, 0)

    #Espeficamos as operações de viewport
    glViewport(0, 0, 800, 600)

    first_mouse = True
    yaw = -90.0
    pitch = 0
    last_y = 300
    last_x = 400

    glEnable(GL_DEPTH_TEST)

    fps_counter = FPSCounter(average_over=30, stats_interval=5.0)
    win_width, win_height = glfw.get_window_size(window)
    fps_counter.initialize_text_rendering(win_width, win_height)
    fps_counter.enable_stats_printing(True)

    # Define a cor de fundo da janela
    glClearColor(0.3, 0.3, 0.3, 1.0)

    # 4. Loop de Renderização Principal
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        fps_counter.update()
        keys()

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
        glDrawArrays(GL_TRIANGLES,0,6)
        glBindTexture(GL_TEXTURE_2D,0)
        glBindVertexArray(0)

        fps_counter.render_fps(x=10, y=win_height - 30, size=2.0, color=(1.0, 1.0, 0.0))
        glUseProgram(0)

        glfw.swap_buffers(window)
        # Verifica e processa eventos da janela
        glfw.poll_events()

        # Troca os buffers front e back para exibir a imagem renderizada


    # 5. Finalização
    glfw.terminate()
    glDeleteVertexArrays(1,vao_qua)
    glDeleteBuffers(1,vbo_qua)
    glDeleteTextures(1,[texture_id])
    glDeleteProgram(shader_program)
    glDeleteShader(mvpshader)
    glDeleteShader(fragshader)

def setup_geometry(vertex):
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)
    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertex.nbytes, vertex, GL_STATIC_DRAW)

    stride = 5 * vertex.itemsize

    # Atributo 0: Posição (3 floats)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # Atributo 1: UV (2 floats)
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
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        print(glGetShaderInfoLog(shader).decode())
    return shader

def create_view(camera_pos,camera_front,camera_up):
    z_axis = -camera_front / np.linalg.norm(camera_front)
    x_axis = np.cross(camera_up, z_axis)
    x_axis = x_axis / np.linalg.norm(x_axis)
    y_axis = np.cross(z_axis, x_axis)

    view = np.array([
    [x_axis[0], y_axis[0], z_axis[0], 0], #s
    [x_axis[1], y_axis[1], z_axis[1], 0], #u
    [x_axis[2], y_axis[2], z_axis[2], 0], #f
    [-np.dot(x_axis, camera_pos), -np.dot(y_axis, camera_pos), -np.dot(z_axis, camera_pos), 1]
    ], dtype=np.float32)
    return view

def create_projection(fov,aspect,near,far):
    f = 1.0 / math.tan(math.radians(fov) / 2.0)
    proj = np.zeros((4, 4), dtype=np.float32)

    proj[0, 0] = f / aspect
    proj[1, 1] = f
    proj[2, 2] = (far + near) / (near - far)
    proj[2, 3] = -1.0
    proj[3, 2] = (2.0 * far * near) / (near - far)
    return proj

def create_scale(fx,fy,fz):
    scale = np.array([[fx,0,0,0],[0,fy,0,0],[0,0,fz,0],[0,0,0,1]],dtype=np.float32)
    return scale

def create_rotation(angle,axis):
    c = math.cos(angle)
    s = math.sin(angle)

    if axis == 'x':
        return np.array([
            [1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)

    elif axis == 'y':
        return np.array([
            [c, 0, s, 0],
            [0, 1, 0, 0],
            [-s, 0, c, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)

    elif axis == 'z':
        return np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)

def create_translation(x,y,z):
    translation = np.array([[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]],dtype=np.float32)
    return translation

def keys():
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
        camera_pos += camera_speed * camera_up
    if shift == glfw.PRESS:
        camera_pos -= camera_speed * camera_up
    if up == glfw.PRESS:
        rot_x += 0.05
    if down == glfw.PRESS:
        rot_x -= 0.05
    if left == glfw.PRESS:
        rot_y += 0.05
    if right == glfw.PRESS:
        rot_y -= 0.05

def mouse_callback(window,xpos,ypos):
    global first_mouse, camera_front,yaw,pitch,last_x,last_y
    
    if (first_mouse):
        last_x = xpos
        last_y = ypos
        first_mouse = False

    x_offset = xpos - last_x
    y_offset = last_y - ypos
    last_y = ypos
    last_x = xpos

    sensitivity = 0.1
    x_offset *= sensitivity
    y_offset *= sensitivity

    yaw += x_offset
    pitch += y_offset

    if pitch > 89.0:
        pitch = 89.0
    if pitch < -89.0:
        pitch = -89.0

    x = math.cos(math.radians(yaw)) * math.cos(math.radians(pitch))
    y = math.sin(math.radians(pitch))
    z = math.sin(math.radians(yaw)) * math.cos(math.radians(pitch))
    direction = np.array([x, y, z], dtype=np.float32)
    camera_front = direction / np.linalg.norm(direction)

if __name__ == "__main__":
    main()
