#ifndef DEFINED_DATA_H
#define DEFINED_DATA_H
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int** Matrix;
	int m;
	int n;
	int minel;
	int minel_posi;
	int minel_posj;
} arr_2d;

extern arr_2d* matr_ptr;
#endif //DEFINED_DATA_H
