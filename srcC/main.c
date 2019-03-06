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

int main(){
    printf("This is a test. PROGRAM START\n");
    while(true){
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
        printf("TIME: %s:%s:%s \n", hstr, mstr, sstr);
    }

    return 0;
}