#include <bits/stdc++.h>

using namespace std;

struct point{
    double x, y;
    point(double _x, double _y) : x(_x), y(_y) {}
};

struct vec {
    double x, y; // name: ‘vec’ is different from STL vector
    vec(double _x, double _y) : x(_x), y(_y) {}
};

vec toVec(point a, point b) { // convert 2 points to vector a->b
    return vec(b.x - a.x, b.y - a.y);
}

vec scale(vec v, double s) { // nonnegative s = [<1 .. 1 .. >1]
    return vec(v.x * s, v.y * s); // shorter.same.longer
}

point translate(point p, vec v) { // translate p according to v
    return point(p.x + v.x , p.y + v.y);
}

double dist(point p1, point p2) { // Euclidean distance
    // hypot(dx, dy) returns sqrt(dx * dx + dy * dy)
    return hypot(p1.x - p2.x, p1.y - p2.y); // return double  
}

double dot(vec a, vec b) { return (a.x * b.x + a.y * b.y); }
double norm_sq(vec v) { return v.x * v.x + v.y * v.y; }

// returns the distance from p to the line defined by
// two points a and b (a and b must be different)
// the closest point is stored in the 4th parameter (byref)
double distToLine(point p, point a, point b, point &c) {
    // formula: c = a + u * ab
    vec ap = toVec(a, p), ab = toVec(a, b);
    double u = dot(ap, ab) / norm_sq(ab);
    c = translate(a, scale(ab, u)); // translate a to c
    return dist(p, c); // Euclidean distance between p and c
}

int main() {
    double x, y;
    while (cin >> x >> y) {
        point m({x, y});
        int n;
        cin >> n;
        vector<point> points;
        
        for (int i = 0; i <= n; i ++) {
            cin >> x >> y;
            points.push_back({x,y});
        }
        double dist = 10000000000.0;
        point ans(0,0);
        for (int i = 0; i <= n; i ++) {
            point p = points[i];
            point p2 = points[(i + 1) % (n + 1)];
            point c(0,0);
            double tmp = distToLine(m, p, p2, c);
            // cout << "(" << p.x << " " << p.y << "), (" << p2.x << " " << p2.y << "), (" << c.x << " " << c.y << endl;
            if (tmp < dist) {
                dist = tmp;
                ans = c;
            }
        }
        cout << setprecision(4) << fixed << ans.x << endl << ans.y << endl;
    }
}