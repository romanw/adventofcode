#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    FILE *fp = fopen("input.txt", "r");
    if(fp == NULL) {
        perror("Unable to open file!");
        exit(1);
    }

    // Read lines using POSIX function getline
    // This code won't work on Windows
    char *line = NULL;
    size_t len = 0;

	const int nbits = 12;
	int bitarray[nbits];
    int input;
    int mask;

    int i;
    for (i = 0; i < nbits; i++) bitarray[i] = 0;

    while(getline(&line, &len, fp) != -1) {
        input = (int) strtol(line, NULL, 2);
        i = 0;
        mask = 1 << (nbits - 1);
        while (mask > 0) {
        	if ((input & mask) == 0) {
        		bitarray[i] -= 1;
        	}
        	else {
        		bitarray[i] += 1;
        	}
        	mask = mask >> 1;
        	i++;
        }
    }

    fclose(fp);
    // getline will resize the input buffer as necessary
    // so we need to free the memory when not needed!
    free(line);

    int gamma = 0;
    int epsilon = 0;

    for (i = 0; i < nbits; i++) {
    	gamma <<= 1;
    	epsilon <<= 1;
    	if (bitarray[i] > 0) {
    		gamma |= 1;
    	}
    	else {
    		epsilon |= 1;
    	}
    }

    printf("%d\n", gamma*epsilon);
}
