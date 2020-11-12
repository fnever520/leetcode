#include <iostream>
#include <vector>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    // ListNode(int x) : val(x), next(NULL){}
};

class Solution
{
public:
    bool hasCycle(ListNode *head)
    {
        if (head == NULL)
            return false;
        ListNode *walker = head, *runner = head;
        cout << walker << endl;
        while (runner->next != NULL && runner->next->next != NULL)
        {
            walker = walker->next;
            runner = runner->next->next;
            if (walker == runner)
                return true;
        }
        return false;
    }
};


void printList(ListNode *node) {
    while (node) {
        cout << node->val << endl;
        node = node->next;
    }
}

int main() {
    ListNode *first = NULL;
    ListNode *sec = NULL;

    first = new ListNode();
    sec = new ListNode();

    first->val = 1;
    first->next = sec;

    sec->val = 5;
    sec->next = NULL;
    Solution sol;

    cout << sol.hasCycle(first);

    return 0;

}