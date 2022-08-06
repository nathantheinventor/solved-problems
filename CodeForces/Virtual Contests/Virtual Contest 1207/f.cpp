#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
ll data[500001];
ll dp[710][710];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int q; scanf("%d", &q);
    while (q --) {
        ll t, x, y; scanf("%Ld %Ld %Ld", &t, &x, &y);
        if (t == 1) {
            data[x] += y;
            for (ll i = 1; i < 710; i ++) {
                dp[i][x % i] += y;
            }
        } else {
            if (x < 710) {
                printf("%Ld\n", dp[x][y]);
                // cout <<  << endl;
            } else {
                ll ans = 0;
                for (ll i = y; i < 500001; i += x) {
                    ans += data[i];
                }
                printf("%Ld\n", ans);
                // cout << ans << endl;
            }
        }
    }
}
