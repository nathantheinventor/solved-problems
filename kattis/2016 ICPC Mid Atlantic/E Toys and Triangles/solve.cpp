#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;

struct Vector {
    double x, y;
    Vector(double theta, double r) {
        x = r * cos(theta);
        y = r * sin(theta);
    }
};

struct Point {
    double x, y;
    Point operator+(Vector v) {
        return {x + v.x, y + v.y};
    }
};

vector<int> range(int n) {
    vector<int> ans;
    for (int i = 0; i < n; i ++) {
        ans.push_back(i);
    }
    return ans;
}

double square(double x) {
    return x * x;
}

double dist(Point A, Point B) {
    return sqrt(square(A.x - B.x) + square(A.y - B.y));
}

double pi = 3.14159265358979323846264338327950288419716;

double EPS = 1e-8;

vector<Point> findEF(Point A, Point B, double x, double y) {
    double z = dist(A, B);
    double s = (x + y + z) / 2.0;
    double Area = sqrt(s * (s - x) * (s - y) * (s - z));
    double h = 2.0 * Area / z;
    double z2 = sqrt(square(x) - square(h));
    vector<Point> ans;
    double ABAngle = atan2(B.y - A.y, B.x - A.x);
    Point GH1 = A + Vector(ABAngle, z2);
    Point GH2 = A + Vector(ABAngle, -z2);
    Point EF1 = GH1 + Vector(ABAngle + pi / 2.0, h);
    Point EF2 = GH1 + Vector(ABAngle + pi / 2.0, -h);
    Point EF3 = GH2 + Vector(ABAngle + pi / 2.0, h);
    Point EF4 = GH2 + Vector(ABAngle + pi / 2.0, -h);
    if (abs(dist(B, EF1) - y) < EPS) { ans.push_back(EF1); }
    if (abs(dist(B, EF2) - y) < EPS) { ans.push_back(EF2); }
    if (abs(dist(B, EF3) - y) < EPS) { ans.push_back(EF3); }
    if (abs(dist(B, EF4) - y) < EPS) { ans.push_back(EF4); }
    GH1 = B + Vector(ABAngle, z2);
    GH2 = B + Vector(ABAngle, -z2);
    EF1 = GH1 + Vector(ABAngle + pi / 2.0, h);
    EF2 = GH1 + Vector(ABAngle + pi / 2.0, -h);
    EF3 = GH2 + Vector(ABAngle + pi / 2.0, h);
    EF4 = GH2 + Vector(ABAngle + pi / 2.0, -h);
    if (abs(dist(A, EF1) - y) < EPS) { ans.push_back(EF1); }
    if (abs(dist(A, EF2) - y) < EPS) { ans.push_back(EF2); }
    if (abs(dist(A, EF3) - y) < EPS) { ans.push_back(EF3); }
    if (abs(dist(A, EF4) - y) < EPS) { ans.push_back(EF4); }
    // cerr << x << " " << y << " " << dist(B, EF2) << " " << dist(A, EF2) << endl;
    // cerr << ans.size() << endl;
    return ans;
}

struct Shape {
    vector<Point> points;
    vector<pii> lines;
    vector<int> unused;
    Shape(int x, vector<int> _unused) {
        unused = _unused;
        points.push_back({0,0});
        points.push_back({(double) x,0});
        lines.push_back({0, 1});
    }
    Shape(Shape* base, Point newPoint, pii baseline, vector<int> _unused) {
        points = base->points;
        int x = points.size();
        points.push_back(newPoint);
        int y = baseline.first;
        int z = baseline.second;
        lines = base->lines;
        lines.push_back({x, y});
        lines.push_back({x, z});
        unused = _unused;
    }
    double solve() {
        double ans = points[0].y;
        for (Point p: points) {
            ans = max(ans, p.y);
        }
        // cerr << lines.size() << " " << unused.size() << endl;
        int n = unused.size();
        int m = lines.size();
        vector<pii> lines2;
        if (m == 1) {
            lines2 = lines;
        } else {
            lines2.push_back(lines[m - 1]);
            lines2.push_back(lines[m - 2]);
        }
        for (pii baseline: lines2) {
            Point A = points[baseline.first];
            Point B = points[baseline.second];
            for (int i = 0; i < n; i ++) {
                int x = unused[i];
                for (int j = i + 1; j < n; j ++) {
                    int y = unused[j];
                    vector<Point> EFs = findEF(A, B, x, y);
                    vector<int> newUnused;
                    for (int k = 0; k < unused.size(); k ++) {
                        if (k != i and k != j) {
                            newUnused.push_back(unused[k]);
                        }
                    }
                    for (Point EF: EFs) {
                        if (EF.y >= 0) {
                            Shape s(this, EF, baseline, newUnused);
                            ans = max(ans, s.solve());
                        }
                    }
                }
            }
        }
        return ans;
    }
};

int main() {
    int n, x;
    while (cin >> n) {
        vector<int> points;
        while (n --) {
            cin >> x;
            points.push_back(x);
        }
        n = points.size();
        double ans = 0;
        for (int i: range(n)) {
            int x = points[i];
            vector<int> excl;
            for (int j = 0; j < n; j ++) {
                if (j != i) {
                    excl.push_back(points[j]);
                }
            }
            ans = max(ans, Shape(x, excl).solve());
        }
        printf("%.2f\n", ans);
    }
}
