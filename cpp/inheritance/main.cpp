#include <iostream>
#include <string>
#include "user.h"
#include "teacher.h"

using namespace std;

int main()
{
    User user;
    cin >> user;
    cout << user << endl;

    Teacher teacher;
    teacher.output();
}

