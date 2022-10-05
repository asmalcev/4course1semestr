#include <stdio.h>

#include "matrix.h"

void flush() {
	char c;
	while ((c = getchar()) != '\n' && c != EOF); 
}

void proccess() {
	u_int N;
	printf("Input N: ");
	int success = scanf("%d", &N);

	if (N < 1 || !success) {
		printf("Invalid N value\n");
		flush();
		return;
	}

	mdata* matrix = scan_matrix(N);

	if (matrix == NULL) {
		return;
	}

	printf("\nInput matrix:\n");
	print_matrix(matrix, N);

	sort_main_diagonal(matrix, N);
	printf("\nMatrix with sorted main diagonal:\n");
	print_matrix(matrix, N);
}

int main() {
	u_int Q;
	printf("Input Q: ");
	int success = scanf("%d", &Q);

	if (Q < 1 || !success) {
		printf("Invalid Q value\n");
		return 0;
	}

	while (Q > 0) {
		proccess();
		Q--;
	}
}