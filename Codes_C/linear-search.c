#include <stdlib.h>
#include <stdio.h>


int search(int vetor[], int n, int k){
    for(int i = 0; i < n; i++){
        if(vetor[i] == k){
            return 1;
        }
    }
    return -1;
}

int main(){

    int vetor[5], n, k, resp;
    printf("Entre com 5 valores inteiros: ");
    for(int y = 0; y < 5; y++){
        scanf("%d", &vetor[y]);
    }

    n = sizeof(vetor)/sizeof(int);
    printf("Qual valor deseja buscar? ");
    scanf("%d", &k);

    resp = search(vetor, n, k);
    if(resp != -1){
        printf("O valor está no vetor.\n");
    }else {
        printf("O valor não está no vetor.\n");
    }
}
