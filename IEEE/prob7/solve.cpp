#include <iostream>
#include <set>

using namespace std;

int main() {
    set<int> notFound;
    for (int i = -100006; i < 200005; i ++) {
        notFound.insert(i);
    }
    set<int> found;
    int n; cin >> n;
    long ans = 0;
    while (n --) {
        int x; cin >> x;
        auto next = notFound.upper_bound(x);
        auto prev = next; prev --;
        int ne = *next;
        int p = *prev;
        if ((ne - x) < (x - p)) {
            found.insert(ne);
            notFound.erase(ne);
            ans += ne - x;
        } else {
            found.insert(p);
            notFound.erase(p);
            ans += x - p;
        }
    }
    cout << ans << endl;
    return 0;
}
