#include <iostream>

using namespace std;

char seq[5001];

int backwards[5001];

int main() {
    string s;
    cin >> s;
    char* ptr = seq;
    for (char c: s) {
        *(ptr ++) = c;
    }
    
    int len = ptr - seq;
    int n = len;
    
    int last = 0;
    //cout << seq << endl;
    bool neg = false;
    while (len --) {
        if (neg) {
            backwards[len] = -1;
            continue;
        }
        backwards[len] = last;
        //cout << seq[len] << endl;
        if (seq[len] == ')') {
            last ++;
        } else {
            last --;
        }
        if (last < 0) {
            neg = true;
        }
    }
    
    for (int i = 0; i < n; i ++) {
        //cout << backwards[i] << endl;
    }
    
    bool possible = false;
    
    for (int i = 0; i < n; i ++) {
        int sum = 0;
        bool neg = false;
        for (int j = 0; j < i; j ++) {
            if (seq[j] == '(') {
                sum ++;
            } else {
                sum --;
            }
            if (sum < 0) {
                neg = true;
                break;
            }
        }
        if (neg) {
            break;
        }
        if (i > 0 and sum == backwards[i - 1]) {
            possible = true;
            break;
        }
        for (int j = i; j < n; j ++) {
            
            if (seq[j] == ')') {
                sum ++;
            } else {
                sum --;
            }
            if (sum < 0) {
                break;
            }
            if (sum == backwards[j]) {
                possible = true;
                break;
            }
        }
        if (possible) {
            break;
        }
    }
    if (possible) {
        cout << "possible" << endl;
    } else {
        cout << "impossible" << endl;
    }
}