#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int n, m;

struct Flight {
    int from, to, start, end;
    const bool operator<(const Flight other) const {
        return start < other.start;
    }
};
struct Flight2 {
    int to, end;
    const bool operator<(const Flight2 other) const {
        return end > other.end;
    }
};
struct State {
    ll frustration;
    int leaving, relative;
    const bool operator<(const State other) const {
        return frustration < other.frustration;
    }
};

vector<set<Flight>> flights2(200001);
vector<vector<Flight>> flights(200001);
vector<map<int, ll>> dp(200001);
set<Flight2> flightEnds;
int firstFlightSeen[200001];
vector<set<State>> seen(200001);

// arriving at location l at time t, what is the minimum frustration I can expect going forward?
ll solve(int time, int location) {
    if (dp[location][time] != 0) {
        return dp[location][time];
    }
    if (location == n) {
        return 0;
    }
    Flight tmp1 = {1,1,time,0};
    auto tmp = upper_bound(flights[location].begin(), flights[location].end(), tmp1);
    int i = 0;
    int newFirstFlight = firstFlightSeen[location];
    while (tmp != flights[location].end() and (*tmp).start < firstFlightSeen[location]) {
        Flight tmp2 = *tmp;
        newFirstFlight = min(newFirstFlight, tmp2.start);
        ll newFrust = tmp2.start - time;
        newFrust *= newFrust;
        State s = {newFrust + solve(tmp2.end, tmp2.to), tmp2.start, time};
        seen[location].insert(s);
        tmp ++;
    }
    firstFlightSeen[location] = newFirstFlight;
    if (seen[location].empty()) {
        dp[location][time] = 1e13;
        return 1e13;
    }
    while ((*(seen[location].begin())).relative != time) {
        State s = *(seen[location].begin());
        // cerr << s.relative << endl;
        seen[location].erase(seen[location].begin());
        ll frust1 = s.leaving - s.relative;
        ll frust2 = s.leaving - time;
        frust1 *= frust1;
        frust2 *= frust2;
        s.frustration -= frust1;
        s.frustration += frust2;
        s.relative = time;
        seen[location].insert(s);
    }
    ll ans = (*(seen[location].begin())).frustration;
    dp[location][time] = ans;
    return ans;
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i ++) {
        int from, to, start, end;
        cin >> from >> to >> start >> end;
        flights2[from].insert({from, to, start, end});
        flightEnds.insert({to, end});
    }
    for (int i = 0; i < 200001; i ++) {
        firstFlightSeen[i] = 2000001;
        for (Flight f: flights2[i]) {
            flights[i].push_back(f);
        }
    }
    for (Flight2 f: flightEnds) {
        solve(f.end, f.to);
        // cerr << f.to << " " << f.end << " " << solve(f.end, f.to) << endl;;
    }
    cout << solve(0, 1) << endl;
}
