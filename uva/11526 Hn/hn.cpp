#include <bits/stdc++.h>

using namespace std;

#define SIZE 67000

typedef long long ll;

ll binSearch(ll n, ll target, ll lo) {
    ll hi = n + 1;
    while (hi - lo > 1) {
        ll mid = (hi + lo) >> 1;
        if (n > mid * (target + 1) - 1) {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    if ((ll) (n / lo) == target) {
        return lo;
    } else {
        return hi;
    }
}

ll solve(ll n) {
    ll ans = 0;
    for (ll i = 1; i < SIZE; i ++) {
        ans += n / i;
    }
    ll tmp = SIZE;
    while (tmp <= n) {
        ll div = n / tmp;
        ll max = binSearch(n, div - 1, tmp);
        ans += div * (max - tmp);
        tmp = max;
    }
    return ans;
}

int main() {
    ll t;
    cin >> t;
    while (t --) {
        ll n;
        cin >> n;
        if ( n <= 0) {
            cout << "0" << endl;
        } else {
            cout << solve(n) << endl;
        }
    }
}
