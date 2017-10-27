#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31};

int ans[16] = {1};

void recurse(int n, int used, int remaining, int prev) {
    if (remaining == 0) {
        if (binary_search(primes.begin(), primes.end(), prev + 1)) {
            for (int i = 0; i < n - 1; i ++) {
                cout << ans[i] << " ";
            }
            cout << ans[n - 1] << "\n";
        }
    }
    for (int i = 1; i <= n; i ++) {
        if (!(used & (2 << (i - 1)))) {
            if (binary_search(primes.begin(), primes.end(), (prev + i))) {
                ans[n - remaining] = i;
                recurse(n, used | (2 << (i - 1)), remaining - 1, i);
            }
        }
    }
}


int main () {
    int s;
    int i = 1;
    while (cin >> s) {
        if (i > 1) {
            cout << endl;
        }
        cout << "Case " << i++ << ":\n";
        recurse(s, 2, s - 1, 1);
    }
}