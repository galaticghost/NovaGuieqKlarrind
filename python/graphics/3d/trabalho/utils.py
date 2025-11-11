from OpenGL.GL import *
import numpy as np
import math

def setup_geometry_uv(vertex):
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