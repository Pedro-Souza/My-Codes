#include <stdio.h>
#include <time.h>

int main () {
	clock_t inicio, fim;
	int i;
	double result;
	inicio = clock();
	for(i; i < 10000; i++) {
		printf("%d\n", i);
	}
	fim = clock();
	printf("Time: %f\n", (((fim-inicio) * 1000.0))/CLOCKS_PER_SEC);
	return 0;
}