#include <bits/stdc++.h>
using namespace std;

struct State {
    int visited, cur, remaining;
    const bool operator<(const State other) const {
        return remaining < other.remaining;
    }
};
int n;
vector<vector<int>> adj;
vector<int> collected;
bool canReach(int init) {
    // cerr << "New call" << endl;
    priority_queue<State> pq;
    pq.push({1, 0, init});
    while (!pq.empty()) {
        State s = pq.top(); pq.pop();
        // cerr << "State having visited " << s.visited << " at node " << s.cur << " with remaining " << s.remaining << endl;
        if (s.cur == n - 1) {
            return true;
        }
        int cur = s.cur;
        int remaining = s.remaining + collected[cur];
        int visited = s.visited;
        for (int i = 0; i < n; i ++) {
            int mask = 1 << i;
            if (adj[cur][i] > -1) {
                if (!(mask & visited)) {
                    if (remaining - adj[cur][i] >= 0) {
                        pq.push({visited | mask, i, remaining - adj[cur][i]});
                    }
                }
            }
        }
    }
    return false;
}

int main() {
    cin >> n;
    while (n > 0) {
        collected.clear();
        collected.push_back(0);
        for (int i = 1; i < n - 1; i ++) {
            int x;
            cin >> x;
            collected.push_back(x);
        }
        adj.clear();
        for (int i = 0; i < n; i ++) {
            adj.push_back(vector<int>(n, -1));
        }
        int i, j, c;
        cin >> i >> j >> c;
        while (i >= 0) {
            adj[i][j] = c;
            adj[j][i] = c;
            cin >> i >> j >> c;
        }
        int lo = 0, hi = 1000000;
        while (hi - lo > 1) {
            int mid = (hi + lo) / 2;
            if (canReach(mid)) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        if (canReach(lo)) {
            cout << lo << endl;
        } else if (canReach(hi)) {
            cout << hi << endl;
        } else {
            cout << -1 << endl;
        }

        cin >> n;
    }
}
