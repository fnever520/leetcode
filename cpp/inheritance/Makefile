output: main.o user.o teacher.o
	g++ main.o user.o teacher.o -o output 

main.o: main.cpp
	g++ -std=c++11 -c main.cpp

user.o: user.cpp
	g++ -std=c++11 -c user.cpp 

teacher.o: teacher.cpp
	g++ -std=c++11 -c teacher.cpp 

clean:
	rm *.o output