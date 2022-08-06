#include <iostream>

using namespace std;

typedef long long ll;

#define MAX 2000000000
#define SIZE 262144

int data[SIZE];
int segment_tree[SIZE * 2 + 50][11];

void update(int i, int j, int k) {
    int l = 0, m = 0;
    for (int n = 0; n < 11; n ++) {
        if (segment_tree[i][l] < segment_tree[j][m]) {
            segment_tree[k][n] = segment_tree[i][l ++];
        } else {
            segment_tree[k][n] = segment_tree[j][m ++];
        }
    }
}

void update_val(int i, int val) {
    data[i] = val;
    segment_tree[i][0] = val;
    int x = i;
    int x2 = i;
    int seg_size = SIZE;
    int seg_sum = 0;
    while (seg_size > 1) {
        x -= x % 2;
        x2 /= 2;
        int next = seg_sum + seg_size + x2;
        seg_sum += seg_size;
        seg_size /= 2;
        update(x, x + 1, next);
        // cerr << x << " " << next << endl;
        // cerr << next << " ";
        // for (int j = 0; j < 11; j ++) {
        //     cerr << segment_tree[next][j] << " ";
        // }
        // cerr << endl;
        x = next;
    }
}

void rmq(int l, int r, int size = SIZE, int index = 2 * SIZE) {
    // cerr << l << " " << r << " " << size << " " << index << endl;
    if (l % size == 0 and r - l + 1 == size) {
        int pos = 0;
        for (int sz = 1; sz < size; sz *= 2) {
            pos += SIZE / sz;
            l /= 2;
        }
        // cerr << l << " " << r << " " << (pos + l) << endl;
        for (int i = 0; i < 11; i ++) {
            segment_tree[index][i] = segment_tree[pos + l][i];
        }
    } else {
        int middle = l - (l % size) + size / 2;
        if (r < middle or l >= middle) {
            rmq(l, r, size / 2, index);
        } else {
            rmq(l, middle - 1, size / 2, index + 1);
            rmq(middle, r, size / 2, index + 2);
            update(index + 1, index + 2, index);
        }
    }
    // cerr << l << " " << r << " ";
    // for (int i = 0; i < 11; i ++) {
    //     cerr << segment_tree[index][i] << " ";
    // }
    // cerr << endl;
}

bool overlap(int x, int y) {
    while (x and y) {
        if ((x % 10) and (y % 10)) {
            return true;
        }
        x /= 10; y /= 10;
        // tmp *= 10;
    }
    return false;
}

int solve(int index = 2 * SIZE) {
    int ans = MAX;
    for (int i = 0; i < 11; i ++) {
        int x = segment_tree[index][i];
        // cerr << x << endl;
        if (x == MAX) {
            continue;
        }
        for (int j = i + 1; j < 11; j ++) {
            // cerr << i << " " << j << endl;
            int y = segment_tree[index][j];
            if (y == MAX) {
                continue;
            }
            if (overlap(x, y)) {
                ans = min(ans, x + y);
            }
        }
    }
    if (ans == MAX) {
        return -1;
    }
    return ans;
}

int main() {
    fill(data, data + SIZE, MAX);
    for (int i = 0; i < 2 * SIZE; i ++){
        fill(segment_tree[i], segment_tree[i] + 11, MAX);
    }
    int n, m; cin >> n >> m;
    for (int i = 0; i < n; i ++) {
        cin >> data[i];
    }
    for (int i = 0; i < SIZE; i ++) {
        segment_tree[i][0] = data[i];
    }
    int size = SIZE;
    int start = 0;
    while (size > 1) {
        for (int i = 0; i < size; i += 2) {
            update(start + i, start + i + 1, start + size + i / 2);
        }
        start += size;
        size /= 2;
    }
    while (m --) {
        int type; cin >> type;
        if (type == 1) {
            int i, x; cin >> i >> x;
            // cerr << 1 << " " << i << " " << x << endl;
            update_val(i - 1, x);
        } else {
            int l, r; cin >> l >> r;
            rmq(l - 1, r - 1);
            // for (int i = 0; i < 5; i ++) {
            //     cerr << segment_tree[SIZE + SIZE / 2][i] << " ";
            // }
            // cerr << endl;
            // cerr << 2 << " " << l << " " << r << endl;
            // cerr << "----" << endl;
            cout << solve() << endl;
            // cerr << 2 << " " << l << " " << r << endl;
        }
    }
    // cout << overlap(20, 20) << endl;
}