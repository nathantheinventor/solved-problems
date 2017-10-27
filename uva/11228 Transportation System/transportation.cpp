#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <queue>
#include <algorithm>

using namespace std;

struct DisjointSet {
    int disjointSet[1001];
    int size; // set by outer program, if needed; keeps track of number of sets
    
    DisjointSet() {
        for (int i = 0; i < 1001; i ++) {
            disjointSet[i] = -1;
        }
    }
    
    int root(int x) {
        int orig = x; // optional path compression
        while (disjointSet[x] > -1) {
            x = disjointSet[x];
        }
        if (orig != x) {
            disjointSet[orig] = x; // optional path compression
        }
        return x;
    }
    
    void merge(int a, int b) {
        int r1 = root(a), r2 = root(b);
        if (r1 == r2) {
            // they're already connected
            return;
        }
        size --;
        int s1 = -disjointSet[r1], s2 = -disjointSet[r2];
        if (s1 > s2) {
            disjointSet[r2] = r1;
            disjointSet[r1] -= s2;
        } else {
            disjointSet[r1] = r2;
            disjointSet[r2] -= s1;
        }
    }
};

int cities[1001][2];

struct Edge {
    int from;
    int to;
    double dist;
    const bool operator<(Edge other) const {
        return dist < other.dist;
    }
};

double dist[1001][1001];

// barely-working implementation of Kruskal's algorithm
double solveMWST(int n) {
    vector<Edge> edges;
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < n; j ++) {
            edges.push_back(Edge({i, j, dist[i][j]}));
        }
    }
    
    DisjointSet ds;
    ds.size = n;
    double ans = 0.0;
    sort(edges.begin(), edges.end());
    int pos = 0;
    while (ds.size > 1) {
        Edge e = edges[pos++];
        if (ds.root(e.from) != ds.root(e.to)) {
            ds.merge(e.from, e.to);
            ans += e.dist;
        }
    }
    return ans;
}


double solveState(vector<int>& locations) {
    for (int i = 0; i < locations.size(); i ++) {
        for (int j = 0; j < locations.size(); j ++) {
            int deltaX = cities[locations[i]][0] - cities[locations[j]][0];
            int deltaY = cities[locations[i]][1] - cities[locations[j]][1];
            int distance = deltaX * deltaX + deltaY * deltaY;
            dist[i][j] = sqrt(distance);
        }
    }
    return solveMWST(locations.size());
}

double stateDist(vector<int>& state1, vector<int>& state2) {
    double minDist = 100000000000.0;
    for (auto& i: state1) {
        for (auto& j: state2) {
            int deltaX = cities[i][0] - cities[j][0];
            int deltaY = cities[i][1] - cities[j][1];
            int distance = deltaX * deltaX + deltaY * deltaY;
            minDist = min(minDist, sqrt(distance));
        }
    }
    return minDist;
}

int main() {
    int t;
    cin >> t;
    for (int set = 1; set <= t; set++) {
        DisjointSet stateDS;
        
        // read in the cities
        int n, maxDist;
        cin >> n >> maxDist;
        for (int i = 1; i <= n; i ++) {
            cin >> cities[i][0] >> cities[i][1];
        }
        
        // connect the cities in the same state
        for (int i = 1; i <= n; i ++) {
            for (int j = i + 1; j <= n; j ++) {
                int deltaX = cities[i][0] - cities[j][0];
                int deltaY = cities[i][1] - cities[j][1];
                if (deltaX * deltaX + deltaY * deltaY <= maxDist * maxDist) {
                    stateDS.merge(i, j);
                }
            }
        }
        
        // disjoint set now contains states; let's get those out
        map<int, vector<int>> states;
        for (int i = 1; i <= n; i ++) {
            int r = stateDS.root(i);
            states[r].push_back(i);
        }
        
        // answer variables
        int numStates = states.size();
        double roads = 0.0;
        double rails = 0.0;
        
        // solve the number of roads
        for (auto& i: states) {
            vector<int> state = i.second;
            roads += solveState(state);
        }
        
        // solve number of rails
        int i1 = 0;
        for (auto& i: states) {
            vector<int> state = i.second;
            int i2 = 0;
            for (auto& j: states) {
                vector<int> state2 = j.second;
                dist[i1][i2++] = stateDist(state, state2);
            }
            i1 ++;
        }
        rails = solveMWST(numStates);
        
        cout << "Case #" << set << ": " << numStates << " " << round(roads) << " " << round(rails) << endl;
    }
}