#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include "display.h"

int main();

float versionNumber = 0.1;
time_t rawtime;
struct tm * timeinfo;

char hstr[8];
char mstr[8];
char sstr[8];
char ampm = 'AM';
int hour;

int main(){
    printf("This is a test. PROGRAM START\n");
    FILE *ptr_file;
    char buf[1000];
    ptr_file = fopen("/dev/rfcomm0", "r");
    
    if(!ptr_file){
        return 1;
    }

    while(true){
        time(&rawtime);
        timeinfo = localtime(&rawtime);
        fgets(buf, 1000, ptr_file);

        hour = timeinfo->tm_hour;

        //Format to look nicer
        if(hour > 12){
            ampm = 'PM';
            hour = hour - 12;
        } else{
            ampm = 'AM';
        }

        if(hour < 10){
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

        printf("%s ||| TIME: %s:%s:%s %s \n", buf, hstr, mstr, sstr, ampm);

        if(buf == "programquit\n"){
            printf("QUITTING PROGRAM");
            return 0;
        }
    }

    fclose(ptr_file);

    return 0;
}