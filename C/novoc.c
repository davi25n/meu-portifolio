#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    float primeirovalor, segundovalor, resultado;
    char operador[100];
    printf("Digite o primeiro valor: ");
    scanf("%f", &primeirovalor);
    printf("Digite o segundo valor: ");
    scanf("%f", &segundovalor);
    printf("Digite o operador: ");
    scanf("%s", operador);
    if (strcmp(operador, "+") == 0) {
        resultado = primeirovalor + segundovalor;
        printf("O resultado da soma : %.0f\n", resultado);
    } else if (strcmp(operador, "-") == 0) {
        resultado = primeirovalor - segundovalor;
        printf("O resultado da subtração : %.0f\n", resultado);
    } else if (strcmp(operador, "*") == 0) {
        resultado = primeirovalor * segundovalor;
        printf("O resultado da multiplicação : %.0f\n", resultado);
    } else if (strcmp(operador, "/") == 0) {
        if (segundovalor != 0) {
            resultado = primeirovalor / segundovalor;
            printf("Resultado da divisão : %.2f\n", resultado);
        } else {
            printf("Erro: Divisão por zero não é permitida.\n");
        }
    } else {
        printf("Erro: Operador inválido. Por favor, use +, -, *, ou /.\n");
    }
}