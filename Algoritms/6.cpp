// Знайти перший індекс заданого елемента в масиві. На основі ітеративних алгоритмів
#include <iostream>
using namespace std;

int findIndex(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            return i;   
        }
    }
    return -1;  
}

int main() {
    int n;

    cout << "Введіть кількість елементів: ";
    cin >> n;

    int arr[100];

    for (int i = 0; i < n; i++) {
        cout << "Введіть елемент: ";
        cin >> arr[i];
    }

    int key;
    cout << "Введіть число для пошуку: ";
    cin >> key;

    int index = findIndex(arr, n, key);

    if (index != -1)
        cout << "Перший індекс = " << index << endl;
    else
        cout << "Елемент не знайдено" << endl;


}



// Видалити з базового вектора максимальне значення. На основі рекуративних алгоритмів
#include <iostream>
#include <vector>
using namespace std;


int findMax(const vector<int>& v, int index = 0) {
    if (index == v.size() - 1) return v[index];
    int maxRest = findMax(v, index + 1);
    return (v[index] > maxRest) ? v[index] : maxRest;
}


void removeMax(vector<int>& v, int maxVal, int index = 0) {
    if (index == v.size()) return;
    if (v[index] == maxVal) {
        v.erase(v.begin() + index);
        return;
    }
    removeMax(v, maxVal, index + 1);
}

int main() {
    int n;
    cout << "Введіть кількість елементів: ";
    cin >> n;

    vector<int> v(n);
    cout << "Введіть елементи: ";
    for (int i = 0; i < n; i++) cin >> v[i];

    cout << "Базовий вектор: ";
    for (int x : v) cout << x << " ";
    cout << endl;

    int maxVal = findMax(v);
    cout << "Максимальне значення: " << maxVal << endl;

    removeMax(v, maxVal);

    cout << "Вектор після видалення максимального: ";
    for (int x : v) cout << x << " ";
    cout << endl;

    return 0;
}