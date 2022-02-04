#include "common_data.h"
#include "func_signatures.h"

void handler_func(arr_2d* mtrx, char isdebug)
{
	if (isdebug == 'd')
		printf(" Handler function has been started in debug mode\n --------------\n");
	int buffer;
	for (int j = 0; j < mtrx->n; j++)
	{
		buffer = mtrx->Matrix[0][j];
		mtrx->minel_posi = 0;
		mtrx->minel_posj = j;
		if (isdebug == 'd')
			printf(" Zero element of [%d] column recorded in buffer\n .\t.\t.\t\n", j);
		for (int i = 0; i < mtrx->m; i++)
		{
			if (mtrx->Matrix[i][j] <= buffer)
			{
				buffer = mtrx->Matrix[i][j];
				mtrx->minel_posi = i;
			}
		}
		if (isdebug == 'd')
			printf(" In column [%d] was finded minimum element = %d,     pos = [%d][%d]\n --------------\n", j, buffer, mtrx->minel_posi, mtrx->minel_posj);
	}
	if (isdebug == 'd')
		printf(" Handler function has been finished\n\n");

	mtrx->minel = buffer;
}
