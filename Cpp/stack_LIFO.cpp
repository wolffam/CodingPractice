#include <iostream>
using namespace std;

class Stack {

    private:
        int a_stack[10];
        int top = 0;
    
    public:
        void push(int var) {
            a_stack[top++] = var;
        }
        
        int pop() {
            cout << a_stack[--top] << endl;
        }
};

int main() {
    Stack lifo;
    lifo.push(11);
    lifo.push(22);
    lifo.pop();
    lifo.push(33);
    lifo.pop();
    lifo.pop();
}