#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int dp[1 << 20];
int cnt[20][20];

int bits(int x) {
    int ans = 0;
    for (int i = 1; i < 1 << 20; i <<= 1) {
        if (x & i) {
            ans += 1;
        }
    }
    return ans;
}

int cmp(int a, int b) {
    return bits(a) < bits(b);
}

int solve(int mask, int m) {
    int ans = 1 << 30;
    int b = bits(mask);
    for (int x = 0; x < m; x ++) {
        if (!((1 << x) & mask)) continue;
        int tmp = dp[mask ^ (1 << x)];
        for (int y = 0; y < m; y ++) {
            if (x == y) continue;
            if (mask & (1 << y)) tmp += cnt[x][y] * b;
            else tmp -= cnt[x][y] * b;
        }
        // cout << mask << " " << m << " " << tmp << endl;
        ans = min(ans, tmp);
    }
    // cout << ans << endl;
    return ans;
}

int main() {
    int n, m;
    string s;
    cin >> n >> m >> s;
    char last = 'z';
    for (char c: s) {
        if (last != 'z') {
            cnt[last - 'a'][c - 'a'] ++;
            cnt[c - 'a'][last - 'a'] ++;
        }
        last = c;
    }

    // for (int i = 0; i < m; i ++) {
    //     for (int j = 0; j < m; j ++) {
    //         cout << cnt[i][j] << "\t";
    //     }
    //     cout << endl;
    // }

    vector<int> arrangements;
    for (int i = 1; i < 1 << m; i ++) {
        arrangements.push_back(i);
    }
    sort(arrangements.begin(), arrangements.end(), cmp);
    
    for (auto& i: arrangements) {
        dp[i] = solve(i, m);
    }
    cout << dp[(1 << m) - 1] << endl;
}