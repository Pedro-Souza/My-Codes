#include <stdlib.h>
#include <stdio.h>

void sort(int vet[], int tam);

int main(){
    int vet[] = {9,10,7,1,2};
    int tam = sizeof(vet)/sizeof(int);
    sort(vet, tam);
    return 0;
}

void sort(int vet[], int tam){
    for(int i = 0; i < tam; i++){
        for(int j = 0; j < tam; j++){
            if(vet[j] > vet[j+1]){
                int aux = vet[j];
                vet[j] = vet[j+1];
                vet[j+1] = aux;
            }
        }
    }
    printf("Vetor ordenado.");
}
