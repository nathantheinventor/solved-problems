#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n, m, k;
vector<ll> l;


ll subsum(ll len) {
    if (len == 0) {
        return 0;
    }
    ll max_sum = -100000000000;
    ll cur_sum = 0;
    for (int i = 0; i < l.size(); i ++) {
        cur_sum += l[i];
        if (i == len - 1) {
            max_sum = max(max_sum, cur_sum);
        }
        if (i >= len) {
            cur_sum -= l[i - len];
            max_sum = max(max_sum, cur_sum);
        }
    }
    return max_sum;
}

ll integer(float x) {
    return (ll) x;
}

ll f(ll x) {
    return subsum(x + 1) - k * (integer((x + 1) / m) + integer((x + 1) % m > 0));
}

ll bin_search(ll lo, ll hi) {
    while (hi - lo > 2) {
        ll m1 = lo + (hi - lo) / 3;
        ll m2 = lo + 2 * (hi - lo) / 3;
        if (f(m2) > f(m1)) {
            lo = m1;
        } else {
            hi = m2;
        }
    }

    return max(f(lo), max(f(lo + 1), f(hi)));
}

ll find_point() {
    vector<double> b;
    for (ll x: l) {
        b.push_back(x - k / m);
    }
    ll ans = 0;
    ll last_zero = -1;
    double max_sum = 0;
    double cur_sum = 0;
    for (int i = 0; i < b.size(); i ++) {
        cur_sum += b[i];
        if (cur_sum <= 0) {
            cur_sum = 0;
            last_zero = i;
        }
        if (cur_sum == max_sum and i - last_zero < ans) {
            ans = i - last_zero;
        }
        if (cur_sum > max_sum) {
            ans = i - last_zero;
            max_sum = cur_sum;
        }
    }
    return ans;
}

int main() {
    cin >> n >> m >> k;
    for (int i = 0; i < n; i ++) {
        ll x;
        cin >> x;
        l.push_back(x);
    }
    ll pt = find_point();
    ll ans = 0;
    ll zero = 0;
    for (ll i = pt - 10; i <= pt + 10; i ++) {
        ans = max(ans, f(min(n, max(zero, i))));
    }

    cout << ans << endl;
}
