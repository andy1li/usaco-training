/*
ID:   andy1li
LANG: C++         
TASK: ride
*/

#include <bits/stdc++.h>
using namespace std;

/*----------------------------------------------------------------------------*/

int get_hash(string& name) {
    int hash = 1;
    for (auto x: name) {
        hash *= (x - 'A' + 1);
        hash %= 47;
    }
    return hash;
}

/*----------------------------------------------------------------------------*/

int main() {
    freopen("ride.in",  "r", stdin);
    freopen("ride.out", "w", stdout);

    string comet, group;
    cin >> comet >> group;

    string ans = (get_hash(comet) == get_hash(group)) ? "GO" : "STAY";
    cout << ans << endl;
}