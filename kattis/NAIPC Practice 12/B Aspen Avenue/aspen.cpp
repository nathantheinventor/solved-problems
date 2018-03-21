#include <bits/stdc++.h>

using namespace std;

double dp[1001][1001];

// double solve(int l, int r) {
//     if (dp[l][r] != 0.0) {
//         return dp[l][r];
//     }
//     if (l == 0 and r == 0) {
//         return 0.0;
//     }
//     double ans = 1.0e20;
// }

int main () {
    int n;
    cin >> n;
    double l, w;
    cin >> l >> w;
    vector<double> points;
    for (int i = 0; i < n; i ++) {
        double x;
        cin >> x;
        points.push_back(x);
    }
    
    sort(points.begin(), points.end());
    
    vector<double> targets;
    for (int i = 0; i < (n / 2) + 1; i ++) {
        double target = (double)(i / 2) * (l / ((n - 2) / 2));
        targets.push_back(target);
        // cerr << target << "\t";
    }
    // cerr << endl;
    
    for (int i = 0; i < (n / 2) + 1; i ++) {
        for (int j = 0; j < (n / 2) + 1; j ++) {
            double ans = 1.0e15;
            if (i == 0 and j == 0) {
                ans = 0;
            }
            if (i > 0) {
                ans = dp[i - 1][j] + abs(points[i + j - 1] - targets[j]);
            }
            if (j > 0) {
                double x = points[i + j - 1] - targets[i];
                // cerr << dp[i][j - 1] + sqrt(x * x + w * w) << " ";
                ans = min(ans, dp[i][j - 1] + sqrt(x * x + w * w));
            }
            dp[i][j] = ans;
            // cerr << ans << "\t";
        }
        // cerr << endl;
    }
    printf("%.10lf\n", dp[n/2][n/2]);
}
