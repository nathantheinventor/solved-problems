#include <bits/stdc++.h>

using namespace std;

int board[1005];

int main() {
    int n, m, c;
    cin >> n >> m >> c;
    fill(board, board + 1004, -1);
    board[0] = 0;
    board[n + 1] = c;
    int unfilled = n;
    
    while (m -- and unfilled > 0) {
        int x;
        cin >> x;
        int lo = 1, hi = n;
        int sm = 0, lg = c;
        for (int i = 0; i <= n + 1; i ++) {
            if (board[i] != -1 and board[i] <= x) {
                lo = i + 1;
                sm = board[i];
            }
            if (board[n + 1 - i] != -1 and board[n + 1 - i] >= x) {
                hi = n - i;
                lg = board[n + 1 - i];
            }
        }
        if (sm == x and lo <= n) {
            cout << lo << endl;
            if (board[lo] == -1) unfilled --;
            board[lo] = x;
            continue;
        }
        if (lg == x and hi >= 1) {
            cout << hi << endl;
            if (board[hi] == -1) unfilled --;
            board[hi] = x;
            continue;
        }
        
        int pos = lo + (hi - lo + 1) * ((x - sm) / (lg - sm));
        if (board[pos] == -1) unfilled --;
        board[pos] = x;
        cout << pos << endl;
    }
}