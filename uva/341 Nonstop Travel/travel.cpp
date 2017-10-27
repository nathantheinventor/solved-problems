#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    int Case = 1;
    while (n > 0) {
        vector<int> paths[n + 1][n + 1];
        int lengths[n + 1][n + 1];
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < n; j ++) {
                lengths[i + 1][j + 1] = 1000000000;
            }
        }
        for (int i = 1; i <= n; i ++) {
            int connections;
            cin >> connections;
            while (connections --) {
                int to, cost;
                cin >> to >> cost;
                if (to == i){
                    continue;
                }
                lengths[i][to] = min(cost, lengths[i][to]);
                paths[i][to] = {i};
            }
        }
        for (int k = 1; k <= n; k ++) {
            for (int i = 1; i <= n; i ++) {
                for (int j = 1; j <= n; j ++) {
                    int cost = lengths[i][k] + lengths[k][j];
                    if (cost < lengths[i][j] and i != j and j != k and i != k) {
                        //cout << i << " " << j << " " << cost << endl;
                        lengths[i][j] = cost;
                        paths[i][j] = paths[i][k];
                        for (auto& o: paths[k][j]) {
                            paths[i][j].push_back(o);
                        }
                    }
                }
            }
        }
        int from, to;
        cin >> from >> to;
        cout << "Case " << Case++ << ": Path = ";
        for (auto& i: paths[from][to]) {
            cout << i << " ";
        }
        cout << to << "; " << lengths[from][to] << " second delay" << endl;
        cin >> n;
    }
}