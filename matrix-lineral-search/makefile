.PHONY: greet clean

greet:
	@echo "build	    :	fast rebuild / build"
	@echo "rebuild	    :	full rebuild"
	@echo "run	    :	run after fast rebuild / build"
	@echo "clean	    :	perform full clean"

build: main.o handler.o io_data.o
	gcc -o 3 main.o handler.o io_data.o

main.o: main.c common_data.h func_signatures.h
	gcc -c -o main.o main.c

handler.o: handler.c common_data.h func_signatures.h
	gcc -c -o handler.o handler.c

io_data.o: io_data.c common_data.h func_signatures.h
	gcc -c -o io_data.o io_data.c

rebuild: main.c handler.c io_data.c
	gcc -o 3 main.c handler.c io_data.c

run: build
	./3 -i 7 -j 10 -r

clean:
	rm -rvf *.o 3
