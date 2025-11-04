#version 330 core
out vec4 FragColor;

in vec2 TexCoords;

uniform sampler2D frameColor;

void main()
{   
    FragColor = texture2D(frameColor,TexCoords);
}