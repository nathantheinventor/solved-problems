#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;
    int z = 0;
    int o = 0;
    for (int i = 1; i <= s.size(); i ++) {
        if (s[i - 1] == '0') {
            o++;
        } else {
            z++;
        }
    }
    
    if (o - z < 1) {
        cout << "-1" << endl;
        exit(0);
    }
    
    vector<vector<int>> ans(o - z);
    set<int> ones;
    set<int> zeros;
    for (int i = 0; i < o - z; i ++) {
        zeros.insert(i);
    }
    
    int index = 1;
    for (char c: s) {
        if (c == '0') {
            if (zeros.size() == 0) {
                cout << "-1" << endl;
                exit(0);
            }
            int pos = *zeros.begin();
            ans[pos].push_back(index);
            zeros.erase(zeros.begin());
            ones.insert(pos);
        } else {
            if (ones.size() == 0) {
                cout << "-1" << endl;
                exit(0);
            }
            int pos = *ones.begin();
            ans[pos].push_back(index);
            ones.erase(ones.begin());
            zeros.insert(pos);
        }
        index ++;
    }
    
    if (zeros.size() > 0) {
        cout << "-1" << endl;
        exit(0);
    }
    
    cout << ans.size() << endl;
    for (auto line: ans) {
        cout << line.size();
        for (auto x: line) {
            cout << " " << x;
        }
        cout << endl;
    }
}