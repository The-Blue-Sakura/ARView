#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include "oled96.h"

extern unsigned char ucSmallFont[];

time_t rawtime;
struct tm * timeinfo;

char hstr[8];
char mstr[8];
char sstr[8];

int main();
void printTime();

int main()
{				
    int i = oledInit(1, 0x3c, 0, 1); // for Raspberry Pi, use channel 1
    oledFill(0);
    while(1){
        time(&rawtime);
        timeinfo = localtime(&rawtime);

        //Format to look nicer
        if(timeinfo->tm_hour < 10){
            sprintf(hstr, "0%d", timeinfo->tm_hour);
        }
        else{
            sprintf(hstr, "%d", timeinfo->tm_hour);
        }
        if(timeinfo->tm_min < 10){
            sprintf(mstr, "0%d", timeinfo->tm_min);
        }
        else{
            sprintf(mstr, "%d", timeinfo->tm_min);
        }
        if(timeinfo->tm_sec < 10){
            sprintf(sstr, "0%d", timeinfo->tm_sec);
        }
        else{
            sprintf(sstr, "%d", timeinfo->tm_sec);
        }
        printTime();
    }


    printf("TIME: %s:%s:%s \n", hstr, mstr, sstr);
    oledShutdown();
    return 0;
} 

void printTime(){
    oledWriteString(1, 0, hstr, FONT_NORMAL);

    oledWriteString(3, 0, ":", FONT_NORMAL);

    oledWriteString(4, 0, mstr, FONT_NORMAL);

    oledWriteString(6, 0, ":", FONT_NORMAL);

    oledWriteString(7, 0, sstr, FONT_NORMAL);    

    //oledWriteString(30,2,sstr, FONT_NORMAL);
}
