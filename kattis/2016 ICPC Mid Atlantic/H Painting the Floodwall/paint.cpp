#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;
map<ll, ll> dp;
vector<ll> seen;

ll maxBefore (ll x) {
    auto tmp = upper_bound(seen.begin(), seen.end(), x);
    tmp --;
    return *tmp;
}

int main() {
    int n;
    while (cin >> n) {
        vector<pll> ranges;
        while (n --) {
            ll x, y;
            cin >> x >> y;
            ranges.push_back({y, x});
        }
        sort(ranges.begin(), ranges.end());
        dp.clear();
        dp[0] = 0;
        seen.clear();
        seen.push_back(0);
        ll y, x;
        for (auto p: ranges) {
            y = p.first; x = p.second;
            ll ans = dp[maxBefore(y)];
            ans = max(ans, y - x + dp[maxBefore(x)]);
            dp[y] = ans;
            seen.push_back(y);
        }
        // for (auto p: dp) {
        //     cerr << p.first << " " << p.second << endl;
        // }

        cout << dp[y] << endl;
    }
}
