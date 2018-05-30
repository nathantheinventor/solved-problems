#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t --) {
        int n;
        cin >> n;
        vector<int> cur(n);
        vector<int> pos(n);
        for (int i = 0; i < n; i ++) {
            cin >> cur[i];
            pos[i] = i;
        }
        vector<int> ans(n, 0);

        int curDay = 1;
        while (true) {
            vector<int> next;
            vector<int> nextPos;
            next.push_back(cur[0]);
            nextPos.push_back(pos[0]);
            int found = 0;
            for (int i = 1; i < cur.size() - 1; i ++) {
                if (cur[i] < cur[i - 1] and cur[i] < cur[i + 1]) {
                    ans[pos[i]] = curDay;
                    found ++;
                } else {
                    next.push_back(cur[i]);
                    nextPos.push_back(pos[i]);
                }
            }
            next.push_back(cur[n - 1]);
            nextPos.push_back(pos[n - 1]);
            cur = next;
            pos = nextPos;
            curDay ++;
            if (found == 0) {
                break;
            }
        }

        for (int i = 0; i < n - 1; i ++) {
            // cerr << cur[i] << " ";
            cout << ans[i] << " ";
        }
        cout << ans[n - 1] << endl;
    }
}