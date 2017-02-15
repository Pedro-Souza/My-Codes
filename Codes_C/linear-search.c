#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int search(int vetor[], int n, int k){
    for(int i = 0; i < n; i++){
        if(vetor[i] == k){
            return 1;
        }
    }
    return -1;
}

int main(){
    clock_t inicio, fim;
    inicio = clock();
    int n, k, resp;
    int vetor[20] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19};
    //printf("Entre com 5 valores inteiros: ");
    //for(int y = 0; y < 5; y++){
    //    scanf("%d", &vetor[y]);
    //}

    n = sizeof(vetor)/sizeof(int);
    printf("Qual valor deseja buscar? ");
    scanf("%d", &k);

    resp = search(vetor, n, k);
    fim = clock();
    if(resp != -1){
        printf("O valor está no vetor.\n");
    }else {
        printf("O valor não está no vetor.\n");
    }
    printf("Time: %f\n", (((fim-inicio) * 1000.0))/CLOCKS_PER_SEC);
}
