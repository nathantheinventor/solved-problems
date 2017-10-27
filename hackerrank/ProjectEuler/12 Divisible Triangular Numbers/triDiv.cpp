#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define SIZE 500000000

int factors[SIZE] = {0};
int main() {
    for (int i = 2; i < SIZE; i ++) {
        factors[i] += 2;
        for (int j = 2 * i; j < SIZE; j += i) {
            factors[j]++;
        }
    }
    factors[1] = 1;
    int cur = 1;
    int add = 2;
    int m = 0;
    for (int i = 0; cur + add < SIZE; i ++) {
        cur += add++;
        if (factors[cur] > m) {
            cout << cur << " " << factors[cur] << endl;
            cout << endl;
            m = factors[cur];
        }
    }
    cout << m << endl;
    return 0;
}
