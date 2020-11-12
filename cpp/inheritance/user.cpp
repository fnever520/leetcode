#include "user.h"

using namespace std;

int User::get_user_count()
{
    return user_count;
}

string User::get_status()
{
    return status;
}

void User::set_status(string status)
{
    if (status == "Not Available") 
    {
        this->status = status;
    }
    else
    {
        this->status = "NotAvailable";
    }
}

User::User()
{
    cout << "User created" << endl;
    user_count++;
}
User::User(string first_name, string last_name, string status)
{
    this->first_name = first_name;
    this->last_name = last_name;
    this->status = status;
    user_count++;
}
User::~User()
{
    // cout << "Destructor" << endl;
    user_count--;
}

int User::user_count = 0;

ostream &operator << (ostream &output, const User user)
{
    output << "First name: " << user.first_name << "\nLast name: " << user.last_name << "\nStatus: " << user.status;
    return output;
}

istream &operator >> (istream &input, User &user)
{
    input >> user.first_name >> user.last_name >> user.status;
    return input;
}
