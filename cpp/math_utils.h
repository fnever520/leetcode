// declaration

#ifndef MATH_UTILS
#define MATH_UTILS

struct Rectangle
{
    int length;
    int width;
};

namespace utilz {
    double area(int length, int width);

    double area(int length);

    double pow(double base, int power = 2);
}


#endif