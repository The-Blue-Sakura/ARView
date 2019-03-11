#include <stdio.h>
#include <stdbool.h>
#include <time.h>

int main();
void delay(int numSeconds);

float versionNumber = 0.1;

int main(){
    printf("A");
    delay(3);
    printf("B\n");
    return 0;
}

void delay(int numSeconds) 
{ 
    // Converting time into milli_seconds 
    int millis = 1000 * numSeconds; 
  
    // Stroing start time 
    clock_t start_time = clock(); 
  
    // looping till required time is not acheived 
    while (clock() < start_time + millis) 
        ; 
}