#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int total;
    do
    {
        printf("Digite o total de notas: ");
        scanf("%d", &total);
    } while (total <= 0);
    float nota[total];
    for (int i = 0; i < total; i++)
    {
        printf("Digite a nota %d: ", i + 1);
        scanf("%f", &nota[i]);
    }
    float media = 0;
    for (int j = 0; j < total; j++)
    {
        media += nota[j];
    }
    media /= total;
    printf("Média das notas: %.2f\n", media);
}