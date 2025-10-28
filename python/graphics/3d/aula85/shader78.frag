#version 330 core
out vec4 FragColor;
in vec3 vColor;

uniform int colortime;

void main()
{   
    if (colortime == 0){
        FragColor = vec4(vColor, 1.0);
    } else {
        FragColor = texture2D(frameColor,TexCoords);
    }

}