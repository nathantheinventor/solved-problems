#include "bits/stdc++.h"

using namespace std;

typedef long double ld;

ld pi = 3.14159265358979323846264338327950288419716;

struct angle {
    ld _x, _y;
    angle(ld x, ld y) {
        _y = y;
        _x = x;
    }
    
    bool operator<(angle other) const {
        ld result = _y * other._x - _x * other._y;
        return result > 0.0;
    }
    
    bool operator<=(angle other) {
        ld result = _y * other._x - _x * other._y;
        return result >= 0.0;
    }
    
    bool operator>(angle other) {
        ld result = _y * other._x - _x * other._y;
        return result < 0.0;
    }
    
    bool operator>=(angle other) {
        ld result = _y * other._x - _x * other._y;
        return result <= 0.0;
    }
    
    ld phi() {
        return atan2(_x, _y);
    }
    
    angle operator+(ld d) {
        return angle(-_y, -_x);
    }
    
    angle operator-(ld d) {
        return angle(-_y, -_x);
    }
};

struct complex2 {
    ld _real, _imag;
    complex2(ld real, ld imag) {
        _real = real;
        _imag = imag;
    }
    
    ld abs() {
        return sqrt(_real * _real + _imag * _imag);
    }
    
    angle phase() {
        return angle(_imag, _real);
    }
    
    complex2 operator-(complex2 other) {
        return complex2(_real - other._real, _imag - other._imag);
    }
};

complex2 zero(0.0, 0.0);

ld triArea(ld a, ld b, ld c) {
    /* Calculate the area of a triangle given the length of its sides */
    ld s = (a + b + c) / 2.0;
    return sqrt(s * (s - a) * (s - b) * (s - c));
}

struct point {
    angle phi;
    ld r;
    complex2 p;
    bool operator<(point other) const {
        return phi < other.phi;
    }
};

bool compareByCoord(complex2 a, complex2 b) {
    if (a._real == b._real) {
        return a._imag < b._imag;
    }
    return a._real < b._real;
}

vector<point> convexHull(vector<complex2>& points, complex2& pivot) {
    /* input: list of complex2 objects, representing points
        output: tuple with
            list of tuples of angle, length, and complex2 objects of points on the convex hull
            pivot complex2 object */
            
    // sort the points by y-value then x-value
    sort(points.begin(), points.end(), compareByCoord);
    pivot = points[0];
    
    vector<point> newPoints;
    // make each point relative to the pivot
    for (int i = 0; i < points.size(); i ++) {
        points[i] = points[i] - pivot;
        if (i > 0) {
            newPoints.push_back({points[i].phase(), points[i].abs(), points[i]});
        }
    }
    
    // sort by angle
    sort(newPoints.begin(), newPoints.end());
    
    vector<point> ch;
    ch.push_back({angle(0, 0), 0.0, complex2(0, 0)});
    ch.push_back(newPoints[0]);
    
    int index = 1;
    while (index < newPoints.size()) {
        point p1 = newPoints[index];
        point p2 = ch[ch.size() - 1];
        point p3 = ch[ch.size() - 2];
        
        // area of the triangle defined by p1 and p3
        ld areaBig = triArea(p1.r, p3.r, (p1.p - p3.p).abs());
        // area of the triangle defined by p1 and p2
        ld area1 = triArea(p1.r, p2.r, (p1.p - p2.p).abs());
        // area of the triangle defined by p2 and p3
        ld area2 = triArea(p2.r, p3.r, (p2.p - p3.p).abs());
        
        if (area1 + area2 < areaBig) {
            ch.pop_back();
        } else {
            ch.push_back(p1);
            index ++;
        }
    }
    
    return ch;
}

vector<ld> buildAreas (vector<point>& ch) {
    /* Build a list of the cumulative areas of the triangles composing the main polygon */
    vector<ld> areas;
    
    ld sum = 0.0;
    for (int i = 1; i < ch.size() - 1; i ++) {
        sum += triArea(ch[i].r, ch[i + 1].r, (ch[i].p - ch[i + 1].p).abs());
        areas.push_back(sum);
    }
    
    return areas;
}

bool inside (vector<point>& ch, complex2& p, int& lo, int& hi) {
    angle phi = p.phase();
    ld r = p.abs();
    
    // if the angle isn't within the polygon
    if (phi <= ch[1].phi or phi >= ch[ch.size() - 1].phi) {
        lo = -1;
        hi = -1;
        return false;
    }
    
    // find which points the angle is between
    lo = 0;
    hi = ch.size();
    while (hi - lo > 1) {
        int mid = (hi + lo) / 2;
        if (phi < ch[mid].phi) {
            hi = mid;
        } else {
            lo = mid;
        }
    }
    
    // cout << "lohi " << lo << " " << hi << " " << phi.phi() << endl;
    
    complex2 p1 = ch[lo].p;
    complex2 p2 = ch[hi].p;
    
    ld r1 = ch[lo].r;
    ld r2 = ch[hi].r;
    
    ld areaBig = triArea(r1, r2, (p1 - p2).abs());
    ld area1   = triArea(r1, r, (p1 - p).abs());
    ld area2   = triArea(r, r2, (p - p2).abs());
    
    // cout << areaBig << " " << area1 << " " << area2 << endl;
    
    if (area1 + area2 < areaBig) {
        return true;
    }
    return false;
}

int searchMin (int lo, int hi, vector<point>& ch, complex2& p) {
    /* Find the index of the point in `ch` in the indexes between `lo` and `hi`
        that yields the smallest angle from `p` */
    
    int m1 = lo + (hi - lo) / 3;
    int m2 = lo + 2 * (hi - lo) / 3;
    
    angle phi1 = (ch[lo].p - p).phase();
    angle phi2 = (ch[m1].p - p).phase();
    angle phi3 = (ch[m2].p - p).phase();
    angle phi4 = (ch[hi].p - p).phase();
    
    while (hi - lo > 2) {
        if (phi2 <= phi1 and phi3 <= phi2) {
            lo = m1;
        }
        if (phi2 <= phi3 and phi3 <= phi4) {
            hi = m2;
        }
        
        m1 = lo + (hi - lo) / 3;
        m2 = lo + 2 * (hi - lo) / 3;
        
        phi1 = (ch[lo].p - p).phase();
        phi2 = (ch[m1].p - p).phase();
        phi3 = (ch[m2].p - p).phase();
        phi4 = (ch[hi].p - p).phase();
    }
    
    if (phi1 < phi3) {
        return lo;
    } else if (phi3 < phi4) {
        return m2;
    }
    return hi;
}

int searchMax (int lo, int hi, vector<point>& ch, complex2& p) {
    /* Find the index of the point in `ch` in the indexes between `lo` and `hi`
        that yields the largest angle from `p` */
    
    int m1 = lo + (hi - lo) / 3;
    int m2 = lo + 2 * (hi - lo) / 3;
    
    angle phi1 = (ch[lo].p - p).phase();
    angle phi2 = (ch[m1].p - p).phase();
    angle phi3 = (ch[m2].p - p).phase();
    angle phi4 = (ch[hi].p - p).phase();
    
    while (hi - lo > 2) {
        if (phi2 >= phi1 and phi3 >= phi2) {
            lo = m1;
        }
        if (phi2 >= phi3 and phi3 >= phi4) {
            hi = m2;
        }
        
        m1 = lo + (hi - lo) / 3;
        m2 = lo + 2 * (hi - lo) / 3;
        
        phi1 = (ch[lo].p - p).phase();
        phi2 = (ch[m1].p - p).phase();
        phi3 = (ch[m2].p - p).phase();
        phi4 = (ch[hi].p - p).phase();
    }
    
    if (phi1 > phi3) {
        return lo;
    } else if (phi3 > phi4) {
        return m2;
    }
    return hi;
}

ld findAreaBelow (complex2& p, vector<point>& ch, vector<ld>& dp) {
    /* point is below the polygon, so find the area looking upward */
    angle phi = (zero - p).phase();
    
    int lo = 0, hi = ch.size();
    while (hi - lo > 1) {
        int mid = (hi + lo) / 2;
        if (phi < ch[mid].phi) {
            hi = mid;
        } else {
            lo = mid;
        }
    }
    
    int leftSide = searchMin(0, lo, ch, p);
    int rightSide = 0;
    if (phi < ch[ch.size() - 1].phi) {
        rightSide = searchMax(hi, ch.size() - 1, ch, p);
    }
    
    // The area of the orig that's going away
    ld area1 = (leftSide >= 2) ? dp[leftSide - 2] : 0;
    // The area of the orig that's staying
    ld area2 = rightSide >= 2 ? dp[rightSide - 2] : ((rightSide == 0) ? dp[dp.size() - 1] : 0);
    // Area of the left triangle
    ld area3 = triArea(p.abs(), (p - ch[leftSide].p).abs(), ch[leftSide].r);
    // Area of the right triangle
    ld area4 = triArea(p.abs(), (p - ch[rightSide].p).abs(), ch[rightSide].r);
    
    return area2 + area3 + area4 - area1;
}

ld findAreaAbove (complex2& p, vector<point>& ch, vector<ld>& dp, int lo, int hi) {
    /* point is above the polygon, so find the area looking upward from the inverted reference frame */
    int leftSide = searchMin(hi, ch.size() - 1, ch, p);
    int rightSide = searchMax(1, lo, ch, p);
    
    // The area of the orig that's staying
    ld area1 = (rightSide >= 2) ? dp[rightSide - 2] : 0;
    // The area of the orig that's going
    ld area2 = dp[leftSide - 2];
    // Area of the left triangle
    ld area3 = triArea(p.abs(), (p - ch[leftSide].p).abs(), ch[leftSide].r);
    // Area of the right triangle
    ld area4 = triArea(p.abs(), (p - ch[rightSide].p).abs(), ch[rightSide].r);
    // cout << dp[dp.size() - 1] << " " << area1 << " " << area2 << " " << area3 << " " << area4 << endl;
    return dp[dp.size() - 1] - area2 + area3 + area4 + area1;
}

int main() {
    int n, k;
    while (cin >> n >> k) {
        vector<complex2> ownedPoints;
        for (int i = 0; i < k; i ++) {
            int x, y;
            cin >> x >> y;
            ownedPoints.push_back(complex2(x, y));
        }
        
        complex2 pivot(0, 0);
        vector<point> ch = convexHull(ownedPoints, pivot);
        
        // for (point p: ch) {
        //     cout << p.p._real << " " << p.p._imag << endl;
        // }
        
        vector<ld> dp = buildAreas(ch);
        
        ld maxArea = dp[dp.size() - 1];
        
        vector<point> negCh;
        for (point p: ch) {
            negCh.push_back({p.phi - pi, p.r, zero - p.p});
        }
        
        for (int i = k; i < n; i ++) {
            int x, y;
            cin >> x >> y;
            complex2 p(x, y);
            p = p - pivot;
            int lo, hi;
            // cout << "orig " << x << " " << y << endl;
            // cout << "new " << p._real << " " << p._imag << endl;
            if (!inside(ch, p, lo, hi)) {
                // cout << "made it" << endl;
                ld area;
                if (lo == -1) {
                    area = findAreaBelow(p, ch, dp);
                } else {
                    p = zero - p;
                    area = findAreaAbove(p, negCh, dp, lo, hi);
                }
                // cout << area << endl;
                maxArea = max(maxArea, area);
            }
        }
        printf("%.1Lf\n", maxArea);
    }
}