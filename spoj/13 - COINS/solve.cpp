#include <iostream>
#include <cmath>
#include <stack>
#include <vector>
#include <map>

using namespace std;
typedef unsigned long long ull;
typedef long long ll;

map<ll, ll> dp;
ll solve(ll x) {
    ll next = (x / 4) + (x / 3) + (x / 2);
    if (next <= x) {
        return x;
    }
    if (dp[x] > 0) {
        return dp[x];
    }
    dp[x] += solve(x / 4) + solve(x / 3) + solve(x / 2);
    return dp[x];
}

int main() {
    ll n;
    while (cin >> n) {
        cout << solve(n) << endl;
    }
}
