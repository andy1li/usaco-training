/*
ID:   andy1li
LANG: C++14
TASK: ariprog 
*/

#include <bits/stdc++.h>
using namespace std;

#define rep(i, j, k) for (int i=j; i<=k; ++i)
#define per(i, j, k) for (int i=j; i>=k; --i)
#define all(c) begin(c), end(c)
#define len(c) c.size()
#define each(x, c) for (auto& x: c)
#define print(x) cout << x << endl;
#define prints(c) each(x, c) cout << x << ' '; cout << endl
#define pb push_back
using vi = vector<int>;

/*----------------------------------------------------------------------------*/

int N, M; 
const int maxN = 2 * 251*251;
bool check[maxN] = {false};

bool bsq_check(int a, int b) {
    rep(i, 0, N-2) {
        if (!check[a + b*i]) return false;
    }
    return true;
}

void solve() {
    cin >> N >> M;

    rep(p, 0, M) rep(q, 0, M) {
        check[p*p + q*q] = true;
    }
    vi bsq; per(i, maxN-1, 0) {
        if (check[i]) bsq.pb(i);
    }
    int n = len(bsq);

    vector<pair<int, int>> ans;
    rep(i, 0, n-3) rep(j, i+1, n-2) {
        int last = bsq[i], pen = bsq[j],
            step = last - pen,
            first = last - step * (N-1);
        if (first < 0) break;
        if (bsq_check(first, step)) 
            ans.pb( {step, first} );
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