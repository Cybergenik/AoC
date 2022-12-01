#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
	FILE * fp;
	char * line = NULL;
	size_t len = 0;
	ssize_t read;

	fp = fopen("input.txt", "r");
	if (fp == NULL)
		exit(EXIT_FAILURE);
	int max_ = 0;
	int curr = 0;
	while ((read = getline(&line, &len, fp)) != -1) {
		if (!strcmp(line, "\n")){
			if (curr > max_)
				max_ = curr;
			curr = 0;
			continue;
		}
		curr += atoi(line);
	}
	printf("%d\n", max_);

	fclose(fp);
	if (line)
		free(line);
}
