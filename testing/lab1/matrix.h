#ifndef MATRIX
#define MATRIX

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include <float.h>

typedef int mdata;
#define MDATA_MIN INT_MIN;

typedef unsigned int u_int;

mdata* scan_matrix(u_int N) {
	if (N < 0) return NULL;

	mdata* matrix = (mdata*) malloc(sizeof(mdata) * N * N);

	int success = 1;
	u_int i;
	for (i = 0; i < N * N; ++i) {
		success = scanf("%d", matrix + i);
		if (!success) {
			printf("\nInvalid value\n");
			free(matrix);
			return NULL;
		}
	}

	return matrix;
}

mdata matrix_max(mdata* matrix, u_int N) {
	mdata max = MDATA_MIN;
	u_int i;
	for (i = 0; i < N * N; ++i) {
		if (matrix[i] > max) max = matrix[i];
	}
	return max;
}

u_int nrank(mdata n) {
	n = abs(n);
	u_int rank = 0;

	while (n > 0) {
		n /= 10;
		rank++;
	}

	return rank;
}

void print_matrix(mdata* matrix, u_int N) {
	mdata max = nrank(matrix_max(matrix, N));
	char* format = (char*) malloc(8);
	sprintf(format, " %dd ", max + 2);
	format[0] = '%';

	u_int i;
	for (i = 0; i < N * N; ++i) {
		printf(format, matrix[i]);
		if (!((i + 1) % N)) printf("\n");
	}
}

void sort_main_diagonal(mdata* matrix, u_int N) {
	/* bubble sort main diagonal */
	u_int i, j;
	for (i = 0; i < N; ++i) {
		for (j = 0; j < N - 1; ++j) {
			if (matrix[j * N + j] > matrix[(j + 1) * N + j + 1]) {
				mdata tmp = matrix[j * N + j];
				matrix[j * N + j] = matrix[(j + 1) * N + j + 1];
				matrix[(j + 1) * N + j + 1] = tmp;
			}
		}
	}
}

#endif