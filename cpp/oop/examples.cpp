#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Student {
    public:
    
        string name;
        int studentID;
        string email;
};



int main() {
    
    vector<Student> users;
    Student me, you;

    me.name = "Fabian";
    me.studentID = 20185112;
    me.email = "fnever@gmail.com";

    you.name = "Emily";
    you.studentID = 20188888;

    users.push_back(me);
    users.push_back(you);
    cout << users[1].name << " " << users[1].studentID << endl;
    
    return 0;
}