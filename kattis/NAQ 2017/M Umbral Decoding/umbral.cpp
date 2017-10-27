#include "bits/stdc++.h"

using namespace std;

typedef long long ll;

#define cube(x) (((x) < 0)? -((x) * (x) * (x)): (x) * (x) * (x))

int main() {
    ll n, k; cin >> n >> k;
    vector<ll> data;
    data.reserve(22000000);
    while(k--) {
        int a, b, c;
        cin >> a >> b >> c;
        int rt = (cbrt(c) + 4);
        for (ll p = a - rt; p < a + rt and p <= n; p ++) {
            for (ll q = b - rt; q < b + rt and q <= n; q ++) {
                if ((cube(b - q)) + (cube(a - p)) <= c) {
                    data.push_back(p << 32 | q);
                }
            }
        }
    }
    sort(data.begin(), data.end());
    ll last = -1;
    ll count = 0;
    for (ll i: data) {
        count = (i != last) ? count + 1: count;
        last = i;
    }
    cout << ((n + 1) * (n + 1) - count) << endl;
    //cout << (cube(3)) << " " << (cube(-2)) << endl;
    return 0;
}