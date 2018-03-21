#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    string l;
    cin >> l;
    if (l == "0") {
        cout << "0" << endl;
        return 0;
    }
    int x = l.size();
    for (int i = max(1, x - 6); i <= x; i ++) {
        string ans = "";
        long long r = 0;
        for (char c: l) {
            long long y = c - '0';
            r = r * 10l + y;
            long long z = r / i;
            r -= z * i;
            ans += (char) (z + '0');
            if (ans == "0") {
                ans = "";
            }
        }
        if (r == 0) {
            cout << ans << endl;
            return 0;
        }
    }
}