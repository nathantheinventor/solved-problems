#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    while (n > 0) {
        int a, b;
        cin >> a >> b;
        while (n--) {
            int x, y;
            cin >> x >> y;
            if (x > a and y > b) {
                cout << "NE" << endl;
            } else if (x > a and y < b) {
                cout << "SE" << endl;
            } else if (x < a and y > b) {
                cout << "NO" << endl;
            } else if (x < a and y < b) {
                cout << "SO" << endl;
            } else {
                cout << "divisa" << endl;
            }
        }
        cin >> n;
    }
}