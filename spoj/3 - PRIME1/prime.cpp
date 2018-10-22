#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;

bool isPrime(ll x) {
    if (x < 2)
        return false;
    if (x < 4)
        return true;
    if (x % 2 == 0)
        return false;
    if (x % 3 == 0)
        return false;
    for (ll i = 5; i < sqrt(x) + 2; i += 6) {
        if (x % i == 0)
            return false;
        if (x % (i + 2) == 0)
            return false;
    }
    return true;
}

int main() {
    ll t; cin >> t;
    while (t --) {
        ll m, n; cin >> m >> n;
        for (ll i = m; i <= n; i ++) {
            if (isPrime(i)) {
                cout << i << endl;
            }
        }
        if (t) cout << endl;
    }
}
