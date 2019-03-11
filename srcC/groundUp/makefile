CFLAGS=-c -Wall -O2
LIBS = -loled96 -lm -lpthread

all: main

main: main.o
	$(CC) main.o $(LIBS) -o main

main.o: main.c
	$(CC) $(CFLAGS) main.c

clean:
	rm -rf *.o main
