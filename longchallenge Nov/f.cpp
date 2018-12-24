#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007l
typedef long long ll;

long modInv(long x, long n = MOD - 2) {
    if (n == 1) {
        return x % MOD;
    }
    long tmp = modInv(x, n / 2);
    tmp = (tmp * tmp) % MOD;
    if (n % 2 == 1) {
        return (tmp * x) % MOD;
    }
    return tmp;
}

vector<ll> f, fi; 

ll ncr[1010][1010];
void makeFact() {
    f.push_back(1);
    fi.push_back(1);
    ll cur = 1;
    for (ll i = 1; i < 1010; i ++) {
        cur = (cur * i) % MOD;
        f.push_back(cur);
        fi.push_back(modInv(cur));
    }
    for (int i = 0; i < 1010; i ++) {
        for (int j = 0; j <= i; j ++) {
            ncr[i][j] = (((f[i] * fi[j]) % MOD) * fi[i - j]) % MOD;
        }
    }
}

#define nCr(a, b) ncr[ a ][ b ]

int main() {
    makeFact();
    int t; cin >> t;
    while (t --) {
        int n; cin >> n;
        vector<int> l;
        for (int i = 0; i < n; i ++) {
            int x; cin >> x;
            l.push_back(x);
        }
        map<int, int> values;
        for (int x: l) {
            values[x] ++;
        }

        map<int, int> lessThan;
        map<int, int> greaterThan;
        for (auto s: values) {
            int x = s.first;
            lessThan[x] = 0;
            greaterThan[x] = 0;
            for (int y: l) {
                if (y < x) {
                    lessThan[x] ++;
                } else if (y > x) {
                    greaterThan[x] ++;
                }
            }
        }

        ll ans = 0;

        // find num odd sequences
        for (int i = 1; i <= n; i += 2) {
            ans += nCr(n, i);
        }
        ans %= MOD;

        // find num even sequences
        for (auto s: values) {
            int x = s.first;
            ll lt = lessThan[x];
            ll gt = greaterThan[x];
            vector<int> tmp3;
            for (int j = 2; j <= s.second; j ++) {
                ll tmp = nCr(s.second, j);
                ll tmp2 = 0;
                for (int b = 0; b <= j - 2; b ++) {
                    int a = j - b - 2;
                    for (int i = max(b, a); i < min(lt + b, gt + a) + 1; i ++) {
                        tmp2 += nCr(lt, i - b) * nCr(gt, i - a) % MOD;
                    }
                    tmp2 %= MOD;
                }
                ans = (ans + tmp * tmp2) % MOD;
            }
        }

        cout << ans << endl;
    }
}
