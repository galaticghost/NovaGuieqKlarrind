#include <stdio.h>

int main()
{
    // Declaração de uma variável do tipo long long int
    long long int numero_grande = 1234567890123456789LL;
    long long int numero_positivo = 9223372036854775807LL;             // Valor máximo possível para long long int com sinal
    unsigned long long int numero_sem_sinal = 18446744073709551615ULL; // Valor máximo para unsigned long long int

    // Exibindo os valores
    printf("Número grande (com sinal): %lld\n", numero_grande);
    printf("Número positivo (máximo com sinal): %lld\n", numero_positivo);
    printf("Número sem sinal (máximo): %llu\n", numero_sem_sinal);

    // Exemplo de uso com leitura
    unsigned long long int numero_lido;
    printf("Digite um número inteiro muito grande: ");
    scanf("%llu", &numero_lido);
    printf("Você digitou: %llu\n", numero_lido);

    return 0;
}