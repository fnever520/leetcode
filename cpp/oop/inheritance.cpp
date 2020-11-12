#include <iostream>

using namespace std;

//superclass
class Chef {
    public:
        void makeChicken() {
            cout << "Chef makes chicken" << endl;
        }
        void makeSald() {
            cout << "Chef makes salad" << endl;
        }
};

//subclass
class ItalianChef : public Chef {
    public:
        void makePasta() {
            cout << "The chef makes pasta" << endl;
        }
};

int main() {
    Chef chef;
    chef.makeChicken();

    ItalianChef italianchef;
    italianchef.makePasta();
}