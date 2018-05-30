#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t; 
    while (t --) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> g;
        // vector<vector<int>> rowSums;
        for (int i = 0; i < n; i ++) {
            vector<int> tmp;
            // vector<int> rowSum;
            // int sum = 0;
            for (int j = 0; j < m; j ++) {
                int x; cin >> x;
                // sum += x;
                tmp.push_back(x);
                // rowSum.push_back(sum);
            }
            g.push_back(tmp);
        }
        vector<vector<int>> rowForwardSums;
        vector<vector<int>> rowBackwardSums;
        for (int i = 0; i < n; i ++) {
            vector<int> rowForwardSum;
            vector<int> rowBackwardSum;
            int sum = 0;
            for (int j = 0; j < m; j ++) {
                sum = max(0, sum + g[i][j]);
                rowForwardSum.push_back(sum);
            }
            sum = 0;
            for (int j = m - 1; j >= 0; j --) {
                sum = max(0, sum + g[i][j]);
                rowBackwardSum.push_back(sum);
            }
            rowForwardSums.push_back(rowForwardSum);
            rowBackwardSums.push_back(rowBackwardSum);
        }
        vector<vector<int>> colForwardSums;
        vector<vector<int>> colBackwardSums;
        for (int j = 0; j < m; j ++) {
            vector<int> colForwardSum;
            vector<int> colBackwardSum;
            int sum = 0;
            for (int i = 0; i < n; i ++) {
                sum = max(0, sum + g[i][j]);
                colForwardSum.push_back(sum);
            }
            sum = 0;
            for (int i = n - 1; i >= 0; i --) {
                sum = max(0, sum + g[i][j]);
                colBackwardSum.push_back(sum);
            }
            colForwardSums.push_back(colForwardSum);
            colBackwardSums.push_back(colBackwardSum);
        }
        vector<vector<int>> rowOptimal = g;
        for (int i = 0; i < n; i ++) {
            for (int j = 1; j < m - 1; j ++) {
                rowOptimal[i][j] += g[i][j - 1] + g[i][j + 1];
                if (j > 1) {
                    rowOptimal[i][j] += rowForwardSums[i][j - 2];
                }
                if (j < m - 2) {
                    rowOptimal[i][j] += rowBackwardSums[i][m - (j + 2) - 1];
                }
            }
        }
        // cerr << endl;
        vector<vector<int>> colOptimal = g;
        for (int j = 0; j < m; j ++) {
            for (int i = 1; i < n - 1; i ++) {
                colOptimal[i][j] += g[i - 1][j] + g[i + 1][j];
                // cerr << colOptimal[i][j] << "\t";
                if (i > 1) {
                    colOptimal[i][j] += colForwardSums[j][i - 2];
                }
                if (i < n - 2) {
                    colOptimal[i][j] += colBackwardSums[j][n - (i + 2) - 1];
                }
            }
            // cerr << endl;
        }
            // cerr << endl;
        int ans = rowOptimal[1][1] + colOptimal[1][1] - g[1][1];
        for (int i = 1; i < n - 1; i ++) {
            for (int j = 1; j < m - 1; j ++) {
                // cerr << rowOptimal[i][j] + colOptimal[i][j] - g[i][j] << "\t";
                ans = max(ans, rowOptimal[i][j] + colOptimal[i][j] - g[i][j]);
            }
            // cerr << endl;
        }
        cout << ans << endl;
    }
}
