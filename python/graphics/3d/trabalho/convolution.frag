#version 330 core

in vec2 vTex;
uniform sampler2D frameColor;
uniform mat3 kernel;
uniform vec2 texSize; // 
uniform bool useKernel; // Bool para ver se será aplicado um filtro na texxtura
uniform float greyColor;

out vec4 FragColor;

void main()
{   
    vec3 result = vec3(0,0,0);
    /*mat3 kernel = mat3(0);
    if (x == 1) {
        kernel = mat3(1/16,1/8,1/16,
        1/8,1/4,1/8,
        1/16,1/8,1/16)
    }*/
    if (useKernel){
        // Loop para pegar os pixeis vizinhos
        for (int y = -1; y <= 1; y++) {
            for (int x = -1; x <= 1; x++) {
                // O offset é o pixel * o tamanho para o próximo pixel no deslocamento uv
                vec2 offset = vec2(x, y) * texSize;    
                // Recebe na textura a coordenada uv + o deslocamento
                vec3 sampleColor = texture(frameColor, vTex + offset).rgb; 
                float weight = kernel[y+1][x+1];
                // Multiplica o vizinho pelo seu valor correspondente no kernel e faz a soma no result
                result += sampleColor * weight;    
            }
        }
        result = clamp(result, 0.0, 1.0); // Clamp para não ultrapassar o valor máximo de 1 nas cores
    } else {
        // Se não for utilizado um filtro
        result = texture(frameColor,vTex).rgb;
    }
    // Variável para coloração cinza, converte os canais rgb para cinze
    float grey = 0.21 * result.r + 0.71 * result.g + 0.07 * result.b;
    // Se o greyColor for 0.0, a cor do pixel será normal, mas se for 1.0 a cor será cinza
    FragColor = vec4(result.rgb * (1.0 - greyColor) + (grey * greyColor), 1.0);
}