#include "common_data.h"
#include "func_signatures.h"
#include <time.h>

void random_in(arr_2d *mtrx)
{
	srand(time(NULL));
	for (int i = 0; i < mtrx->m; i++)
		for (int j = 0; j < mtrx->n; j++)
			mtrx->Matrix[i][j] = rand() % 100;
}

void sorted_in(arr_2d* mtrx)
{
	int num = 0;
	for (int i = 0; i < mtrx->m; i++)
		for (int j = 0; j < mtrx->n; j++)
		{
			mtrx->Matrix[i][j] = num;
			num++;
		}
}

void manual_in(arr_2d* mtrx)
{
	for (int i = 0; i < mtrx->m; i++)
		for (int j = 0; j < mtrx->n; j++)
		{
			printf("\n Enter a [%d][%d] element: ", i, j);
			scanf("%d", &mtrx->Matrix[i][j]);
		}
}

void output(arr_2d* mtrx)
{
	printf("\n\n Processed matrix:\n");
	for (int i = 0; i < mtrx->m; i++)
	{
		for (int j = 0; j < mtrx->n; j++)
			printf("\t%d", mtrx->Matrix[i][j]);
		printf("\n");
	}
}
