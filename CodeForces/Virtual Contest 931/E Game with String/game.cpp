#include <bits/stdc++.h>

using namespace std;

double charFreq[26];
double solutions[26];
int follows[26][26];

int main() {
    string input;
    cin >> input;
    int n = input.size();
    for (int delta = 0; delta < n; delta ++) {
        charFreq[input[delta] - 'a'] ++;
        for (int i =0;i < 26; i ++) {
            for (int j =0;j < 26; j ++) {
                follows[i][j] = 0;
            }
        }
        for (int i = 0; i < n; i ++) {
            char first = input[i] - 'a';
            char second = input[(i + delta) % n] - 'a';
            follows[first][second] ++;
        }
        for (int i = 0; i < 26; i ++) {
            double num = 0;
            double denom = 0;
            for (int j = 0; j < 26; j ++) {
                if (follows[i][j] == 1) {
                    denom ++;
                }
                num += follows[i][j];
            }
            if (num > 0) {
                solutions[i] = max(solutions[i], denom / num);
            }
        }
    }
    
    double ans = 0;
    for (int i = 0; i < 26; i ++) {
        // cout <<(char)('a' + i) << " " << charFreq[i] << " " << solutions[i] << endl;
        ans += charFreq[i] / (double)n * solutions[i];
    }
    cout << ans << endl;
}