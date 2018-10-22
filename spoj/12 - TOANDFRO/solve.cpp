#include <iostream>
#include <cmath>
#include <stack>
#include <vector>

using namespace std;
typedef unsigned long long ull;
typedef long long ll;

int main() {
    int n; cin >> n;
    while (n > 0) {
        string s; cin >> s;
        vector<vector<char>> vvc(s.size() / n, vector<char>(n));
        int i = 0;
        for (char c: s) {
            int col = i % n;
            if ((i / n) % 2 == 1) {
                col = n - 1 - col;
            }
            vvc[i / n][col] = c;
            // cerr << (i / n) << " " << (i % n) << " " << c << endl;
            i ++;
        }
        // cerr << n << endl;
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < vvc.size(); j ++) {
                cout << vvc[j][i];
            }
        }
        cout << endl;
        cin >> n;
    }
}