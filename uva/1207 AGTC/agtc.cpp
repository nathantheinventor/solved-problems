#include "bits/stdc++.h"

using namespace std;

int solve(string& s1, string& s2) {
    vector<int> last(s1.size() + 1, 0);
    for (int i = 0; i <= s1.size(); i ++) {
        last[i] = i;
    }
    for (char& c: s2) {
        vector<int> cur = last;
        cur[0] ++;
        for (int i = 0; i < s1.size(); i ++) {
            char& c2 = s1[i];
            int ans = last[i];
            if (c2 != c) {
                ans += 1;
            }
            ans = min(ans, last[i + 1] + 1);
            ans = min(ans, cur[i] + 1);
            cur[i + 1] = ans;
        }
        last = cur;
    }
    return last[s1.size()];
}

int main() {
    string s1, s2;
    int trash;
    while (cin >> trash >> s1 >> trash >> s2) {
        cout << solve(s1, s2) << endl;
    }
}