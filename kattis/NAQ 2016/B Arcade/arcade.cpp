#include <iostream>
#include <cstdio>

using namespace std;

typedef double dd;

int edges[600][4];

void generateEdges() {
    edges[1][0] = -1;
    edges[1][1] = -1;
    edges[1][2] = 2;
    edges[1][3] = 3;
    for (int row = 2; row < 33; row ++) {
        for (int i = 0; i < row; i ++) {
            int cur = row * (row - 1) / 2 + i + 1;
            if (i == 0) {
                edges[cur][0] = -1;
            } else {
                edges[cur][0] = (row - 2) * (row - 1) / 2 + i;
            }
            if (i == row - 1) {
                edges[cur][1] = -1;
            } else {
                edges[cur][1] = (row - 2) * (row - 1) / 2 + i + 1;
            }
            edges[cur][2] = row * (row + 1) / 2 + i + 1;
            edges[cur][3] = row * (row + 1) / 2 + i + 2;
        }
    }
}

dd edgeWeights[600][5];
dd values[600];

#define TIMES 250000

dd dp[3][600];

int main() {
    generateEdges();
    int n;
    cin >> n;
    int h = n * (n + 1) / 2;
    for (int i = 1; i <= h; i ++) {
        cin >> values[i];
    }
    dd* last = dp[0];
    for (int i = 1; i <= h; i ++) {
        dd* r = edgeWeights[i];
        cin >> r[0] >> r[1] >> r[2] >> r[3] >> r[4];
        last[i] = values[i];
    }
    dd* cur = dp[1];
    for (int i = 1; i < TIMES; i ++) {
        for (int j = 1; j <= h; j ++) {
            cur[j] = edgeWeights[j][4] * values[j];
            for (int k = 0; k < 4; k ++) {
                cur[j] += edgeWeights[j][k] * last[edges[j][k]];
            }
        }
        dd* tmp = cur;
        cur = last;
        last = tmp;
    }
    printf("%.10f\n", last[1]);
}