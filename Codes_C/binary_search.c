#include <stdio.h>
#include <time.h>

void search(int vetor[], int inicio, int fim, int k){
    int aux, cont;
    cont = 0;
    aux = (inicio + fim) / 2;
    while(inicio <= fim){
        if(vetor[aux] < k){
            inicio = aux + 1;
            cont +=1;
        } else if(vetor[aux] == k){
            printf("Found! Position: %d\n", aux+1);
            printf("Count: %d\n", cont);
            break;
        } else {
            fim = aux - 1;
            cont += 1;
        }
        aux = (inicio + fim) / 2;
    }
    if(inicio > fim){
        printf("Not found.\n");
        printf("Count: %d\n", cont);
    }
}


int main(){
    int vetor[100], n;
    n = sizeof(vetor)/sizeof(int);
    for(int i = 0; i < n; i++ ){
        vetor[i] = i;
    }
    clock_t t_inicio, t_fim;
    t_inicio = clock();
    int k, inicio, fim;
    k = 99;
    inicio = 0;
    fim = n - 1;
    search(vetor, inicio, fim, k);
    t_fim = clock();
    printf("Time: %f", (((t_fim - t_inicio) * 1000.0)) / CLOCKS_PER_SEC);
    return 0;
}
