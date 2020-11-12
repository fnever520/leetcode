#include <iostream>
#include <vector>

using namespace std;
/*
struct - the members are instatiated into object in public , by default
class - the members are instatiated into object in private, by default
*/

class User {
    private:
        string status = "Available";

    public:
        string first_name;
        string last_name;
        string get_status() {
            return status;
        }
        void set_status(string aStatus) {
            status = aStatus;
        }
    
};

int add_user_if_not_already_exist(vector<User> &users, User user) {
    for (int i=0; i<users.size(); i++) {
        if (users[i].first_name == user.first_name &&
            users[i].last_name == user.last_name) {
            return i;
        }
    }
    users.push_back(user);
    return users.size()-1;
}

int main() {
    
    User user1, user2, user3;

    vector<User> users;
    user1.first_name = "Fabian";
    user1.last_name = "Tan";
    user1.set_status("Still single");

    user2.first_name = "Hello";
    user2.last_name = "World";

    user3.first_name = "Goodbye";
    user3.last_name = "World";

    users.push_back(user1);
    users.push_back(user2);
    users.push_back(user3);

    User user4;
    user4.first_name = "Test";
    user4.last_name = "Programme";

    add_user_if_not_already_exist(users, user4);

    cout << users[4].last_name << endl;
    cout << user1.get_status() << endl;

    return 0;

}