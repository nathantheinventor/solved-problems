#include <iostream>

using namespace std;

int main() {
    int height, day, night, fatigue;
    cin >> height >> day >> night >> fatigue;
    while (height > 0) {
        int day2 = day;
        height *= 100;
        day    *= 100;
        night  *= 100;
        int start = 0, climed = day, dayResult = day, nightResult = day - night, days = 1;
        bool succeeded = nightResult >= 0;
        while (dayResult <= height and nightResult >= 0) {
            //cout << "Day " << days << "\t" << start << "\t" << climed << "\t" << dayResult << "\t" << nightResult << endl;
            start = nightResult;
            climed -= day2 * fatigue;
            if (climed < 0) {
                climed = 0;
            }
            dayResult = start + climed;
            nightResult = dayResult - night;
            days ++;
            if (nightResult < 0) {
                succeeded = false;
                break;
            }
        }
        
        if (succeeded) {
            cout << "success on day " << days << endl;
        } else {
            cout << "failure on day " << days << endl;
        }
        
        cin >> height >> day >> night >> fatigue;
    }
}