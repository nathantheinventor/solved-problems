#include <bits/stdc++.h>

using namespace std;

bool isPrime(int x) {
    if (x < 2) {
        return false;
    }
    if (x < 4) {
        return true;
    }
    if (x % 2 == 0) {
        return false;
    }
    for (int i = 3; i <= sqrt(x) + 1; i += 2) {
        if (x % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    if (isPrime(n)) {
        cout << 1 << endl << n << endl;
    } else if (isPrime(n - 2)) {
        cout << 2 << endl << "2 " << (n - 2) << endl;
    } else {
        n -= 3;
        for (int i = 3; i < n; i += 2) {
            if (isPrime(i) and isPrime(n - i)) {
                cout << 3 << endl;
                cout << "3 " << i << " " << (n - i) << endl;
                break;
            }
        }
    }
}