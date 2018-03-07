#include <bits/stdc++.h>

using namespace std;

int solution[1000001];

int main() {
    vector<int> cur = {0};
    int ans = 0;
    for (int i = 2; i <= 1000000; i ++) {
        vector<int> tmp = {0};
        for (int j: cur) {
            if (j + i <= 1000000) {
                ans ++;
                solution[j + i] += 1;
                tmp.push_back(j + i);
            }
        }
        cur = tmp;
    }
    
    int n;
    cin >> n;
    while (n) {
        cout << solution[n] << endl;
        cin >> n;
    }
}