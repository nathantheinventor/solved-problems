#include "bits/stdc++.h"

using namespace std;

typedef long long ll;

ll ms[10005];

struct Range {
    ll begin, end;
    bool operator<(Range other) const {
        if (begin == other.begin) {
            return end > other.end;
        }
        return begin < other.begin;
    }
};

int main() {
    ios::sync_with_stdio(false);
    ll n, k, t1, t2;
    cin >> n >> k >> t1 >> t2;
    t2 -= t1;
    for (int i = 0; i < n; i ++) {
        cin >> ms[i]; 
    }
    valarray<ll> bs(k);
    valarray<ll> es(k);
    for (int i = 0; i < k; i ++) {
        cin >> bs[i] >> es[i];
    }
    bs -= t1;
    es -= t1;
    //cout << bs[0] << endl;


    vector<Range> ranges;
    ranges.reserve(n * k + 5);
    for (int i = 0; i < n; i++) {
        valarray<ll> tmp1 = bs - ms[i];
        valarray<ll> tmp2 = es - ms[i];
        for (int j = 0; j < k; j ++) {
            //cout << i << " " << j << " " << bs[i] << " " << tmp2[j] << endl;
            ranges.push_back(Range({tmp1[j], tmp2[j]}));
        }
    }
    sort(ranges.begin(), ranges.end());

    ll end = 0;
    ll area = 0;
    for(int i = 0; i < ranges.size(); i++) {
        if (ranges[i].begin >= t2) {
            break;
        }
        //cout << ranges[i].begin << " " << ranges[i].end << endl;
        if(ranges[i].begin > end) {
            area += ranges[i].begin - end;
            end = ranges[i].end;
        } else if(ranges[i].end > end) {
            end = ranges[i].end;
        }
    }
    if(end < t2) { area += t2 - end; }
    cout << fixed << setprecision(10) << (double) area / (double) t2 << endl;    
}