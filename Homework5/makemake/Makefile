#Homework 5	Yosub Lee

CC	= g++ -Wall -c -MMD
OBJS	= exprtest.o parser.tab.o scanner.o driver.o

all: exprtest

exprtest: ${OBJS}
	g++ -Wall -g -MDD -o exprtest ${OBJS}

scanner.o: scanner.ll scanner.hpp
	flex -t scanner.ll > scanner.cpp
	${CC} scanner.cpp
exprtest.o: exprtest.cpp driver.hpp expression.hpp
	${CC} exprtest.cpp
parser.tab.o: expression.hpp scanner.hpp driver.hpp
	bison parser.ypp
	${CC} parser.tab.cpp
driver.o: driver.cpp driver.hpp scanner.hpp
	${CC} driver.cpp

clean:
	rm -f *.o *.d *~ *.hh exprtest scanner.cpp parser.tab.hpp parser.tab.cpp
