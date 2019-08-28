#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
ll data[500001];
ll dp[710][710];

int main() {
    int q; cin >> q;
    while (q --) {
        ll t, x, y; cin >> t >> x >> y;
        if (t == 1) {
            data[x] += y;
            for (ll i = 0; i < 710; i ++) {
                dp[i][x % i] += y;
            }
        } else {
            if (x < 710) {
                cout << dp[x][y] << endl;
            } else {
                ll ans = 0;
                for (ll i = y; i < 500001; i += x) {
                    ans += data[i]
                }
                cout << ans << endl;
            }
        }
    }
}
