#include <bits/stdc++.h>

using namespace std;

vector<int> primes;

void sieve() {
    vector<bool> isPrime(1000, true);
    isPrime[0] = false;
    isPrime[1] = false;
    for (int i = 4; i < 1000; i += 2) {
        isPrime[i] = false;
    }
    for (int i = 3; i < 40; i += 2) {
        if (isPrime[i]) {
            for (int j = i * i; j < 1000; j += 2 * i) {
                isPrime[j] = false;
            }
        }
    }
    for (int i = 0; i < 1000; i ++) {
        if (isPrime[i]) {
            primes.push_back(i);
        }
    }
}

set<int> factor(int x) {
    set<int> ans;
    for (int i: primes) {
        while (x % i == 0) {
            ans.insert(i);
            x /= i;
        }
        if (x == 1) {
            break;
        }
    }
    if (x > 1) {
        ans.insert(x);
    }
    return ans;
}

int max(set<int> items) {
    int ans = 0;
    for (int i: items) {
        ans = max(i, ans);
    }
    return ans;
}

int dp[100]; // max score using k partitions
int cur[100]; // current GCD of recent items

int main() {
    sieve();
    int n, k;
    cin >> n >> k;
    vector<set<int>> items;
    vector<int> nums;
    for (int i = 0; i < n; i ++) {
        int v;
        cin >> v;
        nums.push_back(v);
        items.push_back(factor(v));
    }
    
    dp[0] = max(items[0]);
    cur[0] = nums[0];
    
    for (int j = 0; j < n; j ++) {
        for (int i = 0; i < k; i ++) {
            int g = __gcd(cur[i], nums[j]);
            cur[i] = g;
            dp[i] = min(dp[i], max(factor(g)));
            if (i > 0) {
                int tmp = min(dp[i - 1], max(items[j]));
                if (tmp > dp[i]) {
                    dp[i] = tmp;
                    cur[i] = __gcd(cur[i - 1], nums[j]);
                }
            }
            cerr << dp[i] << "\t" << cur[i] << "\t";
        }
        cerr << endl;
    }
    cout << dp[k - 1] << endl;
}