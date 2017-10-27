#include <iostream>
#include <valarray>
#include <vector>

using namespace std;

void mod (vector<valarray<int>> &data, int p) {
    for (int i = 0; i < data.size(); i ++) {
        data[i] = ((data[i] % p) + p) % p;
    }
}

void print(vector<valarray<int>> &data) {
    return;
    for (auto &line: data) {
        for (auto &val: line) {
            cout << val << " ";
        }
        cout << endl;
    }
    cout << endl;
}


// do Gaussian elimination over modular field
void solve (vector<valarray<int>> &data, int p) {
    print(data);
    // form the upper triangular matrix
    for (int i = 0; i < data.size(); i ++) {
        mod(data, p);
        print(data);
        int bottom = 1;
        while (data[i][i] == 0 and i + bottom <= data.size()) {
            //swap this till we have a workable row
            auto tmp = data[data.size() - bottom];
            data[data.size() - bottom++] = data[i];
            data[i] = tmp;
        }
        for (int j = i + 1; j < data.size(); j ++) {
            int tmp = data[j][i];
            if (data[i][i] != 0) {
                data[j] = data[i][i] * data[j] - tmp * data[i];
            }
        }
    }
    //return;
    // eliminate the upper triangle
    for (int i = data.size() - 1; i >= 0; i --) {
        mod(data, p);
        if (data[i].sum() == 0) {
            continue;
        } else if (data[i].sum() == data[i][data.size()]) {
            throw 42;
        }
        print(data);
        int divisor = data[i][i];
        if (divisor == 0) {
            throw 42;
        }
        for (int j = 0; j < data.size() + 1; j ++) {
            while (data[i][j] % divisor != 0) {
                data[i][j] += p;
            }
        }
        //cout << "dividing by " << data[i][i] << endl;
        data[i] /= ((int) data[i][i]);
        //cout << "dividing by " << data[i][i] << endl;
        print(data);
        for (int j = i - 1; j >= 0; j --) {
            int tmp = data[j][i];
            data[j] = data[j] - tmp * data[i];
        }
        
        
    }
    mod(data, p);
    print(data);
}


int main() {
    int n, m, p;
    cin >> m >> n >> p;

    vector<valarray<int>> data(n * m, valarray<int>(n * m + 1));
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < m; j ++) {
            int x;
            cin >> x;
            data[i * m + j][n * m] = -x;
        }
    }
    for (int i = 0; i < m; i ++) {
        for (int j = 0; j < n; j ++) {
            for (int k = 0; k < n; k ++) {
                data[i * n + j][i * n + k] = 1;
            }
            for (int k = 0; k < m; k ++) {
                data[i * n + j][k * n + j] = 1;
            }
        }
    }
    
    try { solve(data, p); } catch (...) { cout << -1 << endl; exit(0); }
    
    vector<int> ans;
    for (int i = 0; i < n * m; i ++) {
        for (int j = 0; j < data[i][n * m]; j ++) {
            ans.push_back(i + 1);
        }
    }
    
    cout << ans.size() << endl;
    if (ans.size() == 0) {
        exit(0);
    }
    cout << ans[0];
    for (int j = 1; j < ans.size(); j ++) {
        int i = ans[j];
        cout << " " << i;
    }
    cout << endl;
}