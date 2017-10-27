#include "bits/stdc++.h"
using namespace std;

#define INF 10000000000
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    int n, m, f, s, t;
    scanf("%d%d%d%d%d", &n, &m, &f, &s, &t);
    vector<vector<pair<int, ll>>> adj(n, vector<pair<int, int>>());

    for(int i = 0; i < m; i++) {
        int i, j, c;
        scanf("%d%d%d", &i, &j, &c);
        adj[i].push_back({j, c});
        adj[j].push_back({i, c});
    }

    vector<pair<int, int>> flights(f);
    for(int i = 0; i < f; i++) {
        int u, v; scanf("%d%d", &u, &v);
        flights[i] = {u, v};
    }

    

    return 0;
}