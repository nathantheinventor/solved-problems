#include <bits/stdc++.h>
using namespace std;

int dp[256];

char line[10050];

void gets(char* s) {
    char c = getchar();
    while (c != '\n') {
        *(s ++) = c;
    }
    *s = 0;
}

int main() {
    ios::sync_with_stdio(false);
    
    int t;
    scanf("%d", &t);
    while (t--) {
        long long ans = 0;
        for (int a = 0; a < 256; a ++) {
            dp[a] = 0;
        }
        int n;
        scanf("%d\n", &n);
        while (n --) {
            char c; int x;
            scanf("%c %d\n", &c, &x);
            dp[c] = x;
        }
        scanf("%d\n", &n);
        while (n --) {
            gets(line);
            char* l = line;
            // printf("%s\n", l);
            while (*l) {
                ans += dp[*l];
                l++;
            }
        }
        printf("%d.%02d$\n", ans / 100, ans % 100);
    }
}