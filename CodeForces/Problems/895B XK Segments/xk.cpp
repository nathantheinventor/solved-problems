#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
    ll n, x, k;
    cin >> n >> x >> k;
    vector<ll> data(n);
    for (int i = 0; i < n; i ++) {
        cin >> data[i];
    }
    
    sort(data.begin(), data.end());
    
    ll ans = 0;
    for (int i = 0; i < n; i ++) {
        ll elem = data[i];
        ll elem2 = (((long) ((elem - 1) / x)) + k) * x;
        auto loPos = lower_bound(data.begin(), data.end(), max(elem, elem2));
        auto hiPos = upper_bound(data.begin(), data.end(), elem2 + x - 1);
        ll lo = distance(data.begin(), loPos);
        ll hi = distance(data.begin(), hiPos);
        //cout << elem << " " << hi - lo << endl;
        ans += max(hi - lo, (ll) 0);
    }
    
    cout << ans << endl;
}