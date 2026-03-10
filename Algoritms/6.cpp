// Знайти перший індекс заданого елемента в масиві.
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
}


// Видалити з базового вектора максимальне значення.
#include <iostream>
#include <vector>
using namespace std;

void removeMaxIter(vector<int>& v) {
    if (v.empty()) return;
    auto it = max_element(v.begin(), v.end());
    v.erase(it);
}


int findMaxIdx(vector<int>& v, int n, int maxIdx) {
    if (n == v.size()) return maxIdx; 
    if (v[n] > v[maxIdx]) maxIdx = n; 
    return findMaxIdx(v, n + 1, maxIdx); 
}

int main() {
    vector<int> v = {5, 12, 3, 12, 8};

    removeMaxIter(v); 

    int m = findMaxIdx(v, 0, 0); 
    v.erase(v.begin() + m);

    for (int x : v) cout << x << " "; 
}






