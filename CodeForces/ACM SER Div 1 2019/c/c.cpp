#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

#define N 400004

map<int, set<int>> factors;
map<int, long long> counts;
map<int, set<int>> factor_sets;

void make_factors(set<int> nums) {
    for (int f: nums) {
        for (int x = f; x < N; x += f) {
            factors[x].insert(f);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    vector<int> piles;
    vector<int> fs;
    set<int> fs2;
    int n, m;
    cin >> n >> m;
    while (n --) {
        int x; cin >> x;
        piles.push_back(x);
    }
    while (m --) {
        int x; cin >> x;
        fs.push_back(x);
        fs2.insert(x);
    }

    make_factors(fs2);
    
    for (int x: piles) {
        counts[x] ++;
        for (int f: factors[x]) {
            factor_sets[f].insert(x);
        }
    }

    long long ans = 0;
    for (int x: fs) {
        set<int> mults = factor_sets[x];
        for (int mult: mults) {
            // 1. Move the counts
            counts[mult + 1] += counts[mult];
            ans += counts[mult];
            counts[mult] = 0;

            // 2. Remove from factor_sets
            for (int f: factors[mult]) {
                factor_sets[f].erase(mult);
            }

            // 3. Insert new into factor_sets
            for (int f: factors[mult + 1]) {
                factor_sets[f].insert(mult + 1);
            }
        }
    }

    cout << ans << endl;
}
