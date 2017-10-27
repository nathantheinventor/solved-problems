#include <iostream>
#include <vector>

using namespace std;

struct Node {
    Node* subNodes[10] = {nullptr};
    int elems = 0;
    int size;
    Node(int n) {
        size = n;
    }
    void insert(int x) {
        elems ++;
        if (size == 0) {
            return;
        }
        int sub = x / size;
        if (subNodes[sub] == nullptr) {
            subNodes[sub] = new Node(size / 10);
        }
        subNodes[sub]->insert(x % size);
    }
    void remove(int x, bool child=false) {
        //check if it exists
        if (!child) {
            int sub = x / size;
            Node* subElem = subNodes[sub];
            while (subElem != nullptr and subElem->size > 0) {
                int tmp = x % subElem->size;
                sub = tmp / subElem->size;
                subElem = subElem->subNodes[sub];
            }
            if (subElem == nullptr or subElem->elems == 0) {
                return;
            }
        }
        //remove it
        elems --;
        int sub = x / size;
        Node* subElem = subNodes[sub];
        if (subElem != nullptr) {
            subElem->remove(x % size, true);
        }
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
    void getElems(vector<int>& data, int x = 0) {
        if (size == 0) {
            data.push_back(x);
            return;
        }
        for (int i = 0; i < 10; i ++) {
            if (subNodes[i] != nullptr) {
                subNodes[i]->getElems(data, x + i * size);
            }
        }
    }
};

int main() {
    int n, k, x;
    while (cin) {
        cin >> n >> k;
        Node negs(100000);
        Node zeros(100000);
        for (int i = 1; i <= n; i ++) {
            cin >> x;
            if (x < 0) {
                negs.insert(i);
            } else if (x == 0) {
                zeros.insert(i);
            }
        }
        /*vector<int> data;
        negs.getElems(data);
        cout << "negs: ";
        for (auto i: data) {
            cout << i << "\t";
        }
        cout << endl;*/
        for (int i = 1; i <= k; i ++) {
            char command;
            int v1, v2;
            cin >> command >> v1 >> v2;
            if (command == 'C') {
                zeros.remove(v1);
                negs.remove(v1);
                if (v2 < 0) {
                    negs.insert(v1);
                } else if (v2 == 0) {
                    zeros.insert(v1);
                }
            } else {
              
                vector<int> data;
                negs.getElems(data);
                cout << endl << "negs: ";
                for (auto i: data) {
                    cout << i << "\t";
                }
                cout << endl;
                int zerosBetween = zeros.greater(v1 - 1) - zeros.greater(v2);
                int negsBetween  = negs .greater(v1 - 1) - negs .greater(v2);
                if (zerosBetween > 0) {
                    cout << 0;
                } else if (negsBetween % 2 == 0) {
                    cout << '+';
                } else {
                    cout << '-';
                }
            }
        }
        cout << endl;
    }
}