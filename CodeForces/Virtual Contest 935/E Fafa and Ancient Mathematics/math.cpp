#include <bits/stdc++.h>
using namespace std;

int pos = 0;
string s;
void match(char c) {
    pos += 1;
}

bool inBounds(pair<int, int> p) {
    if (p.first == 0x3fffffff or p.second == 0xB0000000) {
        return false;
    }
    return true;
}

// ans[i] will tell the min and max values resulting from i minus signs
vector<pair<int,int>> exprMin() {
    if (s[pos] <= '9' and '1' <= s[pos]) {
        char c = s[pos];
        match(s[pos]);
        return {pair<int, int>({c - '0', c - '0'})};
    } else {
        match('(');
        auto e1 = exprMin();
        match('?');
        auto e2 = exprMin();
        match(')');
        
        // option 1: question mark is a minus sign
        vector<pair<int, int>> ans(101, pair<int, int>({0x3fffffff, 0xB0000000}));
        for (int i = 0; i < e1.size(); i ++) {
            for (int j = 0; j < e2.size(); j ++) {
                if (i + j + 1 <= 100 and inBounds(e1[i]) and inBounds(e2[j])) {
                    int min1 = e1[i].first - e2[j].second;
                    int max1 = e1[i].second - e2[j].first;
                    ans[i + j + 1].first = min(ans[i + j + 1].first, min1);
                    ans[i + j + 1].second = max(ans[i + j + 1].second, max1);
                }
            }
        }
        
        for (int i = 0; i < e1.size(); i ++) {
            for (int j = 0; j < e2.size(); j ++) {
                if (i + j <= 100 and inBounds(e1[i]) and inBounds(e2[j])) {
                    int min1 = e1[i].first + e2[j].first;
                    int max1 = e1[i].second + e2[j].second;
                    ans[i + j].first = min(ans[i + j].first, min1);
                    ans[i + j].second = max(ans[i + j].second, max1);
                }
            }
        }
        
        return ans;
    }
}

// ans[i] will tell the min and max values resulting from i minus signs
vector<pair<int,int>> exprPlus() {
    if (s[pos] <= '9' and '1' <= s[pos]) {
        char c = s[pos];
        match(s[pos]);
        return {pair<int, int>({c - '0', c - '0'})};
    } else {
        match('(');
        auto e1 = exprPlus();
        match('?');
        auto e2 = exprPlus();
        match(')');
        
        // option 1: question mark is a minus sign
        vector<pair<int, int>> ans(101, pair<int, int>({0x3fffffff, 0xB0000000}));
        for (int i = 0; i < e1.size(); i ++) {
            for (int j = 0; j < e2.size(); j ++) {
                if (i + j + 1 <= 100 and inBounds(e1[i]) and inBounds(e2[j])) {
                    int min1 = e1[i].first + e2[j].first;
                    int max1 = e1[i].second + e2[j].second;
                    ans[i + j + 1].first = min(ans[i + j + 1].first, min1);
                    ans[i + j + 1].second = max(ans[i + j + 1].second, max1);
                }
            }
        }
        
        for (int i = 0; i < e1.size(); i ++) {
            for (int j = 0; j < e2.size(); j ++) {
                if (i + j <= 100 and inBounds(e1[i]) and inBounds(e2[j])) {
                    int min1 = e1[i].first - e2[j].second;
                    int max1 = e1[i].second - e2[j].first;
                    ans[i + j].first = min(ans[i + j].first, min1);
                    ans[i + j].second = max(ans[i + j].second, max1);
                }
            }
        }
        
        return ans;
    }
}

int main() {
    cin >> s;
    int min, plus;
    cin >> plus >> min;
    if (min <= 100) {
        auto ans = exprMin();
        // for (auto i: ans) {
        //     cout << i.first << " " << i.second << endl;
        // }
        auto ans2 = ans[min];
        cout << ans2.second << endl;
    } else {
        auto ans = exprPlus();
        auto ans2 = ans[plus];
        cout << ans2.second << endl;
    }
}