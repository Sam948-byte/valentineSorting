#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char *filename = "input.txt";
    FILE *fp = fopen(filename, "r");

    if (fp == NULL)
    {
        printf("Error: could not open file %s", filename);
        return 1;
    }

    // reading line by line, max 256 bytes
    const unsigned MAX_LENGTH = 256;
    char buffer[MAX_LENGTH];

    // greatest calorie value and the array
    int greatestValue = 0;
    int arraySum = 0;

    while (fgets(buffer, MAX_LENGTH, fp)){
   if(strcmp(buffer, "\n") == 0){
    if(greatestValue < arraySum){
        printf("\ngreatest value now equals %i", arraySum);
        greatestValue = arraySum;
        arraySum = 0;
       
        
    }
    } else{

    arraySum += atoi(buffer);
    }
    }
    // close the file
    fclose(fp);

printf("\nthe greatest value of the array is %i", greatestValue);

    return 0;
}