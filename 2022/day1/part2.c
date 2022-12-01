#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmpfunc (const void *a, const void *b){
	return (*(int*)b - *(int*)a);
}

int main() {
	FILE * fp;
	char * line = NULL;
	size_t len = 0;
	ssize_t read;

	fp = fopen("input.txt", "r");
	if (fp == NULL)
		exit(EXIT_FAILURE);
	int all[1000];
	int curr = 0;
	int N = 0;
	while ((read = getline(&line, &len, fp)) != -1) {
		if (!strcmp(line, "\n")){
			all[N] = curr;
			curr = 0;
			N++;
			continue;
		}
		curr += atoi(line);
	}
	all[N] = curr;
	N++;
	qsort(all, N, sizeof(int), cmpfunc);
	printf("%d\n", all[0]+all[1]+all[2]);

	fclose(fp);
	if (line)
		free(line);
}
