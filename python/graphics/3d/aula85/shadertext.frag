#version 330 core

in vec2 TexCoords;
out vec4 color;

uniform sampler2D frameColor;

void main() {
    color = texture2D(frameColor,TexCoords);
}