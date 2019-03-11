#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include "oled96.h"


int main();
void delay(int seconds);

float versionNumber = 0.1;
time_t rawtime;
struct tm * timeinfo;

char hstr[8];
char mstr[8];
char sstr[8];
char *timestr;
int hour;

int oledinit;

int main(){
    oledinit = oledInit(1, 0x3C, false, false);
    oledFill(0); //Clear Display

    oledWriteString(0,0,"OLED 96 Library!",FONT_NORMAL);
    delay(1);
	oledWriteString(2,2,"BIG!",FONT_BIG);
    delay(1);
    oledWriteString(3,5,"Narrow Font (6x8)", FONT_SMALL);
    delay(1);

    printf("This is a test. PROGRAM START\n");

    FILE *ptr_file;
    char buf[1000];
    ptr_file = fopen("/dev/rfcomm0", "r");
    
    if(!ptr_file){
        printf("No Bluetooth File \n");
    }
    //Time Only
    while(!ptr_file){
        oledFill(0); // Clear Display
        time(&rawtime);
        timeinfo = localtime(&rawtime);

        //Format to look nicer
        if(timeinfo->tm_hour < 10){
            sprintf(hstr, "0%d", timeinfo->tm_hour);
        } else{
            sprintf(hstr, "%d", timeinfo->tm_hour);
        }
        
        if(timeinfo->tm_min < 10){
            sprintf(mstr, "0%d", timeinfo->tm_min);
        } else{
            sprintf(mstr, "%d", timeinfo->tm_min);
        }

        if(timeinfo->tm_sec < 10){
            sprintf(sstr, "0%d", timeinfo->tm_sec);
        } else{
            sprintf(sstr, "%d", timeinfo->tm_sec);
        }

        sprintf(timestr, "%s:%s:%s", hstr, mstr, sstr);
        oledWriteString(3, 5, timestr, FONT_SMALL);
    }

    //Bluetooth Commands Only
    while(ptr_file){
        oledFill(0); // Clear Display
        fgets(buf, 1000, ptr_file);

        oledWriteString(3, 5, buf, FONT_SMALL);

        if(buf == "programquit\n"){
            printf("QUITTING PROGRAM");
            break;
        }
    }

    fclose(ptr_file);
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