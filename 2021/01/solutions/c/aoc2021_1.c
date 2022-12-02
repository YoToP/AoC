#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <errno.h>

//returns an unsigned integer.
//returns zero when string does not contain 
uint32_t string_to_uint32(char *str,size_t str_size){
    uint32_t return_value = 0;
    uint32_t counter = 1;
    for(int32_t i = str_size-1; i >= 0; --i){
        if ((str[i] > 47) && (str[i] < 58)){
            //printf("i: %i, ascii: %i, char: %c\n",i,str[i],str[i]);  
            return_value += (str[i]-48) * counter;
            counter = counter * 10;
        }
    }
    return return_value;
}

//corrects the index for a ringbuffer with size 4
int8_t get_ring_buffer4_index(int8_t index){
    //if -3, then should be 1
    //if -2, then should be 2
    //if -1, then should be 3
    //if 0, then 0
    if (index < 0) return index + 4;
    else return 0;
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

    #define INPUT_LINE_SIZE 10
    char input[INPUT_LINE_SIZE]; //looks like inputlines are not bigger than 10 chars long.
    int32_t last = 0;
    int32_t new = 0;
    uint32_t counterp1 = 0;
    uint32_t counterp2 = 0;
    uint32_t bufferp2[4]; //ringbuffer used for part 2
    int8_t bufferp2_index = 0; //index of the ringbuffer
    if(fgets( input, INPUT_LINE_SIZE, input_file ) != NULL){
        last = string_to_uint32(input,INPUT_LINE_SIZE);
        bufferp2[bufferp2_index] = last; //put at place 0
        bufferp2_index++; //1
    }
    if(fgets( input, INPUT_LINE_SIZE, input_file ) != NULL){
        new = string_to_uint32(input,INPUT_LINE_SIZE); //Read the next value
        bufferp2[bufferp2_index] = new; //put at place 1
        bufferp2_index++; //2
        if (new > last)counterp1++;
        last = string_to_uint32(input,INPUT_LINE_SIZE);
    }
    if(fgets( input, INPUT_LINE_SIZE, input_file ) != NULL){
        new = string_to_uint32(input,INPUT_LINE_SIZE); //Read the next value
        bufferp2[bufferp2_index] = new; //put at place 2
        bufferp2_index++; //3
        if (new > last)counterp1++;
        last = string_to_uint32(input,INPUT_LINE_SIZE);
    }
    while (fgets( input, INPUT_LINE_SIZE, input_file ) != NULL ) {
        new = string_to_uint32(input,INPUT_LINE_SIZE);
        bufferp2[bufferp2_index] = new; //put at next place
        if (bufferp2[bufferp2_index] > bufferp2[get_ring_buffer4_index(bufferp2_index-3)]) counterp2++;
        bufferp2_index++; //update ringbuffer index
        if (bufferp2_index > 3)bufferp2_index = 0; //check if ringbuffer is out of bounds and correct
        //printf("String to int:%i\n",new);
        if (new > last){
            //printf("Last: %i, New: %i\n",last,new);
            counterp1++;
        }
        last = new;

    }
    printf("Puzzle answer part1: %i\n",counterp1);
    printf("Puzzle answer part2: %i\n",counterp2);
    fclose(input_file);

    return 0;
}