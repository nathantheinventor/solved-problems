#include <iostream>
#include <cmath>
#include <stack>

using namespace std;
typedef unsigned long long ull;
typedef long long ll;

int main() {
    int t; cin >> t;
    while (t --) {
        string s; cin >> s;
        stack<char> st;
        for (char c: s) {
            switch (c) {
                case '(': break;
                case ')': cout << st.top(); st.pop(); break;
                case '+': st.push(c); break;
                case '*': st.push(c); break;
                case '/': st.push(c); break;
                case '-': st.push(c); break;
                case '^': st.push(c); break;
                default: cout << c;
            }
        }
        cout << endl;
    }
}