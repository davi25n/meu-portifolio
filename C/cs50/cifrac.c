#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int chave = atoi(argv[1]);
    printf("qual o texto a ser cifrado? ");
    char texto[1000];
    fgets(texto, sizeof(texto), stdin);
    for (int i = 0, n = strlen(texto); i < n; i++)
    {
        if ((texto[i] >= 'a' && texto[i] <= 'z') || (texto[i] >= 'A' && texto[i] <= 'Z'))
        {
            if (((texto[i]+chave) < 'a' && (texto[i]+chave) > 'Z') || (texto[i]+chave) > 'z')
            {
                texto[i] = texto[i] + (chave-26);
            }
            else
            {
                texto[i] = texto[i] + chave;
            }
        }
    }
    printf("texto cifrado:%s", texto);
    return 0;
}