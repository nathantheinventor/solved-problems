#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int g, V, r;

map<ll, ll> dp[100];
ll apsp[100][100];

struct Gig {
    int start, end, venue, money;
    bool operator<(const Gig other) const {
        return end < other.end;
    }
};

vector<Gig> gigs;

int main() {
    cin >> g >> V >> r;

    // initialize graph
    for (int i = 0; i < V; i ++)
        for (int j = 0; j < V; j ++)
            apsp[i][j] = i == j ? 0 : INT_MAX;
    
    // read in graph
    for (int i = 0; i < r; i ++) {
        int a, b, t; cin >> a >> b >> t; a --; b--;
        apsp[a][b] = t;
        apsp[b][a] = t;
    }

    // calculate APSP
    for (int k = 0; k < V; k++)
        for (int i = 0; i < V; i++)
            for (int j = 0; j < V; j++)
                apsp[i][j] = min(apsp[i][j], apsp[i][k] + apsp[k][j]);
    
    // read in the gigs
    for (int i = 0; i < g; i ++) {
        int s, e, v, m; cin >> v >> s >> e >> m; v--;
        gigs.push_back({s, e, v, m});
    }
    sort(gigs.begin(), gigs.end());

    // initialize dp
    dp[0][0] = 0;
    for (Gig gig: gigs) {
        ll maxMoney = 0;
        auto tmp = dp[gig.venue].upper_bound(gig.end);
        if (tmp != dp[gig.venue].begin()) {
            tmp --;
            maxMoney = (*tmp).second;
        }
        for (int i = 0; i < V; i ++) {
            ll dist = apsp[i][gig.venue];
            auto tmp2 = dp[i].upper_bound(gig.start - dist);
            if (tmp2 != dp[i].begin()) {
                tmp2 --;
                maxMoney = max(maxMoney, (*tmp2).second + gig.money);
            }
        }
        if (maxMoney > 0) {
            dp[gig.venue][gig.end] = maxMoney;
        }
    }
    ll ans = 0;
    for (int i = 0; i < V; i ++) {
        for (auto x: dp[i]) {
            ans = max(ans, x.second);
        }
    }
    cout << ans << endl;
}
