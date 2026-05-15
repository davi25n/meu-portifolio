#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    printf("qual o texto a ser analisado? ");
    char texto[1000];
    fgets(texto, sizeof(texto), stdin);
    int caracteres = 0;
    int palavras = 1;
    int frases = 0;
    int indice = 0;
    for (int i = 0, n = strlen(texto); i < n; i++)
    {
        if (texto[i] == 'q' || texto[i] == 'w' || texto[i] == 'e' || texto[i] == 'r' || texto[i] == 't' || texto[i] == 'y' || texto[i] == 'u' || texto[i] == 'i' || texto[i] == 'o' || texto[i] == 'p' || texto[i] == 'a' || texto[i] == 's' || texto[i] == 'd' || texto[i] == 'f' || texto[i] == 'g' || texto[i] == 'h' || texto[i] == 'j' || texto[i] == 'k' || texto[i] == 'l' || texto[i] == 'z' || texto[i] == 'x' || texto[i] == 'c' || texto[i] == 'v' || texto[i] == 'b' || texto[i] == 'n' || texto[i] == 'm' || texto[i] == 'Q' || texto[i] == 'W' || texto[i] == 'E' || texto[i] == 'R' || texto[i] == 'T' || texto[i] == 'Y' || texto[i] == 'U' || texto[i] == 'I' || texto[i] == 'O' || texto[i] == 'P' || texto[i] == 'A' || texto[i] == 'S' || texto[i] == 'D' || texto[i] == 'F' || texto[i] == 'G' || texto[i] == 'H' || texto[i] == 'J' || texto[i] == 'K' || texto[i] == 'L'|| texto[i] == 'Z' || texto[i] == 'X' || texto[i] == 'C' || texto[i] == 'V' || texto[i] == 'B' || texto[i] == 'N' || texto[i] == 'M'){
            caracteres++;
        }
        else if (texto[i] == ' '){
            palavras++;
        }
        else if (texto[i] == '.' || texto[i] == '!' || texto[i] == '?'){
            frases++;
        }
    }
    indice = 0.0588*100*(caracteres/palavras) - 0.296*100*(frases/palavras) - 15.8;
    indice = round(indice);
    if (indice <= 1){
        printf("texto com nível de leitura: before grade 1\n");
    }
    else if (indice == 2){
        printf("texto com nível de leitura: grade 2\n");
    }
    else if (indice == 3){
        printf("texto com nível de leitura: grade 3\n");
    }
    else if (indice == 4){
        printf("texto com nível de leitura: grade 4\n");
    }
    else if (indice == 5){
        printf("texto com nível de leitura: grade 5\n");
    }
    else if (indice == 6){
        printf("texto com nível de leitura: grade 6\n");
    }
    else if (indice == 7){
        printf("texto com nível de leitura: grade 7\n");
    }
    else if (indice == 8){
        printf("texto com nível de leitura: grade 8\n");
    }
    else if (indice == 9){
        printf("texto com nível de leitura: grade 9\n");
    }
    else if (indice == 10){
        printf("texto com nível de leitura: grade 10\n");
    }
    else if (indice == 11){
        printf("texto com nível de leitura: grade 11\n");
    }
    else if (indice == 12){
        printf("texto com nível de leitura: grade 12\n");
    }
    else if (indice == 13){
        printf("texto com nível de leitura: grade 13\n");
    }
    else if (indice == 14){
        printf("texto com nível de leitura: grade 14\n");
    }
    else if (indice == 15){
        printf("texto com nível de leitura: grade 15\n");
    }
    else {
        printf("texto com nível de leitura: grade 16+\n");
    }
}
