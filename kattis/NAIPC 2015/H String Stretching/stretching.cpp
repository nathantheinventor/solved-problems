#include <bits/stdc++.h>

using namespace std;

class charFreq {
    int freqs[26];
public:
    charFreq(string s) {
        for (char c: s) {
            freqs[c - 'a'] ++;
        }
    }
    
    int reduce() {
        int g = 0;
        for (int i = 0; i < 26; i ++) {
            if (freqs[i] != 0) {
                g = freqs[i];
                break;
            }
        }
        for (int i = 0; i < 26; i ++) {
            if (freqs[i] != 0) {
                g = __gcd(g, freqs[i]);
            }
        }
        for (int i = 0; i < 26; i ++) {
            freqs[i] /= g;
        }
        return g;
    }
    
    bool operator==(charFreq other) {
        for (int i = 0; i < 26; i ++) {
            if (freqs[i] != other.freqs[i]) {
                return false;
            }
        }
        return true;
    }
    void operator*=(int x) {
        for (int i = 0; i < 26; i ++) {
            freqs[i] *= x;
        }
    }
};

bool canGenerate(string s, string ans) {
    int r = s.length();
    int l = ans.length();
    int n = r/l;
    string tmpS = ans;
    for (int i = 1; i < n; i ++) {
        int x = s.rfind(ans);
        if (x < 1) {
            return false;
        }
        s = s.erase(x, l);
    }
    return s.length() == tmpS.length();
}

int main() {
    string s;
    cin >> s;
    
    charFreq cf(s);
    int gcd = cf.reduce;
    
    for (int i = 1; i <= gcd; i ++) {
        int len = s.size() / gcd * i;
        charFreq tmp = cf;
        tmp *= i;
        vector<string> ans;
        for (int j = 0; j < s.size() - len + 1; j ++) {
            string tmp2 = s.substr(j, j + len);
            if (charFreq(tmp2) == cf and canGenerate(s, tmp2)) {
                ans.push_back(tmp2);
            }
        }
        sort(ans.begin(), ans.end());
        if (ans.size() > 0) {
            cout << ans[0] << endl;
        }
    }
}