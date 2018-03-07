#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> data;
    int n;
    cin >> n;
    for (int i = 0; i < n; i ++) {
        int x;
        cin >> x;
        data.push_back(x);
    }
    
    set<int> totalSolutions;
    set<int> curSolutions;
    for (int i = 0; i < n; i ++) {
        set<int> tmp;
        tmp.insert(data[i]);
        totalSolutions.insert(data[i]);
        for (int j: curSolutions) {
            tmp.insert(__gcd(j, data[i]));
            totalSolutions.insert(__gcd(j, data[i]));
        }
        curSolutions = tmp;
    }
    
    // for (auto i: totalSolutions) {
    //     cout << i << endl;
    // }
    cout << totalSolutions.size() << endl;
}