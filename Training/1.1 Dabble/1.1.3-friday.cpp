/*
ID:   andy1li
PROG: friday
LANG: C++11
*/

#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int isLeap(int year) {
    return year%4==0 && (year%100 != 0 || year%400 == 0);
}

int daysInMonth(int year, int month) {
    switch (month) {
        case 2:                          return 28 + isLeap(year);
        case 4: case 6: case 9: case 11: return 30;
        default:                         return 31;
    }
}

int main() {
    ifstream fin  ("friday.in");
    ofstream fout ("friday.out");

    int n; fin >> n;

    vector<int> thirteenths(7, 0);
    int dayOfWeek  = 0; // day of week: January 13, 1900 was a Saturday = 0

    for (int year = 1900; year < 1900+n; year++) {
        for (int month = 1; month < 13; month++) {
            thirteenths[dayOfWeek]++;
            dayOfWeek = (dayOfWeek + daysInMonth(year, month)) % 7;
        }
    }

    for (int i = 0; i < thirteenths.size(); i++) {
        if (i < thirteenths.size() - 1) 
            fout << thirteenths[i] << ' ';
        else                            
            fout << thirteenths[i] << endl;
    }

    return 0;
}