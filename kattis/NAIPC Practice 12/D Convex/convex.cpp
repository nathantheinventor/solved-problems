#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;

int key(pii p) {
    return p.first + p.second;
}

bool cmp(pii x, pii y) {
    return key(x) < key(y);
}

double key2(pii p) {
    return (double) p.first / (double) p.second;
}

bool cmp2(pii x, pii y) {
    return key2(x) < key2(y);
}

bool tmp1[1000000];

int main() {
    vector<pii> tmp, tmp2;
    for (int i = 1; i < 1000; i ++) {
        for (int j = 1; j < 1000; j ++) {
            int g = __gcd(i, j);
            if (not tmp1[(i / g) * 1000 + j / g]) {
                tmp.push_back({i / g, j / g});
                tmp1[(i / g) * 1000 + j / g] = true;
            }
        }
    }
    int ans1 = 0;
    int ans2 = 0;
    sort(tmp.begin(), tmp.end(), cmp);
    
    for (int i = 0; i < 100000; i ++) {
        tmp2.push_back(tmp[i]);
    }
    
    sort(tmp2.begin(), tmp2.end(), cmp2);
    
    vector<pii> solution;
    int x = 0, y = 20000000;
    
    for (pii p: tmp2) {
        solution.push_back({x, y});
        x += p.first;
        y -= p.second;
    }
    reverse(tmp2.begin(), tmp2.end());
    for (pii p: tmp2) {
        solution.push_back({x, y});
        x += p.first;
        y += p.second;
    }
    reverse(tmp2.begin(), tmp2.end());
    for (pii p: tmp2) {
        solution.push_back({x, y});
        x -= p.first;
        y += p.second;
    }
    reverse(tmp2.begin(), tmp2.end());
    for (pii p: tmp2) {
        solution.push_back({x, y});
        x -= p.first;
        y -= p.second;
    }
    
    int n;
    cin >> n;
    for (int i = 0; i < n; i ++) {
        cout << solution[i].first << " " << solution[i].second << endl;
    }
}