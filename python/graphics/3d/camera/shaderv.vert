#version 330 core
// Entrada: Posição do Vértice (Attribute)
layout (location = 0) in vec3 aPos;
// Entrada: Única Matriz (Uniform)
uniform mat4 uMVP;
void main()
{
    // Multiplica a MVP (4x4) pela posição (4x1) do vértice
    // O resultado é a posição no Clip Space (gl_Position)
    gl_Position = uMVP * vec4(aPos, 1.0);
}