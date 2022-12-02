#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

int main(int argc,char **argv){
    
    (void) argc;

    char *program  = *argv++;

    if (*argv != NULL){
        fprintf(stderr, "Usage: %s\n",program);
        fprintf(stderr, "ERROR: Input file is not read\n");
        //exit(1);
    }

    clock_t start,end;
    start = clock();

    int32_t xmin = 14;
    int32_t xmax = 50;
    int32_t ymin = -267;
    int32_t ymax = -225;

    int32_t xVel = 0;
    int32_t yVel = 0;
    int32_t xPos = 0;
    int32_t yPos = 0;
    uint8_t inZone = 0;

    printf("Target: x:%i..%i, y:%i..%i\n",xmin,xmax,ymin,ymax);
    int32_t counter = 0;
    for (int32_t i = 1; i <= xmax;++i){
        for (int32_t j = ymin; j <= 5000;++j){
            xVel = i;
            yVel = j;
            xPos = 0;
            yPos = 0;
            inZone = 0;
            while ((xPos <= xmax) && (yPos >= ymin))
            {
                xPos += xVel;
                yPos += yVel;
                if (xVel > 0) xVel -= 1;
                else if (xVel < 0) xVel += 1;
                yVel -= 1;
                if (((xmin <= xPos) && (xPos <= xmax))&&((ymin <= yPos)&&(yPos <= ymax))) inZone = 1;
            }                
            if (inZone) counter += 1;
        }
    }
    

    end = clock();
    printf("start time: %li\n",start);
    printf("end time: %li\n",end);
    printf("Puzzle answer part2: %i\n",counter);

    double time_passed = (double)end-start;
    printf("CPU time passed:%f/%li=%f\n",time_passed,CLOCKS_PER_SEC,time_passed/CLOCKS_PER_SEC);
    return 0;
}