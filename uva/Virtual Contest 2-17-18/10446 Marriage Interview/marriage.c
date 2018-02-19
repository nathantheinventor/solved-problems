#include <stdio.h>

typedef unsigned long long datatype;
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


void main() {
    count=0;
    datatype a, b;
    scanf("%llu %llu", &a, &b);
    trib(a, b);
    printf(" %llu\n" ,count);
}