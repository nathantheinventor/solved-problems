// Ford Fulkerson
// C++ program for implementation of Ford Fulkerson algorithm
#include <bits/stdc++.h>
using namespace std;
 
// Number of vertices in given graph
#define V 305
 
/* Returns true if there is a path from source 's' to sink 't' in
  residual graph. Also fills parent[] to store the path */
bool bfs(int rGraph[V][V], int s, int t, int parent[]) {
    // Create a visited array and mark all vertices as not visited
    bool visited[V];
    memset(visited, 0, sizeof(visited));
 
    // Create a queue, enqueue source vertex and mark source vertex
    // as visited
    queue <int> q;
    q.push(s);
    visited[s] = true;
    parent[s] = -1;
 
    // Standard BFS Loop
    while (!q.empty()) {
        int u = q.front();
        q.pop();
 
        for (int v=0; v<V; v++) {
            if (visited[v]==false && rGraph[u][v] > 0) {
                q.push(v);
                parent[v] = u;
                visited[v] = true;
            }
        }
    }
 
    // If we reached sink in BFS starting from source, then return
    // true, else false
    return (visited[t] == true);
}
 
// Returns the maximum flow from s to t in the given graph
int fordFulkerson(int graph[V][V], int s, int t) {
    int u, v;
 
    // Create a residual graph and fill the residual graph with
    // given capacities in the original graph as residual capacities
    // in residual graph
    int rGraph[V][V]; // Residual graph where rGraph[i][j] indicates
                     // residual capacity of edge from i to j (if there
                     // is an edge. If rGraph[i][j] is 0, then there is not)
    for (u = 0; u < V; u++)
        for (v = 0; v < V; v++)
             rGraph[u][v] = graph[u][v];
 
    int parent[V];  // This array is filled by BFS and to store path
 
    int max_flow = 0;  // There is no flow initially
 
    // Augment the flow while tere is path from source to sink
    while (bfs(rGraph, s, t, parent)) {
        // Find minimum residual capacity of the edges along the
        // path filled by BFS. Or we can say find the maximum flow
        // through the path found.
        int path_flow = INT_MAX;
        for (v=t; v!=s; v=parent[v]) {
            u = parent[v];
            path_flow = min(path_flow, rGraph[u][v]);
        }
 
        // update residual capacities of the edges and reverse edges
        // along the path
        for (v=t; v != s; v=parent[v]) {
            u = parent[v];
            rGraph[u][v] -= path_flow;
            rGraph[v][u] += path_flow;
        }
 
        // Add path flow to overall flow
        max_flow += path_flow;
    }
 
    // Return the overall flow
    return max_flow;
}

int graph[V][V];

int main() {
    int n, m, p;
    cin >> n >> m >> p;
    // node 301 is the source, 302 is the sink
    // nodes 0-99 are the children
    // nodes 100-199 are the toys
    // nodes 200-299 are the categories
    // node 303 is the destination for unselected toys
    for (int i = 0; i < n; i ++) {
        graph[301][i] = 1; // from the source to each child
        int toys;
        cin >> toys;
        while (toys --) {
            int toy;
            cin >> toy;
            graph[i][99 + toy] = 1; // from the child to the toys he wants
        }
    }
    
    map<int, int> toysUnused;
    for (int i = 1; i <= m; i ++) {
        toysUnused[i] = 1;
    }
    
    for (int i = 0; i < p; i ++) {
        // for each category
        int toys;
        cin >> toys;
        while (toys --) {
            int toy;
            cin >> toy;
            graph[99 + toy][200 + i] = 1; // from the toy to the category
            toysUnused[toy] = 0;
        }
        int c;
        cin >> c;
        graph[200 + i][302] = c;
    }
    
    for (int i = 1; i <= m; i ++) {
        if (toysUnused[i] == 1) {
            graph[99 + i][303] = 1;
        }
    }
    graph[303][302] = 300;
    
    cout << fordFulkerson(graph, 301, 302) << endl;
}