#include <iostream>
using namespace std;

class Queue {
    private:
        
        int q_array[5];
        int head = 0;
        int tail = 0;
        
    public:
        
    void put(int var) {
        q_array[tail] = var;
        tail++;
    }
    
    int get() {
        return q_array[head++];
    }
};

int main() {
    Queue q;
    q.put(11);
    q.put(22);
    cout << q.get() << endl;
    cout << q.get() << endl;
}