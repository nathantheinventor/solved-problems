#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

bool solve(ld x, ld y, ld n, ld r) {
    r = 1.0 + r / 1200.0;
    n = n * 12.0;
    
    ld exp;
    if (r == 1.0) {
        exp = x - y * n; 
    } else {
        ld tmp = pow(r, n);
        exp = x * tmp - y * ((1.0 - tmp) / (1.0 - r));
    }
    return exp <= 0;
}

int main() {
    ios::sync_with_stdio(false);
    ld x, y, n, r;
    // cin >> x >> y >> n >> r;
    scanf("%Lf %Lf %Lf %Lf\n", &x, &y, &n, &r);
    while (x > 0) {
        if (solve(x, y, n, r)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
        // cin >> x >> y >> n >> r;
        scanf("%Lf %Lf %Lf %Lf\n", &x, &y, &n, &r);
    }
}