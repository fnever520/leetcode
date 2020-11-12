#include <iostream>
#include <string>

using namespace std;

void swap(int &first, int &second)
{
    int temp;
    temp = first;
    first = second;
    second = temp;
}

int main() {
    int first = 10;
    int second = 5;

    swap(first, second);

    cout << "first: "<< first << "\tSecond: " << second << endl;
    return 0;

}