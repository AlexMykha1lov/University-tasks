#include "common_data.h"
#include "func_signatures.h"
#include <stdbool.h>
#include <unistd.h>


void matr_init(arr_2d *mtrx)
{
	mtrx->Matrix = (int**)malloc(mtrx->m * sizeof(int*));
	for (int i = 0; i < mtrx->m; i++)
		mtrx->Matrix[i] = (int*)malloc(mtrx->n * sizeof(int));
}

void matr_free(arr_2d* mtrx)
{
	for (int i = 0; i < mtrx->m; i++)
		free(mtrx->Matrix[i]);
	free(mtrx->Matrix);
}

void help()
{
	printf("\n . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .");
	printf("\n Mandatory options:");
	printf("\n -i  -  'm' dimension value (m > 0)");
	printf("\n -j  -  'n' dimension value (n > 0)\n");
	printf("\n Input settings:");
	printf("\n -r  -  random input");                
	printf("\n -s  -  sorted input");              
	printf("\n -m  -  manual input (default option)\n");
	printf("\n Output settings:");
	printf("\n -o  -  without matrix output (default option is with matrix output)");
	printf("\n -e  -  release output (default option)");
	printf("\n -d  -  debugging output");
	printf("\n . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .");
}

int main(int argc, char *argv[])
{
	arr_2d matr;
	arr_2d* matr_ptr = &matr;

	char buffer;
	char options[] = {'m', 'e', '?'}; // default options initialization
	bool check_i = false; // necessary options
	bool check_j = false; // input check
	while ((buffer = getopt(argc, argv, "hi:j:rsmoed")) != -1)
	{
		switch (buffer)
		{
			case 'i':
				if((matr_ptr->m = atoi(optarg)) > 0)
					check_i = true;
				else 
				{
					printf("\n ERROR!\n Matrix dimension must be a possitive number!\n\n");
					return 1;
				}
				break;

			case 'j':
				if((matr_ptr->n = atoi(optarg)) > 0)
					check_j = true;
				else
				{
					printf("\n ERROR!\n Matrix dimension must be a possitive number!\n\n");
					return 1;
				}
				break;

			default:
				if ((buffer == 'r') || (buffer == 's') || (buffer == 'm'))
					options[0] = buffer;
				else if ((buffer == 'e') || (buffer =='d'))
					options[1] = buffer;
				else if (buffer == 'o')
					options[2] = 'o';
				else if (buffer == 'h')
				{
					help();
					return 0;
				}
				else printf("\n Was entered wrong option \'%c\'\n Restart program with -h key for help", buffer);
				break;
		}
	}

	if (check_i && check_j)
	{
		matr_init(matr_ptr);
		switch (options[0])
		{
			case 'r':
				random_in(matr_ptr);
				break;

			case 's':
				sorted_in(matr_ptr);
				break;

			case 'm':
				manual_in(matr_ptr);
				break;
		}
		handler_func(matr_ptr, options[1]);
		if (options[2] != 'o')
			output(matr_ptr);
		printf("\n Last minimum element = %d was finded in [%d][%d]\n\n", matr_ptr->minel, matr_ptr->minel_posi / 100, matr_ptr->minel_posj % 100);
		matr_free(matr_ptr);
	}
	else if(!check_i)
		printf("\n The value of \'m\' was not entered");
    else
        printf("\n The value of \'n\' was not entered");

	return 0;
}
