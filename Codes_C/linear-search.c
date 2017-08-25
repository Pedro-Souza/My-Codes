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
    int n, k, resp;
    int vetor[20] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19};

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
