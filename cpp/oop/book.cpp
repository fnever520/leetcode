#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Book {
    public:
        string title;
        string author;
        int numPage;

        Book() {
            title = "";
            author = "";
            numPage = 0;
        }

        // Constructors
        Book(string aTitle, string aAuthor, int aPages) {
            title = aTitle;
            author = aAuthor;
            numPage = aPages;
        }

};

int main() {
    
    Book book1("harry potter", "JK Rowling", 550);

    cout << book1.title << endl;
    return 0;
}
