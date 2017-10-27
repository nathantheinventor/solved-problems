#include <iostream>

using namespace std;

int main() {
    long long n, m;
    while (cin >> n >> m) {
        m = n - m;
        //cout << m << " " << n << endl;
        long long ans = 1;
        for (long long i = m + 1; i <= n; i ++) {
            //cout << ans << endl;
            ans *= i;
            while (ans % 10 == 0) {
                ans /= 10;
            }
            ans = ans % 100000000000;
        }
        cout << (ans % 10) << endl;
    }
}