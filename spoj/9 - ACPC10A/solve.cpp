#include <iostream>
#include <cmath>
#include <stack>

using namespace std;
typedef unsigned long long ull;
typedef long long ll;

int main() {
    int a, b, c; cin >> a >> b >> c;
    while (a != b) {
        int diff = b - a;
        int quot = a == 0 ? 0 : b / a;
        if (c - b == diff) {
            cout << "AP " << (c + diff) << endl;
        } else if (a * quot == b and b * quot == c) {
            cout << "GP " << (c * quot) << endl;
        }
        cin >> a >> b >> c;
    }
}