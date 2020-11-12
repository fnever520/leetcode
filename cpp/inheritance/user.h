#ifndef USER_H
#define USER_H

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class User
{
    static int user_count;
    string status = "Available";

    public:
        static int get_user_count();
        string first_name;
        string last_name;
        string get_status();
        void set_status(string status);
        User();
        User(string first_name, string last_name, string status);
        ~User();
        friend ostream &operator << (ostream &output, const User user);
        friend istream &operator >> (istream &input, User &user);
};

#endif