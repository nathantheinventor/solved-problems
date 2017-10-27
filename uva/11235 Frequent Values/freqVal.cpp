#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

#define BEGIN 131072
#define SIZE 3 * BEGIN + 5

int tree[SIZE];

int rmq(int l, int r, int size = BEGIN) {
    //cout << "rmq(" << l << ", " << r << ", " << size << ")" << endl;
    if (r < l) {
        return 0;
    }
    if (r % size == size - 1 and l % size == 0) {
        int pos = BEGIN + l;
        int tmp = 1;
        while (tmp < size) {
            tmp *= 2;
            pos /= 2;
        }
        return tree[pos];
    }
    if (r % size >= size / 2 and l % size < size / 2) {
        int mid = r - (r % size) + size / 2;
        return max(rmq(mid, r, size / 2), rmq(l, mid - 1, size / 2));
    }
    return rmq(l, r, size / 2);

}

int main() {
    int n, q;
    while (cin >> n >> q) {
        for (int i = 0; i < SIZE; i ++) {
            tree[i] = 0;
        }
        int bound = 0;
        int last = -1000000000;
        int cur = 0;
        vector<int> starts;
        vector<int> ends;
        vector<int> lengths;
        for (int i = 0; i < n; i ++) {
            int x;
            cin >> x;
            if (last == x) {
                cur ++;
            } else if (cur > 0) {
                starts.push_back(i - cur + 1);
                ends.push_back(i);
                lengths.push_back(cur);
                cur = 1;
            } else {
                cur = 1;
            }
            last = x;
        }
        starts.push_back(n - cur + 1);
        ends.push_back(n);
        lengths.push_back(cur);
        for (int i = 0; i < starts.size(); i ++) {
            int length = lengths[i];
            tree[BEGIN + i] = length;
        }
        for (int i = BEGIN - 1; i >= 0; i --) {
            tree[i] = max(tree[2*i], tree[2 * i + 1]);
        }
        while (q--) {
            int l, r;
            cin >> l >> r;
            auto start = upper_bound(starts.begin(), starts.end(), l);
            auto end   = upper_bound(starts.begin(), starts.end(), r);
            
            int start1 = distance(starts.begin(), start) - 1;
            int end1 = distance(starts.begin(), end) - 1;

            int first = ends[start1] - l + 1;
            int last = r - starts[end1] + 1;
            
            if (start1 == end1) {
                first = r - l + 1;
                last = r - l + 1;
            }

            int ans = max(first, last);
            ans = max(ans, rmq(start1 + 1, end1 - 1));
            cout << ans << endl;
        }
    }
}