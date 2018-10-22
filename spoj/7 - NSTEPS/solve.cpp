#include <iostream>
#include <cmath>
#include <stack>

using namespace std;
typedef unsigned long long ull;
typedef long long ll;

int main() {
    int t; cin >> t;
    while (t --) {
        ll x, y; cin >> x >> y;
        if (x == y) {
            cout << (2 * x - (x % 2)) << endl;
        } else if (x == y + 2) {
            cout << (2 * x - 2 - (x % 2)) << endl;
        } else {
            cout << "No Number" << endl;
        }
    }
}