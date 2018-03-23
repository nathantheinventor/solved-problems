#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int caseNum = 1;
class Angle {
public:
    ll x, y;
    Angle(ll _x, ll _y) {
        ll g = __gcd(_x, _y);
        g = abs(g);
        // if (_y == 0 and _x < 0) {
            // x = -1;
        // } else {
            x = _x / g;
        // }
        y = _y / g;
    }
    bool operator==(Angle other) {
        return x == other.x and y == other.y;
    }
    bool isInf() {
        return x > 0 and y == 0;
    }
    bool isNegInf() {
        return x < 0 and y == 0;
    }
    bool operator<(Angle other) {
        return x * other.y < other.x * y;
    }
};

class point {
public:
    ll x, y, height;
    Angle angle;
    point(ll _x, ll _y, ll _height) : x(_x), y(_y), height(_height), angle(_x, _y) {
        
    }
    
    ll abs() {
        return x * x + y * y;
    }
    
    const bool operator<(point other) {
        
        if (angle == other.angle) {
            return abs() < other.abs();
        }
        if (angle.isInf() or other.angle.isNegInf()) {
            return false;
        } else if (angle.isNegInf() or other.angle.isInf()) {
            return true;
        }
        return angle < other.angle;
    }
};

int main() {
    int n;
    cin >> n;
    while (n > 0) {
        vector<point> poles;
        for (int i = 0; i < n; i ++) {
            int x, y, z;
            cin >> x >> y >> z;
            poles.push_back(point(x, y, z));
        }
        
        sort(poles.begin(), poles.end());
        // if (caseNum == 91) {
        //     for (point pole: poles)
        //     cout << pole.x << " " << pole.y << " " << pole.height << endl;
        // }
        
        point last = poles[0];
        
        ll maxH = last.height;
        
        vector<pair<int, int>> ans;
        
        bool first = true;
        for (point pole: poles) {
            if (first) {
                first = false;
                continue;
            }
            if (pole.angle == last.angle) {
                // same angle as the last pole; potential for overlap
                if (pole.height <= maxH) {
                    ans.push_back({pole.x, pole.y});
                } else {
                    maxH = pole.height;
                }
            } else {
                maxH = pole.height;
            }
            last = pole;
        }
        cout << "Data set " << caseNum ++ << ":" << endl;
        if (ans.size() == 0) {
            cout << "All the lights are visible." << endl;
        } else {
            cout << "Some lights are not visible:" << endl;
            sort(ans.begin(), ans.end());
            for (auto p: ans) {
                if (p == ans[ans.size() - 1]) {
                    cout << "x = " << p.first << ", y = " << p.second << "." << endl;
                } else {
                    cout << "x = " << p.first << ", y = " << p.second << ";" << endl;
                }
            }
        }
        
        cin >> n;
    }
}
