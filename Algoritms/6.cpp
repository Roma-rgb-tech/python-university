// // Знайти перший індекс заданого елемента в масиві.
#include <iostream>
using namespace std;

int iter(int arr[], int n, int x) {
    for (int i = 0; i < n; i++)
        if (arr[i] == x) return i;
    return -1;
}

int recur(int arr[], int n, int x, int i = 0) {
    if (i == n) return -1;           
    if (arr[i] == x) return i;     
    return recur(arr, n, x, i + 1);  
}

int main() {
    int a[] = {10, 20, 30, 40};
    int n = 4, x = 30;

    cout << "Ітеративна: " << iter(a, n, x) << endl;
    cout << "Рекурсивна: " << recur(a, n, x) << endl;

    return 0;
}