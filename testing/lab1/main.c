#include <stdio.h>

#include "matrix.h"

int main() {
	u_int N;
	printf("Input N: ");
	scanf("%d", &N);

	if (N < 1) {
		printf("Invalid N value");
		return 0;
	}

	int* matrix = scan_matrix(N);

	printf("\nInput matrix:\n");
	print_matrix(matrix, N);

	sort_main_diagonal(matrix, N);
	printf("\nMatrix with sorted main diagonal:\n");
	print_matrix(matrix, N);
}