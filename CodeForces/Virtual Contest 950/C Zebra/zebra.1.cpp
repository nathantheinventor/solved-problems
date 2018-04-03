#include <bits/stdc++.h>

using namespace std;

int main() {
    set<int> zeros;
    set<int> ones;
    string s;
    cin >> s;
    for (int i = 1; i <= s.size(); i ++) {
        if (s[i - 1] == '0') {
            zeros.insert(i);
        } else {
            ones.insert(i);
        }
    }
    
    vector<vector<int>> ans;
    while (zeros.size() > 0 or ones.size() > 0) {
        if (zeros.size() == 0) {
            cout << "-1" << endl;
            exit(0);
        }
        int cur = *zeros.begin();
        zeros.erase(zeros.begin());
        vector<int> curAns;
        curAns.push_back(cur);
        
        while (true) {
            auto one = ones.lower_bound(cur);
            if (one == ones.end()) {
                break;
            }
            int o = *one;
            auto zero = zeros.lower_bound(o);
            if (one == ones.end()) {
                cout << "-1" << endl;
                exit(0);
            }
            int z = *zero;
            ones.erase(one);
            zeros.erase(zero);
            curAns.push_back(o);
            curAns.push_back(z);
            cur = z;
        }
        ans.push_back(curAns);
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