#include <iostream>
using namespace std;

void find_missing(int a_var[]) {
    //int len = sizeof(a_var)/sizeof(a_var[0]);
    for (int i=0; i<5; i++) {
        cout << a_var[i] << endl;
    }
    //cout << len;
}

int main () {
    int arr[5] = {1,2,4,5,6};
    cout << sizeof(arr)/sizeof(arr[0]);
    find_missing(arr);
}