#include <stdio.h>

int main(void)
{
    printf("Digite o tamanho do quadrado: ");
    int tamanho;
    scanf("%i", &tamanho);
    for (int n = 0; n < tamanho; n++)
    {
        if ( n == 0 || n == tamanho -1)
        {
            for (int i = 0; i < tamanho; i++)
            {
                printf("#");
            }
            printf("\n");
        }
        else
        {
            printf("#");
            for (int j = 0; j < tamanho - 2; j++)
            {
                printf(" ");
            }
            printf("#\n");
        }
    }
}