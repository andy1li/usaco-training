/*
ID:   andy1li
PROG: ride
LANG: C++         
*/

#include <bits/stdc++.h>
using namespace std;

#define foreach(x, xs) for (auto x=xs.begin(); x!=xs.end(); x++)

/*----------------------------------------------------------------------------*/

int get_hash(const string &name) {
    int hash = 1;
    foreach (x, name) {
        hash *= (*x - 'A' + 1);
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