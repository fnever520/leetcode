// definition

#include "math_utils.h"

namespace utilz {
    double area(int length, int width)
    {
        return length * width;
    }

    double area(int length)
    {
        return length * length;
    }

    double area(Rectangle rectangle)
    {
        return rectangle.length * rectangle.length;
    }

    double pow(double base, int power)
    {
        int total = 1;

        for (int i = 0; i < power; i++)
        {
            total *= base;
        }

        return total;
    }
}
