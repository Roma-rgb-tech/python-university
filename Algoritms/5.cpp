#include <iostream>
#include <vector>
using namespace std;
void MyPrint(vector<int> arr) {
    for (int i = 0; i < arr.size(); i++) 
    cout << arr[i] << endl;
}

int main() {
    vector<int> arr = { 2, -4, 6, 7};
    MyPrint(arr);
}