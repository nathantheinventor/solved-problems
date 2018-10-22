#include <iostream>
#include <cmath>
#include <stack>

using namespace std;
typedef unsigned long long ull;
typedef long long ll;

int main() {
    int t; cin >> t;
    while (t > 0) {
        ll ans = 0;
        for (int i = 0; i <= t; i ++) {
            ans += i * i;
        }
        cout << ans << endl;
        cin >> t;
    }
}