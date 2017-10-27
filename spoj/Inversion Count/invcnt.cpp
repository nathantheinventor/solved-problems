#include <iostream>

using namespace std;
int pos = 0;
struct Node;

Node* newNode(int);

struct Node {
    Node* subNodes[10] = {nullptr};
    int elems = 0;
    int size;
    void insert(int x) {
        elems ++;
        if (size == 0) {
            return;
        }
        int sub = x / size;
        if (subNodes[sub] == nullptr) {
            subNodes[sub] = newNode(size / 10);
        }
        subNodes[sub]->insert(x % size);
    }
    int greater(int x) {
        int ans = 0;
        int sub = x / size;
        for (int i = sub + 1; i < 10; i ++) {
            if (subNodes[i] != nullptr) {
                ans += subNodes[i]->elems;
            }
        }
        if (subNodes[sub] != nullptr) {
            ans += subNodes[sub]->greater(x % size);
        }
        return ans;
    }
};

Node nodes[400000];
Node* newNode(int size) {
	Node& n = nodes[pos++];
	n.size = size;
	return &n;
}


int main() {
    int n;
    cin >> n;
    while (n--) {
    	pos = 0;
        Node root = *newNode(1000000);
        int m;
        cin >> m;
        long long ans = 0;
        while (m--) {
            int x;
            cin >> x;
            ans += root.greater(x);
            root.insert(x);
        }
        cout << ans << endl;
    }
}