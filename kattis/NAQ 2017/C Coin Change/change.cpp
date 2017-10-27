#include "bits/stdc++.h"

using namespace std;

int data[100];

int dp[10000000];

int main() {
    int n;
    cin >> n;
    int max = 0;
    int last = 0;
    for (int i = n - 1; i >= 0; i --) {
        cin >> data[i];
        max = data[i] + last;
        last = data[i];
    }
    bool canonical = true;
    for (int i = 1; i <= max; i ++) {
        int min = 0xfffffff;
        bool found = false; 
        for (int j = 0; j < n; j ++) {
            //cout << data[j] << " >= " << i << endl;
            if (data[j] > i) {
                continue;
            }
            if (!found and dp[i - data[j]] + 1 < min) {
                min = dp[i - data[j]] + 1;
                //cout << i << " " << j << endl;
                found = true;
            } else if (found and dp[i - data[j]] + 1 < min) {
                canonical = false;
                //cout << i << " " << j << endl;
                break;
            }
        }
        dp[i] = min;
        if (!canonical) {
            break;
        }
    }
    if (canonical) {
        cout << "canonical" << endl;
    } else {
        cout << "non-canonical" << endl;
    }
}