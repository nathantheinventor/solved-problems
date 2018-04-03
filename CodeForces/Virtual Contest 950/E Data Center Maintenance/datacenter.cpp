#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;

int main() {
    int n, m, h;
    vector<int> u;
    for (int i = 0; i < n; i ++) {
        int x; cin >> x;
        u.push_back(x);
    }
    
    vector<pii> graph;
    for (int i = 0; i < m; i ++) {
        int c1, c2; cin >> c1 >> c2;
        if ((u[c1] + 1) % h == u[c2]) {
            graph.push_back({c1, c2});
        }
        if ((u[c2] + 1) % h == u[c1]) {
            graph.push_back({c2, c1});
        }
    }
    
    
}