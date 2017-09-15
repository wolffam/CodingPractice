#include <iostream>
#include <vector> 
using namespace std;

void print_to_ten(std::vector<int> & vect){
    for (vector<int>::iterator t=vect.begin(); t!=vect.end(); ++t) {
        cout << *t << endl;
    }
}

int main(){
    vector<int> t_v{1,2,3,4,5,6,7,8,9,10};
    print_to_ten(t_v);
}