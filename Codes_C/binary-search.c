#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    clock_t t_inicio, t_fim;
    t_inicio = clock();
    int vetor[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13};
    int n, k, fim, inicio, aux, cont;
    n = sizeof(vetor)/sizeof(int);
    printf("Qual valor deseja buscar?: ");
    scanf("%i", &k);
    inicio, cont = 0, 0;
    fim = n-1;
    aux = (inicio + fim) / 2;
    while (inicio <= fim){
        if(vetor[aux] < k){
            inicio = aux + 1;
            cont += 1;
        } else if(vetor[aux] == k) {
            printf("Found! Position: %d\n", aux+1);
            printf("Count: %d\n", cont);
            break;
        } else {
            fim = aux - 1;
            cont += 1;
        }
        aux = (inicio + fim) / 2;
    }
    if (inicio > fim){
        printf("Not found.\n");
        printf("Count: %d\n", cont);
    }
    t_fim = clock();
    printf("Time: %f", (((t_fim - t_inicio) * 1000.0)) / CLOCKS_PER_SEC);
    return 0;
}
