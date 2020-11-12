#include <iostream>
using namespace std;

class Node { 
public: 
    int data; 
    Node* next; 

};
void printList(Node *n)
{
    while (n)
    {
        cout << n->data << " ";
        n = n->next;
    }
}

int main() {
    Node *first = NULL;
    Node *sec = NULL;
    Node *third = NULL;

    first = new Node();
    sec = new Node();
    third = new Node();

    first->data = 3;
    first->next = sec;

    sec->data = 4;
    sec->next = NULL;

    printList(first);

    return 0;
}