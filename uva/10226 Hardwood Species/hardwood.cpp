#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    string trash;
    getline(cin, trash);
    getline(cin, trash);
    while (t --) {
        string s;
        map<string, int> counts;
        double total = 0;
        while (getline(cin, s) and s != "") {
            counts[s] ++;
            total ++;
        }
        for (auto tmp: counts) {
            s = tmp.first;
            cout << s << " " << fixed << setprecision(4) << counts[s] / total * 100.0 << endl;
        }
        if (t) {
            cout << endl;
        }
    }
}