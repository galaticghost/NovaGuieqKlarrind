#version 330 core

in vec2 vTex;
uniform sampler2D frameColor;
uniform mat3 kernel;
uniform vec2 texSize;
uniform bool useKernel;
uniform float greyColor;

out vec4 FragColor;

void main()
{   
    vec3 result = vec3(0,0,0);
    if (useKernel){
        for (int y = -1; y <= 1; y++) {
            for (int x = -1; x <= 1; x++) {
                vec2 offset = vec2(x, y) * texSize;    
                vec3 sampleColor = texture(frameColor, vTex + offset).rgb; 
                float weight = kernel[x+1][y+1];         
                result += sampleColor * weight;    
            }
        }
        result = clamp(result, 0.0, 1.0); // Clamp para não ultrapassar o valor máximo de 1 nas cores
    } else {
        result = texture(frameColor,vTex).rgb;
    }
    float grey = 0.21 * result.r + 0.71 * result.g + 0.07 * result.b; // Variável para coloração cinza
    FragColor = vec4(result.rgb * (1.0 - greyColor) + (grey * greyColor), 1.0);
}