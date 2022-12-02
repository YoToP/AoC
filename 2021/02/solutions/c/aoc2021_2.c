#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <errno.h>
#include <time.h>
//returns an unsigned integer.
//returns zero when string does not contain 
uint32_t string_to_uint32(char *str,uint8_t start_pos,size_t str_size){
    uint32_t return_value = 0;
    uint32_t counter = 1;
    for(int32_t i = str_size-1; i >= start_pos; --i){
        if ((str[i] > 47) && (str[i] < 58)){
            //printf("i: %i, ascii: %i, char: %c\n",i,str[i],str[i]);  
            return_value += (str[i]-48) * counter;
            counter = counter * 10;
        }
    }
    return return_value;
}


uint8_t get_space_pos(char *str, size_t str_size){
    uint8_t pos = 0;
    for(uint8_t i = 0; i < str_size;++i){
        if (str[i]==' ') pos = i;
    }
    return pos;
}

int main(int argc,char **argv){
    
    (void) argc;
    assert(*argv != NULL);
    char *program  = *argv++;

    if (*argv == NULL){
        fprintf(stderr, "Usage: %s <input.txt>\n",program);
        fprintf(stderr, "ERROR: No input file is provided\n");
        exit(1);
    }

    char *input_filepath = *argv++;

    printf("provided file is %s\n",input_filepath);

    FILE *input_file= fopen(input_filepath, "rb");
    if (input_file == NULL){
        fprintf(stderr,"ERROR: Could not open file %s: %s\n",input_filepath, strerror(errno));
        exit(1);
    }
    struct timespec ts;
    time_t start,end;
    long start_n, end_n;
    clock_gettime(CLOCK_MONOTONIC,&ts);
    start = ts.tv_sec;
    start_n = ts.tv_nsec;
    //printf("start Time: %li\n",start);
    #define INPUT_LINE_SIZE 20
    char input[INPUT_LINE_SIZE]; //looks like inputlines are not bigger than 10 chars long.
    memset(input, 0, INPUT_LINE_SIZE); //make sure the input buffer is zeroed
    uint8_t spacepos = 0; //position of the space
    uint8_t linevalue = 0; //Value on that line

    uint64_t depthp1 = 0; //dept of submarine
    uint64_t horp1 = 0; //hor pos of submarine

    uint64_t depthp2 = 0; //dept of submarine
    uint64_t horp2 = 0; //hor pos of submarine
    uint64_t aimp2 = 0; //hor pos of submarine
    
    while (fgets( input, INPUT_LINE_SIZE, input_file ) != NULL ) {
        spacepos = get_space_pos(input,INPUT_LINE_SIZE);
        linevalue = string_to_uint32(input,spacepos,INPUT_LINE_SIZE);
        //printf("space position =%u. Line value: %u\n",spacepos,linevalue);
        if (spacepos == 7){ // forward
            horp1 += linevalue;
            horp2 += linevalue;
            depthp2 += (aimp2 * linevalue);
        }else if (spacepos == 4) //down
        {
            depthp1 += linevalue;
            aimp2 += linevalue;
        }else if (spacepos == 2) //up
        {
            depthp1 -= linevalue;
            aimp2 -= linevalue;
        }
        memset(input, 0, INPUT_LINE_SIZE); //copy zero's to prevent reading old data in str > int function
    }
    clock_gettime(CLOCK_MONOTONIC,&ts);
    end = ts.tv_sec;
    end_n = ts.tv_nsec;
    //printf("start Time: %li\n",end);
    printf("Puzzle answer part1: %li\n",depthp1*horp1);
    printf("Puzzle answer part2: %li\n",depthp2*horp2);
    fclose(input_file);
    printf("Time passed: %li.%09li ms\n",(end-start),(end_n-start_n));//https://linux.die.net/man/3/clock_gettime
    return 0;
}