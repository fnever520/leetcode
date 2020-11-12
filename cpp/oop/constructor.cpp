#include <iostream>
#include <vector>

using namespace std;
/*
struct - the members are instatiated into object in public , by default
class - the members are instatiated into object in private, by default
*/

class User
{
    private:
        static int user_count;
        string status = "Available";

    public:
        static int get_user_count() {
            return user_count;
        }
        string first_name;
        string last_name;
        string get_status()
        {
            return status;
        }
        void set_status(string aStatus)
        {
            status = aStatus;
        }
        User(string first_name, string last_name)
        {
            this->first_name = first_name;
            this->last_name = last_name;
            user_count++;
        }
        ~User()
        {
            cout << "Destructor" << endl;
            user_count--;
        }
};

int User::user_count = 0;

int add_user_if_not_already_exist(vector<User> &users, User user)
{
    for (int i = 0; i < users.size(); i++)
    {
        if (users[i].first_name == user.first_name &&
            users[i].last_name == user.last_name)
        {
            return i;
        }
    }
    users.push_back(user);
    return users.size() - 1;
}

int main()
{

    User user("Fabian", "Tan");

    cout << User::get_user_count();
    cout << user.last_name << endl;

    return 0;
}