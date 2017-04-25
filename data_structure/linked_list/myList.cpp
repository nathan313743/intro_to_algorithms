#include "node.cpp"
class MyList
{
    public:
        MyList();
        Node* head;
        void insertNode(int n);
        void deleteNode(int n);
        void reverseList();
};



MyList::MyList()
{
    head = new Node();
}

void MyList::reverseList()
{
    Node *current = head;
    Node *prev = NULL;
    Node *next;

    while(current != NULL)
    {
        next = currnet->next;
        current->next = prev
        prev = current
        current = next
    }
}

void MyList::insertNode(int n)
{
    Node* newNode = new Node();
    if (n==1){
        head = newNode;
        return;
    }
    Node* tempNode = head;
    for(int i = 0; i < n-2; ++i){
        tempNode = tempNode->next;
    }
    newNode->next = tempNode->next;
    tempNode->next = newNode;
}

void MyList::deleteNode(int n)
{
    Node* temp1 = head;
    if (n == 1){
        head = temp1->next;
        delete temp1;
        return;
    }
    for(int i = 0; i < n-2; ++i)
    {
        temp1 = temp1->next;
    }
    Node* nNode = temp1->next;
    temp1->next = nNode->next;
    delete nNode;
}