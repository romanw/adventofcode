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
    char *running;
    char *token;
    
    int x1, y1, x2, y2;
    int start, end;
    int i, x, y, xstep, ystep;

    #define GRID_SIZE 1000
    int grid[GRID_SIZE][GRID_SIZE];

	// initialise the grid to zero
    for (x = 0; x < GRID_SIZE; x++)
    	for(y = 0; y < GRID_SIZE; y++)
    		grid[x][y] = 0;

	// http://www.gnu.org/savannah-checkouts/gnu/libc/manual/html_node/Finding-Tokens-in-a-String.html
    while(getline(&line, &len, fp) != -1) {
        //input = (int) strtol(line, NULL, 2);
        running = strdup(line);
        // get x1
        token = strsep(&running, ",");
        x1 = atoi(token);
        // get y1
        token = strsep(&running, " ");
        y1 = atoi(token);
        // skip the seperator
        token = strsep(&running, " ");
        // get x2
        token = strsep(&running, ",");
        x2 = atoi(token);
        // get y2
        y2 = atoi(running);

		// if x1 and x2 are the same mark the y(s)
        if (x1 == x2) {
        	start = y1; end = y2;
        	if (y2 < y1) { start = y2; end = y1; }
       		for (i = start; i <= end; i++) grid[x1][i] += 1;
        }
        // else if y1 and y2 are the same mark the x(s)
        else if (y1 == y2) {
        	start = x1; end = x2;
        	if (x2 < x1) { start = x2; end  = x1; }
       		for (i = start; i <= end; i++) grid[i][y1] += 1;
        }
        // else we are on an angle
        else {
	        if (abs(x2 - x1) == abs(y2 - y1)) {
	        	x = x1; y = y1;
	        	xstep = 1; ystep = 1;
	        	if (x2 < x1) xstep = -1;
	        	if (y2 < y1) ystep = -1;
	        	i = abs(x2 - x1);
	        	while (i >= 0) {
        			grid[x][y] += 1;
        			x += xstep;
        			y += ystep;
        			i--;
	        	}
	        }
	        else {
	        	// don't know what to do here!
	        	printf("%d,%d -> %d,%d\n", x1,y1,x2,y2);
	        }
        }
    }

    fclose(fp);
    // getline will resize the input buffer as necessary
    // so we need to free the memory when not needed!
    free(line);


	int count = 0;
	for (x = 0; x < GRID_SIZE; x++) {
		for (y = 0; y < GRID_SIZE; y++) {
			if (grid[x][y] > 1) count++;
		}
	}
	printf("%d\n", count);
}
