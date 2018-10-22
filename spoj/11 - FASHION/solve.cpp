#include <iostream>
#include <cmath>
#include <stack>
#include <vector>

using namespace std;
typedef unsigned long long ull;
typedef long long ll;

int main() {
    int t; cin >> t;
    while (t --) {
        int n; cin >> n;
        vector<int> men;
        vector<int> women;
        for (int i = 0; i < n; i ++) {
            int x; cin >> x;
            men.push_back(x);
        }
        for (int i = 0; i < n; i ++) {
            int x; cin >> x;
            women.push_back(x);
        }
        sort(men.begin(), men.end());
        sort(women.begin(), women.end());
        ll ans = 0;
        for (int i = 0; i < n; i ++) {
            ans += men[i] * women[i];
        }
        cout << ans << endl;
    }
}