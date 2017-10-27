#include <iostream>
#include <algorithm>

using namespace std;

int dp[(1 << 16)+5] = {-1}; // just the first elem is -1, the rest are 0

int flashlight = 0x8000;

int cost[16];

int solve(int mask, int n) {
    if (dp[mask] != 0) {
        return dp[mask]; // this will return -1 for mask=0
    }
    //printf("After dp: %x\n", mask);
    
    int ans = 10000000;
    if (mask & flashlight) {
        //printf("Option 1: %x\n", mask);
        // send two people over
        for (int i = 0; i < n; i ++) {
            if (!(mask & (1 << i))) {
                continue;
            }
            //printf("i: %d\n", i);
            for (int j = i + 1; j < n; j ++) {
                //printf("%d: %d\n", j, mask & (1 << j));
                if (!(mask & (1 << j))) {
                    continue;
                }
                //printf("i and j: %d, %d\n", i, j);
                int c = max(cost[j], cost[i]);
                c += solve(mask - flashlight - (1 << i) - (1 << j), n);
                ans = min(ans, c);
            }
        }
    } else {
        //printf("Option 2: %x\n", mask);
        for (int i = 0; i < n; i ++) {
            if (mask & (1 << i)) {
                continue;
            }
            int c = cost[i];
            c += solve(mask | flashlight | (1 << i), n);
            ans = min(ans, c);
        }
    }
    //printf("%x, %d, %d\n", mask, n, ans);
    dp[mask] = ans;
    return dp[mask];
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i ++) {
        cin >> cost[i];
    }
    int ans = solve(((1 << n) - 1) | flashlight, n);
    
    // undoing the -1 for dp[0]
    cout << (ans + 1) << endl;
}