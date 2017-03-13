#include <stdlib.h>
#include <stdio.h>

int sort(int vetor[]){
    printf("testes");
    return 0;

}


int main(){
    int vet[] = {9,10,7,1,2};
    int tam = sizeof(vet)/sizeof(int);
    for(int i = 0; i < tam; i++){
        for(int j = 0; j < tam; j++){
            if(vet[j] > vet[j + 1 ]){
                int aux = vet[j];
                vet[j] = vet[j + 1];
                vet[j + 1] = aux;
            }
        }
    }
    for(int i = 0; i < tam; i++){
        printf("%i - ", vet[i]);
    }
    return 0;
}
