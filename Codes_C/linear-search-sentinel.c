#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int search(int vetor[], int n, int k){
    int i = 0;
    int ult = vetor[n-1];
    vetor[n-1] = k;
    while(vetor[i] != k){
        i++;
    }
    vetor[n-1] = ult;
    if(i < n || vetor[n-1] == k){
        return 1;
    }
    return -1;
}

int main(){
    clock_t inicio, fim;
    inicio = clock();
    int n, k, resp;
    int vetor[20] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19};

    n = sizeof(vetor)/sizeof(int);
    printf("Qual valor quer buscar? ");
    scanf("%d", &k);
    inicio = clock();
    resp = search(vetor, n, k);
    if(resp == 1){
        printf("Valor encontrado.");
    }else {
        printf("Achou não parsa.\n");
    }
    fim = clock();
    printf("Time: %f\n", (((fim-inicio) * 1000.00))/CLOCKS_PER_SEC);
    return 0;
}
