#include <iostream>

using namespace std;

int main() {
    long double l1 = ((long double) 4e30) + 0.1;
    long double l2 = ((long double) 4e30) + 0.2;
    cout << (l2 - l1) << endl;
}