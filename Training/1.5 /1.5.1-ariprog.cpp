/*
ID:   andy1li
LANG: C++14
TASK: ariprog 
*/

#include <bits/stdc++.h>
using namespace std;

#define rep(i, j, k) for (size_t i=j; i<=k; ++i)
#define all(c) begin(c), end(c)
#define len(c) c.size()
#define each(x, c) for (auto& x: c)
#define pb push_back

/*----------------------------------------------------------------------------*/

int N, M;
bool bsq[2 * 251*251];

bool check(int a, int b) {
    rep(i, 0, N-1) {
        if (!bsq[a + b*i]) return false;
    }
    return true;
}

void solve() {
    cin >> N >> M;
    const int stop = 2 * M*M;

    rep(p, 0, M) rep(q, 0, M) {
        bsq[p*p + q*q] = true;
    }

    vector<pair<int, int>> ans;
    rep(a, 0, stop) {
        if (!bsq[a]) continue;
        rep(b, 1, (stop-a)/(N-1)) {
            if (check(a, b)) ans.pb({b, a});
        }
    }
    sort(all(ans));

    if (len(ans)) {
        each(pair, ans) cout << pair.second << ' ' << pair.first << endl;
    } else {
        cout << "NONE" << endl;
    } 
}

/*----------------------------------------------------------------------------*/

int main() {
    freopen("ariprog.in",  "r", stdin);
    freopen("ariprog.out", "w", stdout);
    solve();
}