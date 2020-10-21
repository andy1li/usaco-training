/*
ID:   andy1li
LANG: C++
TASK: friday
*/

#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;

#define range(stop) for (size_t i=0; i<stop; ++i)
#define rep(i, start, stop) for (size_t i=start; i<stop; ++i)

/*----------------------------------------------------------------------------*/

int is_leap(int year) {
    return year%4==0 && (year%100 != 0 || year%400 == 0);
}

int days_in_month(int year, int month) {
    vi days = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
    return days[month] + (month == 1 && is_leap(year));
}

void solve() {
    int n; cin >> n;

    vi count(7, 0);
    int day_of_week = 0; // day of week: January 13, 1900 was a Saturday = 0

    rep(year, 1900, 1900+n) {
        rep(month, 0, 12) {
            count[day_of_week]++;
            day_of_week += days_in_month(year, month)
            day_of_week %= 7
        }
    }

    range(7) { 
        cout << count[i] << ((i < 6) ? ' ' : '\n'); 
    }
}

/*----------------------------------------------------------------------------*/

int main() {
    freopen("friday.in",  "r", stdin);
    freopen("friday.out", "w", stdout);
    solve();
}