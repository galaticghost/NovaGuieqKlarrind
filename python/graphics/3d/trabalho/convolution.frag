#version 330 core

in vec2 vTex;
uniform sampler2D frameColor;
uniform mat3 kernel;
uniform vec2 texSize;

out vec4 FragColor;

void main()
{   
    vec3 result = vec3(0,0,0); // Vetor vazio para colocar a textura modificada pelo kernel

    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 offset = vec2(x, y) * texSize;    
            vec3 sampleColor = texture(frameColor, vTex + offset).rgb; 
            float weight = kernel[y+1][x+1];         
            result += sampleColor * weight;    
        }
    }
    result = clamp(result, 0.0, 1.0); // Clamp para não ultrapassar o valor máximo de 1
    FragColor = vec4(result, 1.0);
}