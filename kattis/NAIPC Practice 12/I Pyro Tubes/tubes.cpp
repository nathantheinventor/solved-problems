#include <bits/stdc++.h>

using namespace std;

bool stuff2[1 << 18];

int main() {
    vector<int> stuff;
    ios::sync_with_stdio(false);
    int x;
    cin >> x;
    while (x >= 0) {
        stuff.push_back(x);
        stuff2[x] = true;
        cin >> x;
    }
    int i = 0;
    for (int x: stuff) {
        int ans = 0;
        for (int i = 0; i < 18; i ++) {
            if (x & (1 << i)) {
                continue;
            }
            int tmp = x | (1 << i);
            if (stuff2[tmp]) {
                ans ++;
            }
            for (int j = 0; j < i; j ++) {
                int tmp2 = tmp ^ (1 << j);
                if (stuff2[tmp2]) {
                    ans ++;
                }
            }
        }
        cout << x << ":" << ans << endl;
    }
}