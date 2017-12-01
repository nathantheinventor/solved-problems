#include <bits/stdc++.h>

using namespace std;

int pi[5005];
int bi[5005];
int piXorBn[5005];

set<vector<int>> tmp1;

int main() {
    int n;
    cin >> n;
    
    vector<int> random;
    int x = rand() % n;
    for (int i = 0; i < n; i++) {
        cout << "? " << i << " " << x << endl;
        cin >> piXorBn[i];
    }
    
    for (int bn = 0; bn < n; bn ++) {
        bool poss = true;
        vector<int> v;
        for (int i = 0; i < n; i ++) {
            pi[i] = piXorBn[i] ^ bn;
            v.push_back(piXorBn[i] ^ bn);
            bi[pi[i]] = i;
            if (pi[i] >= n) {
                poss = false;
            }
        }
        //cout << x << endl;
        if (bi[x] != bn) {
            poss = false;
        }
        if (poss) {
            tmp1.insert(v);
        }
        //cout << bi[bn][n - 1] << endl;
    }
    
    for (int i = 0; i < n; i++) {
        cout << "? " << i << " " << n - 1 << endl;
        cin >> piXorBn[i];
    }
    
    
    for (int bn = 0; bn < n; bn ++) {
        bool poss = true;
        vector<int> v;
        for (int i = 0; i < n; i ++) {
            pi[i] = piXorBn[i] ^ bn;
            v.push_back(piXorBn[i] ^ bn);
            bi[pi[i]] = i;
            if (pi[i] >= n) {
                poss = false;
            }
        }
        if (bi[n - 1] != bn) {
            poss = false;
        }
        if (!poss) {
            tmp1.erase(v);
        }
        //cout << bi[bn][n - 1] << endl;
    }
    vector<int> v = *(tmp1.begin());
    
    int ans = tmp1.size();
    cout << "!" << endl << ans << endl;
    for (int i = 0; i < n; i++) {
        cout << v[i];
        if (i != n - 1) {
            cout << " ";
        }
    }
    cout << endl;
}