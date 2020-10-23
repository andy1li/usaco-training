/*
ID:   andy1li
LANG: C++
TASK: beads 
*/

#include <bits/stdc++.h>
using namespace std;

#define all(xs) xs.begin(), xs.end()
#define FOR(stop) for (size_t i=0; i<stop; ++i)

/*----------------------------------------------------------------------------*/

int collect(string s, char color = 'w') {
    FOR(s.size()) {
        char x = s[i];
        if (x == 'w') continue;
        if (color == 'w') color = x;
        else if (x != color) return i;
    }
    return s.size();
}

void solve() {
    int n; cin >> n;
    string beads; cin >> beads;

    int ans = 0;
    FOR(n) {
        string rbeads = beads; reverse(all(rbeads));
        ans = max(ans, collect(beads) + collect(rbeads));

        rotate(begin(beads), begin(beads)+1, end(beads));
    }
    cout << min(n, ans) << endl;
}

/*----------------------------------------------------------------------------*/

int main() {
    freopen("beads.in",  "r", stdin);
    freopen("beads.out", "w", stdout);
    solve();
}