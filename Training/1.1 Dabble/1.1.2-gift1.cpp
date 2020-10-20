/*
ID:   andy1li
LANG: C++ 
TASK: gift1
*/

#include <bits/stdc++.h>
using namespace std;

#define range(stop) for (size_t i=0; i<stop; ++i)

/*----------------------------------------------------------------------------*/

void solve() {
    int n; cin >> n;

    vector<string> names(n);
    map<string, int> balance;
    range(n) {
        string name; cin >> name;
        names[i] = name;
        balance[name] = 0;
    }

    range(n) {
        string giver; cin >> giver;
        int amount, numReceivers; cin >> amount >> numReceivers;

        range(numReceivers) {
            string receiver; cin >> receiver;
            balance[giver]    -= amount / numReceivers;
            balance[receiver] += amount / numReceivers;
        }
    }
    
    for (string name: names) {
        cout << name << ' ' << balance[name] << endl;
    }
}

/*----------------------------------------------------------------------------*/

int main() {
    freopen("gift1.in",  "r", stdin);
    freopen("gift1.out", "w", stdout);
    solve();
}