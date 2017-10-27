#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>

#include <typeinfo>
#include <map>
using namespace std;

typedef vector<int> vec;

int convert(int x) {
    return x;
}

struct Node {
    Node* subNodes[10] = {nullptr};
    int elems = 0;
    int size;
    Node(int n) {
        size = n;
    }
    void insert(int x) {
        cout << "inserting " << x << endl;
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
    int greater(int x) {
        if (size == 0) {
            return 0;
        }
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

int main() {
    Node tree(100000);
    int n, m, k;
    cin >> n >> m >> k;
    long long sum = 0;
    vector<int> nums(n, 0);
    map<int, vec* > indices;
    for (int i = 0; i < n; i ++) {
        int x;
        cin >> x;
        sum += x;
        nums[i] = x;
        if (indices.find(x) != indices.end()) {
            indices[x]->push_back(i + 1);
        } else {
            vector<int> *v = new vector<int>();
            v->push_back(i + 1);
            indices[x] = v;
        }
    }
    //vector<int> sorted_nums = nums;
    //sort(sorted_nums.begin(), sorted_nums.end());
    vector<int> s(k, 0);
    for (int i = 0; i < k; i ++) {
        int x;
        cin >> x;
        for (int j = 0; j < nums.size(); j ++) {
            if (nums[j] == x) {
                //cout << "inserting " << j + 1 << endl;
                tree.insert(j + 1);
            }
        }
        s[i] = x;
    }
    
    for (int i = 0; i < m; i ++) {
        long long a, b, c;
        cin >> a >> b >> c;
        sum += c * (b - a + 1);
        
        long long starred = tree.greater(a - 1) - tree.greater(b);
        //cout << starred << endl;
        sum -= starred * c;
        
        
        for (int j = 0; j < k; j ++) {
            s[j] -= c;
            if (indices.find(s[j]) != indices.end()) {
                vector<int> v = *indices[s[j]];
                vector<int> v2 = v;
                //cout << v.size() << endl;
                for (int e = 0; e < v.size(); e ++) {
                    stringstream ss;
                    int f;
                    ss << v.at(e);
                    ss >> f;

                    if (f <= b and f >= a and tree.greater(f) == tree.greater(f - 1)) {
                        tree.insert(f);
                    }
                }
            }
            
        }
        
        cout << sum << "\n";
    }
    return 0;
}
