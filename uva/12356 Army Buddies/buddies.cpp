#include <iostream>

using namespace std;

int soldiers[100000][2];

int main() {
    int s, b;
    cin >> s >> b;
    while (s > 0) {
        for (int i = 0; i < s; i ++) {
            soldiers[i][0] = i;
            soldiers[i][1] = i + 2;
        }
        soldiers[0][0] = -1;
        soldiers[s - 1][1] = -1;
        for (int i = 0; i < b; i ++) {
            int l, r;
            cin >> l >> r;
            l --;
            r --;
            int left = soldiers[l][0];
            int right = soldiers[r][1];
            if (right > -1) {
                soldiers[right - 1][0] = soldiers[l][0];
            }
            if (soldiers[l][0] > -1) {
                cout << soldiers[l][0] << " ";
            } else {
                cout << "* ";
            }
            if (left > -1) {
                soldiers[left - 1][1] = soldiers[r][1];
            }
            if (soldiers[r][1] > -1) {
                cout << soldiers[r][1] << "\n";
            } else {
                cout << "*\n";
            }
        }
        cout << "-" << endl;
        cin >> s >> b;
    }
}