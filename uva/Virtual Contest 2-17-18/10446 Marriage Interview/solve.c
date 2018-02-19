#include <stdio.h>

typedef long long datatype;
datatype count;

datatype trib(int n, unsigned int back) {
    datatype sum=0;
    int i;
    count++;
    if(n<=0) return 0;
    if(n==1) return 1;
    for(i=1; i<=back; i++) {
        sum+=trib(n-i,back);
    }
    return sum;
}

datatype dp[70][70];

datatype solve(datatype a, datatype b) {
    if (a < 0 || b < 0) {
        return 1;
    }
    datatype increment = 0;
    for (int i = 0; i < b && a - 1 - i >= 1; i ++) {
        increment += dp[a - 1 - i][b] - dp[a - 2 - i][b];
    }
    return dp[a - 1][b] + increment;
}

int main() {
    count=0;
    datatype a, b;
    int i = 0;
    for (int i = 0; i < 10; i ++) {
        for (int j = 0; j < 70; j ++) {
            count = 0;
            trib(i, j);
            dp[i][j] = count;
        }
        count = 0;
        trib(i, 1);
        // printf("%llu %llu %llu\t", count, solve(i, 1), (datatype) 0 - (datatype) 1);
// 
        // printf("\n");
    }
    
    for (int i = 10; i < 70; i ++) {
        for (int j = 0; j < 70; j ++) {
            dp[i][j] = solve(i, j);
        }
    }
    scanf("%llu %llu", &a, &b);
    while (a <= 60) {
        if (a < 0 || b < 0) {
            printf("Case %d: %llu\n", ++i, (datatype) 1);
        } else {
            printf("Case %d: %llu\n", ++i, dp[a][b]);
        }
        scanf("%llu %llu", &a, &b);
    }
    
    
}