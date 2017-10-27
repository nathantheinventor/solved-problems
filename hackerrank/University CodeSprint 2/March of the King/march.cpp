#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

char secret[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
char board[8][8] = {0};
int neighbors[8][2] = {{-1, -1}, {-1, 0}, {-1, 1},
                       { 0, -1},          { 0, 1},
                       { 1, -1}, { 1, 0}, { 1, 1}};

ull mask(ull i, ull j) {
    return 1 << (8 * i + j);
}

bool inBounds(int x, int y) {
    return x >= 0 and y >= 0 and x < 8 and y < 8;
}

ull recurse(int x, int y, int pos, ull taken) {
    if (secret[pos] == 0) {
        return 1;
    }
    ull ans = 0;
    for (int k = 0; k < 8; k ++) {
        int i = neighbors[k][0] + x;
        int j = neighbors[k][1] + y;
        if (inBounds(i, j) and board[i][j] == secret[pos] and !(taken & mask(i, j))) {
            ans += recurse(i, j, pos + 1, taken | mask(i, j));
        }
    }
    return ans;
}

int main() {
    int k;
    cin >> k;
    
    for (int i = 0; i < k; i ++) {
        cin >> secret[i];
    }
    for (int i = 0; i < 8; i ++) {
        for (int j = 0; j < 8; j ++) {
            cin >> board[i][j];
        }
    }
    ull ans = 0;
    for (int i = 0; i < 8; i ++) {
        for (int j = 0; j < 8; j ++) {
            if (board[i][j] == secret[0]) {
                ans += recurse(i, j, 1, mask(i, j));
            }
        }
    }
    cout << ans << endl;
    
    return 0;
}
