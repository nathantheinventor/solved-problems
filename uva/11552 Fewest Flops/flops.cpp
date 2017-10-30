#include "bits/stdc++.h"

using namespace std;

int dp[1000][27];

int solve2(vector<set<char>>& vs, char c, int level) {
    if (dp[level][c - 'a'] != -1) {
        return dp[level][c - 'a'];
    }
    if (level >= vs.size()) {
        return 0;
    }
    if (vs[level].size() == 1) {
        char elem = *(vs[level].begin());
        if (c == elem) {
            return dp[level][c - 'a'] = solve2(vs, c, level + 1);
        } else {
            return dp[level][c - 'a'] = solve2(vs, elem, level + 1) + 1;
        }
    } else {
        int ans = 10000;
        int add = 0;
        for (char elem: vs[level]) {
            if (elem == c) {
                add --;
            } else {
                ans = min(ans, solve2(vs, elem, level + 1));
            }
        }
        return dp[level][c - 'a'] = ans + add + vs[level].size();
    }
}

int solve(int n, string& s) {
    vector<set<char>> vs(s.size() / n);
    int i1 = 0;
    int i2 = -1;
    for (char c: s) {
        if (i1++ % n == 0) {
            i2 ++;
        }
        vs[i2].insert(c);
    }
    
    for (int i = 0; i < 1000; i ++) {
        for (int j = 0; j < 27; j ++) {
            dp[i][j] = -1;
        }
    }
    return solve2(vs, '{', 0);
}

int main() {
    int t;
    cin >> t;
    while(t --) {
        int n;
        string s;
        cin >> n >> s;
        cout << solve(n, s) << endl;
    }
}