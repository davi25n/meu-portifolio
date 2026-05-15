#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    char nome[40];
    int votos;
}
candidatos;
// definição da estrutura candidatos
int main(int argc, char *argv[])
{
        typedef struct
    {
        char candvotado[40][argc - 1];
    }
    votantes;
    //votantes é a estrutura que guarda os votos dos eleitores
    candidatos candidato[argc - 1];
    for (int i = 0; i < argc - 1; i++)
    {
        strcpy(candidato[i].nome, argv[i + 1]);
        candidato[i].votos = 0;
    }
    int eleitores;//eleitores é a quantidade de pessoas que votarão
    printf("quantos eleitores? ");
    scanf("%i", &eleitores);
    votantes eleitor[eleitores];//eleitor é o array que guarda os votos de cada eleitor separadamente
    for (int i = 0; i < eleitores; i++)
    {
        for (int j = 0; j < argc - 1; j++)
        {
            int valido = 0;
            printf("%iº voto do eleitor %i para? ", j + 1, i + 1);
            char voto[40];
            scanf("%s", voto);
            strcpy(eleitor[i].candvotado[j], voto);
            for (int k = 0; k < argc - 1; k++)
            {
                if (strcmp(voto, candidato[k].nome) == 0)
                {
                    valido++;
                    break;
                }
            }
            if (valido == 0)
            {
                j--;
                printf("candidato invalido\n");
            }
        }
    }
    int maisvoto = candidato[0].votos;
    int candidatocommaisvoto = 0;
    int menosvoto = candidato[0].votos;
    int candidatocommenosvoto = 0;
    int candidatoseliminados = 0;
    for (int i = 0; i < argc - 1; i++)//primeira analise dos votos de cada candidato para cada eleitor
    {
        for (int j = 0; j < eleitores; j++)//analise dos votos de cada eleitor para cada candidato
        {
            for (int k = 0; k < argc - (1 + candidatoseliminados); k++)//analise candidato por candidato
            {
                 if (strcmp(eleitor[i].candvotado[j], candidato[k].nome) == 0)
                 {
                     candidato[k].votos++;
                 }
            }
        }
        for (int k = 0; k < argc - (1 + candidatoseliminados); k++)//analise de quem tem mais votos
        {
            if (candidato[k].votos > maisvoto)
            {
                maisvoto = candidato[k].votos;
                candidatocommaisvoto = k;
            }
            else if (candidato[k].votos < menosvoto)
            {
                menosvoto = candidato[k].votos;
                candidatocommenosvoto = k;
            }
        }
        if (maisvoto > eleitores / 2)//verificação se o candidato tem mais de 50% dos votos
        {
            printf("o vencedor é %s com %i votos", candidato[candidatocommaisvoto].nome, candidato[candidatocommaisvoto].votos);
            return 0;
        }
        else
        {
            if (i == candidatocommenosvoto)
            {
                strcpy(candidato[i].nome, candidato[argc].nome);
                candidato[i].votos = 0;
            }
            else if (i > candidatocommenosvoto)
            {
                strcpy(candidato[i - 1].nome, candidato[i].nome);
                candidato[i - 1].votos = candidato[i].votos;
            }
            candidatoseliminados++;
        }
    }
    printf("o vencedor é %s", candidato[candidatocommaisvoto].nome);
    return 0;
}
