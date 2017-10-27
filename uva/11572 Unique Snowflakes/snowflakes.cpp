#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

typedef pair<int, int> pa;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        map<int, int> freq;
        int lastBreak = 0;
        int maxUnique = 0;
        for (int i = 1; i <= n; i ++) {
            int x;
            cin >> x;
            if (freq[x] > 0) {
                lastBreak = max(lastBreak, freq[x]);
            }
            freq[x] = i;
            maxUnique = max(maxUnique, i - lastBreak);
        }
        cout << maxUnique << endl;
    }
}