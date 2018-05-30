#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t --) {
        string s;
        int k;
        cin >> s >> k;
        vector<valarray<int>> data;
        valarray<int> cur(0, 26);
        data.push_back(cur);
        for (char c: s) {
            cur[c - 'a'] += 1;
            data.push_back(cur);
        }
        int ans = 0;
        for (int i = 0; i <= s.size(); i ++) {
            valarray<int> tmp(0, 26);
            int m = 0;
            int sum = 0;
            for (int j = i; j < s.size(); j ++) {
                tmp[s[j] - 'a'] ++;
                m = max(m, tmp[s[j] - 'a']);
                sum ++;
                if (sum < k * m or m < 1) {
                    continue;
                }
                bool works = true;
                for (int i: tmp) {
                    if (i != 0 and i != m) {
                        works = false;
                        break;
                    }
                }
                if (not works) {
                    continue;
                }
                ans ++;
                // cerr << j << " : " << i << endl;
            }
        }
        cout << ans << endl;
    }
}
