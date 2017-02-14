#include <stdio.h>
#include <stdlib.h>


int search(int vetor[], int n, int k){
    int i = 0;
    vetor[n] = k;
    while(vetor[i] != k){
        i++;
    }
    if(i < n){
        return 1;
    }
    return -1;
}

int main(){
    int vetor[4], n, k, resp;
    printf("Digite valores inteiros:\n ");
    for(int i = 0; i < 4; i++ ){
        scanf("%d", &vetor[i]);
    }
    n = sizeof(vetor)/sizeof(int);
    printf("Qual valor quer buscar? ");
    scanf("%d", &k);
    resp = search(vetor, n, k);
    if(resp == 1){
        printf("Valor encontrado.");
    }else {
        printf("Achou não parsa.");
    }
    return 0;
}
