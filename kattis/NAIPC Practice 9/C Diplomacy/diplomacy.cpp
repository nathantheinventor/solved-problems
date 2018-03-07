#include <bits/stdc++.h>

using namespace std;

typedef bitset<100> bits;

int n, m;
vector<int> graph[100];

int solveOdd(bits);

int solveEven(bits start) {
    if (start.count() == n or start.count() == 0) {
        return 0;
    }
    bits found = start;
    int ans = 100000;
    for (int i = 0; i < n; i ++) {
        if (!found[i]) {
            bits tmp = start;
            queue<int> friends;
            friends.push(i);
            
            while (friends.size() > 0) {
                int j = friends.front();
                friends.pop();
                tmp[j] = true;
                found[j] = true;
                for (int k: graph[j]) {
                    if (not tmp[k]) {
                        friends.push(k);
                    }
                }
            }
            
            ans = min(ans, 1 + solveOdd(tmp));
        }
    }
    return ans;
}

int solveOdd(bits start) {
    if (start.count() == n or start.count() == 0) {
        return 0;
    }
    bits found = start;
    int ans = 100000;
    for (int i = 0; i < n; i ++) {
        if (found[i]) {
            bits tmp = start;
            queue<int> friends;
            friends.push(i);
            
            while (friends.size() > 0) {
                int j = friends.front();
                friends.pop();
                tmp[j] = false;
                found[j] = false;
                for (int k: graph[j]) {
                    if (tmp[k]) {
                        friends.push(k);
                    }
                }
            }
            
            ans = min(ans, 1 + solveEven(tmp));
        }
    }
    return ans;
}

int main() {
    cin >> n >> m;
    bits start;
    for (int i = 0; i < n; i ++) {
        bool x;
        cin >> x;
        start[i] = x;
    }
    
    for (int i = 0; i < m; i ++) {
        int x, y;
        cin >> x >> y;
        x --; y --;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }
    cout << min(solveEven(start), solveOdd(start)) << endl;
}