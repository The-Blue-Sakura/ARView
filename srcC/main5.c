#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <oled96.h>

int main();
void delay(int numSeconds);

float versionNumber = 0.1;
int oledinit;

int main(){
    oledinit = oledInit(1, 0x3C, false, false);
    oledFill(0); //Clear Display

    printf("A");
    oledWriteString(3,5,"First Half", FONT_SMALL);
    delay(3);
    oledFill(0); //Clear Display
    printf("B\n");
    oledWriteString(3,5,"Second Half", FONT_SMALL);

    oledShutdown();
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