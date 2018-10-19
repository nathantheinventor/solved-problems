#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
#define MOD 1000000007

ll solve(vector<ll>& nodes) {
    ll root = nodes[nodes.length - 1];
    ll roots = 0;
    for (ll x: nodes) {
        if (x == root) {
            roots ++;
        }
    }
    ll ans = 0;
    
    return ans * roots % MOD;
}

int main() {
    vector<ll> nodes;
    int n; cin >> n;
    while (n --) {
        int x; cin >> x;
        nodes.push_back(x);
    }
    sort(nodes.begin(), nodes.end());
    cout << solve(nodes) << endl;
}