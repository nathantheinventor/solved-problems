#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, m;

//separate this part of the code for cleanliness
int solve(vector<vector<int>>& grid, int l, int r) {
    int ans = 0;
    for (int i = 0; i < n; i ++) {
        vector<int>& v = grid[i];
        auto it = lower_bound(v.begin(), v.end(), l);
        if (it == v.end()) {
            continue;
        }
        int pos = distance(v.begin(), it);
        int lo = 0, hi = min(n - i, m - pos);
        while (hi - lo > 1) {
            int mid = (hi + lo) / 2;
            //cout << "accessing " << i + mid - 1 << " " << pos + mid - 1 << endl;
            int comp = grid[i + mid - 1][pos + mid - 1];
            if (comp > r) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        //cout << hi << endl;
        int comp = grid[i + hi - 1][pos + hi - 1];
        if (comp > r) {
            ans = max(ans, lo);
        } else {
            ans = max(ans, hi);
        }
    }
    return ans;
}

int main() {
    cin >> n >> m;
    while (n > 0) {
        vector<vector<int>> grid(n, vector<int>(m, 0));
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < m; j ++) {
                int x;
                cin >> x;
                grid[i][j] = x;
            }
        }
        int q;
        cin >> q;
        for (int i = 0; i < q; i ++) {
            int l, r;
            cin >> l >> r;
            cout << solve(grid, l, r) << endl;
        }
        cout << "-" << endl;
        cin >> n >> m;
    }
}