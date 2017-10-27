#include <bits/stdc++.h>

using namespace std;

#define MAX_SIZE 121000
#define SEG_TREE_SIZE 1048576;

struct SegmentTree {
    int segmentTree[2 * SEG_TREE_SIZE];

    // range sum query: find the sum of values in the range [l, r] (inclusive)
    int rsq(int l, int r, int size = SEG_TREE_SIZE) {
        // check to make sure r <= l
        if (r < l) {
            return 0;
        }
        // if the range given covers an entire block, return the block
        if (r % size == size - 1 and l % size == 0) {
            int pos = SEG_TREE_SIZE + l;
            int tmp = 1;
            while (tmp < size) {
                tmp *= 2;
                pos /= 2;
            }
            return segmentTree[pos];
        }


        // if the range crosses the middle, try on both sides of the middle
        if (r % size >= size / 2 and l % size < size / 2) {
            int mid = r - (r % size) + size / 2;
            return rsq(mid, r, size / 2) + rsq(l, mid - 1, size / 2);
        }
        // else the query is just on one side of the middle, so try with a smaller range
        return rsq(l, r, size / 2);
    }

    // add the value amt to the element at index i;
    int update(int i, int amt) {
        i += SEG_TREE_SIZE;
        while (i > 0) {
            segmentTree[i] += amt;
            i /= 2;
        }
        segmentTree[0] += amt;
    }
};
SegmentTree st;

// array holding 3 values, a, b, and c
// representing an edge from a to b with color c
int edges[MAX_SIZE][3];

struct Edge {
    int id; // index in the edges array;
    int color;
    bool operator<(Edge other) const {
        return color < other.color;
    }
}

// adjacency list of edges that are connected to a given node
vector<Edge> adj[MAX_SIZE];

struct DisjointSet {
    // holds two values, a and b
    // a - parent of this node or negative size of the edge
    // b - size of the subtree under this edge
    int disjointSet[MAX_SIZE][5];

    DisjointSet() {
        for (int i = 0; i < MAX_SIZE; i ++) {
            disjointSet[i][0] = -1;
            disjointSet[i][1] = -1;
        }
    }

    int root(int x) {
        while (disjointSet[x][0] > -1) {
            x = disjointSet[x][0];
        }
        return x;
    }

    int size(int x) {
        return disjointSet[x][1];
    }

    void merge(int a, int b) {
        int r1 = root(a); r2 = root(b);
        // sanity check; shouldn't be needed.
        if (r1 == r2) {
            return;
        }
        if (size(r1) > size(r2)) {
            // re-root r2 and merge with a
            
        } else {
            // re-root r1 and merge with b

        }
    }
};

int main() {
    int n; // num edges
    cin >> n;
    for (int i = 1; i < n; i ++) {
        int a, b, c; // edge from node a to node b with color c
        cin >> a >> b >> c;
        edges[i][0] = a;
        edges[i][1] = b;
        edges[i][2] = c;
        // push the edge into the adjacency list for nodes a and b
        adj[a].push_back(Edge({i, c}));
        adj[b].push_back(Edge({i, c}));
    }
    // preprocessing to form a dynamic disjoint set
    DisjointSet ds;
    for (int i = 1; i < n; i ++) {
        sort(adj[i].begin(), adj[i].end());
        int lastColor = 0;
        int lastId = 0;
        for (Edge e: adj[i]) {
            if (e.color == lastColor) {
                ds.merge(e.id, lastId);
            }
            lastColor = e.color;
            lastId = e.id;
        }
    }

    // now the actual work begins
    int q; // num queries
    cin >> q;
    while (q--) {
        int type;
        cin >> type;
        switch (type) {
            case 1:
                // change the color of an edge;
                int i, c; // node and new color
                cin >> i >> c;
                // TODO
                break;
            case 2:
                // sum of all trees between l and r
                int l, r;
                cin >> l >> r;
                cout << rsq(l, r) << "\n";
                break;
            case 3:
                // P(x) for a given i;
                int i;
                cin >> i;
                unsigned long long k = ds.size(ds.root(i));
                cout << ((k * (k - 1)) / 2) << "\n";
                break;
        }
    }
}