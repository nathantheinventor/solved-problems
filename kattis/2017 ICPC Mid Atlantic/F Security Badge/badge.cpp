#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;

int n, l, b, s, d;
int starts[1001][1001];
int ends2[1001][1001];

vector<set<int>> neighbors(1001);

bool canPass(int badge) {
    vector<bool> visited(1000, false);
    deque<int> toVisit = {s};
    while (toVisit.size() > 0) {
        int x = toVisit.front();
        if (x == d) {
            return true;
        }
        toVisit.pop_front();
        if (visited[x]) {
            continue;
        }
        visited[x] = true;
        for (int neighbor: neighbors[x]) {
            if (starts[x][neighbor] <= badge and badge <= ends2[x][neighbor]) {
                toVisit.push_back(neighbor);
            }
        }
    }
    return false;
}

int main() {
    cin >> n >> l >> b >> s >> d;
    vector<int> ss;
    vector<int> es;
    for (int i = 0; i < l; i ++) {
        int x, y;
        cin >> x >> y;
        neighbors[x].insert(y);
        cin >> starts[x][y];
        ss.push_back(starts[x][y]);
        cin >> ends2[x][y];
        es.push_back(ends2[x][y]);
    }
    vector<pii> ranges;
    vector<int> sts;
    for (int s2: ss) {
        if (canPass(s2)) {
            sts.push_back(s2);
        }
    }
    for (int s2: es) {
        if (canPass(s2 + 1)) {
            sts.push_back(s2 + 1);
        }
    }
    sort(sts.begin(), sts.end());
    sort(es.begin(), es.end());
    for (int s2: sts) {
        auto e = lower_bound(es.begin(), es.end(), s2);
        ranges.push_back({s2, *e});
    }
    int nextEnd = 0;
    int ans = 0;
    for (pii x: ranges) {
        int start = x.first, end = x.second;
        // cerr << start << " " << end << endl;
        start = max(start, nextEnd + 1);
        end = max(end, start - 1);
        nextEnd = end;
        ans += end - start + 1;
        // cerr << ans << " " << nextEnd << " " << start << " " << end << endl;
    }
    cout << ans << endl;
}