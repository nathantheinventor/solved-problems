#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t --) {
        string s;
        cin >> s;
        int n = s.size();
        int len = (n + 1) / 2;
        
        vector<int> curStr(26, 0);
        long long hash0 = 0;
        long long hash1 = 0;
        long long hash2 = 0;
        for (long long i = 0; i < len; i ++) {
            hash0 += (len - i) * (len - i) * (long long) s[i];
            hash1 += (len - i) * (long long) s[i];
            hash2 += s[i];
        }
        vector<long long> forwards;
        for (long long i = len, j = 0; i < n + len; i ++, j ++) {
            forwards.push_back(hash1);
            // cerr << hash0 << s[j] << s[(j + 1) % n] << endl;
            
            hash2 += s[i % n] - s[j];
            hash1 += hash2;
            hash1 -= s[j] * len;
            hash0 -= s[j] * len * len;
            hash0 += 2 * hash1 - hash2;
        }
        int ans = 0;
        string s2 = s;
        reverse(s2.begin(), s2.end());
        
        hash0 = 0;
        hash1 = 0;
        hash2 = 0;
        for (long long i = 0; i < len; i ++) {
            hash0 += (len - i) * (len - i) * (long long) s2[i];
            hash1 += (len - i) * (long long) s2[i];
            hash2 += s2[i];
        }
        for (long long i = len, j = 0; i < n + len; i ++, j ++) {
            hash1 == forwards[(n - j) % n] ? ans ++ : 0;
            // cerr << hash0 << s2[j] << s2[(j + 1) % n] << endl;
            // cerr << s2 << endl;
            
            hash2 += s2[i % n] - s2[j];
            hash1 += hash2;
            hash1 -= s2[j] * len;
            hash0 -= s2[j] * len * len;
            hash0 += 2 * hash1 - hash2;
        }
        cout << ans << endl;
    }
}