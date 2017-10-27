#include <iostream>

int min(int a, int b, int c) {
    if (a < b and a < c) {
        return a;
    } else if (b < a and b < c) {
        return b;
    } else {
        return c;
    }
}

int max(int a, int b, int c) {
    if (a > b and a > c) {
        return a;
    } else if (b > a and b > c) {
        return b;
    } else {
        return c;
    }
}

using namespace std;

int main() {
    int n;
    cin >> n;
    int caseNum = 1;
    while (n --) {
        int a, b, c;
        cin >> a >> b >> c;
        int ans = a + b + c - max(a, b, c) - min(a, b, c);
        cout << "Case " << caseNum++ << ": " << ans << endl;
    }
}