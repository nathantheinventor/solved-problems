#include <bits/stdc++.h>

using namespace std;

char data[500][500];
int h, w, l;
int dp[500][500];

bool fits(int x, int y, int size) {
    if (x - size + 1 < 0) {
        return false;
    }
    for (int i = x - size + 1; i <= x; i ++) {
        if (dp[i][y] < l * size) {
            return false;
        }
    }
    return true;
}

int maxSize() {
    int ans = 0;
    for (int i = 0; i < h; i ++) {
        for (int j = 0; j < w; j ++) {
            int hi = min(h, w / l), lo = 0;
            while (hi - lo > 1) {
                int mid = (hi + lo) / 2;
                if (fits(i, j, mid)) {
                    lo = mid;
                } else {
                    hi = mid;
                }
            }
            if (fits(i, j, hi)) {
                ans = max(ans, hi);
            }
            ans = max(ans, lo);
        }
    }
    return ans;
}

void preProcess() {
    for (int i = 0; i < h; i ++) {
        dp[i][0] = data[i][0] == '.' ? 1 : 0;
        for (int j = 1; j < w; j ++) {
            dp[i][j] = data[i][j] == '.' ? dp[i][j - 1] + 1 : 0;
        }
    }
}

int main() {
    int n;
    cin >> n;
    while (n --) {
        cin >> h >> w;
        for (int i = 0; i < h; i ++) {
            for (int j = 0; j < w; j ++) {
                cin >> data[i][j];
            }
        }
        string word;
        cin >> word;
        l = word.length();
        preProcess();
        cout << maxSize() << endl;
    }
}