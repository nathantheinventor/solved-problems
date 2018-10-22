#include <iostream>
#include <cmath>
#include <stack>
#include <vector>

using namespace std;
typedef unsigned long long ull;
typedef long long ll;

int main() {
    int t; cin >> t;
    while (t > -1) {
        int n = t;
        vector<int> nums;
        ll sum = 0;
        while (t --) {
            int x; cin >> x;
            nums.push_back(x);
            sum += x;
        }
        if (sum % n != 0) {
            cout << -1 << endl;
        } else {
            ll ans = 0;
            ll avg = sum / n;
            for (int x: nums) {
                ans += abs(x - avg);
            }
            cout << (ans / 2) << endl;
        }
        cin >> t;
    }
}