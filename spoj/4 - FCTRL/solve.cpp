#include <iostream>
#include <cmath>

using namespace std;
typedef unsigned long long ull;
typedef long long ll;

ll z(ll n) {
    ll x = 5;
    ll ans = 0;
    while (x <= n) {
        ans += n / x;
        x *= 5;
    }
    return ans;
}

int main() {
    int t; cin >> t;
    while (t --) {
        ll n; cin >> n;
        cout << z(n) << endl;
    }
}