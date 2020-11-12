// main file

#include <iostream>
#include <fstream>
#include <vector>
#include "math_utils.h"

using namespace std;

int main()
{
    Rectangle rectangle;
    rectangle.length = 11;
    int base;
    cin >> base;

    cout << "The power of 2 for base " << base << " is "<< utilz::pow(base) << endl;
    cout << "The area of a rectangle is: "<< utilz::area(rectangle.length) << endl;
    return 0;
}