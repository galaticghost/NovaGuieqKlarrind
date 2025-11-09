#version 330 core

out vec4 FragText;
in vec2 vTex;
uniform sampler2D frameColor;

void main()
{   
    FragText = texture2D(frameColor,vTex);
}