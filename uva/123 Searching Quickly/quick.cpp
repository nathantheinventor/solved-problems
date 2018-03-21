#include <bits/stdc++.h>

using namespace std;

string lower(string s) {
    string tmp;
    for (char c: s) {
        tmp += tolower(c);
    }
    return tmp;
}

string filter(string x) {
    string ans;
    for (char c: x) {
        if ('A' <= c and c <= 'Z') {
            ans += c;
        }
    }
    return ans;
}

bool cmpKeyword(string a, string b) {
    if (lower(a) == lower(b) and filter(a) == filter(b)) {
        return a < b;
    }
    return filter(a) < filter(b);
}

set<string> filters;

string upper(string s) {
    string tmp;
    for (char c: s) {
        tmp += toupper(c);
    }
    return tmp;
}

vector<string> split(string s) {
    vector<string> ans;
    string tmp;
    for (char c: s) {
        if (c == ' ') {
            ans.push_back(tmp);
            tmp = "";
        } else {
            tmp += c;
        }
    }
    if (tmp != "") {
        ans.push_back(tmp);
    }
    return ans;
}

string join(string sep, vector<string> input) {
    string ans;
    bool started = false;
    for (string s: input) {
        if (started) {
            ans += sep + s;
        } else {
            started = true;
            ans += s;
        }
    }
    return ans;
}

vector<string> cap(string s) {
    vector<string> words = split(s);
    vector<string> ans;
    int i = 0;
    for (string x: words) {
        if (filters.count(x) == 0) {
            vector<string> tmp = words;
            tmp[i] = upper(tmp[i]);
            ans.push_back(join(" ", tmp));
        }
        i ++;
    }
    return ans;
}

int main() {
    vector<string> titles;
    
    string s;
    cin >> s;
    while (s != "::") {
        filters.insert(lower(s));
        cin >> s;
    }
    getline(cin, s);
    while (getline(cin, s)) {
        titles.push_back(lower(s));
    }
    
    vector<string> final;
    
    for (string s: titles) {
        for (string x: cap(s)) {
            final.push_back(x);
        }
    }
    
    stable_sort(final.begin(), final.end(), cmpKeyword);
    
    for (string s: final) {
        cout << s << endl;
    }
}