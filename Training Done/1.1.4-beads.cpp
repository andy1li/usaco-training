/*
ID:   andy1li
PROG: beads
LANG: C++11
*/

#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int longest(string s) {
    int res = 0; 
    char color = '0';

    for (int i = 0; i < s.length(); i++) {
        char x = s[i];

        if (color != '0' && x != 'w' && x != color) {
            break;
        } else if (color == '0' && x != 'w') {
            color = x;
        }     
        res++;
    }
    return res;
}

int solve(string beads, int i) {
    beads   += beads;
    string a = beads.substr(0, i);
    reverse(a.begin(), a.end());
    string b = beads.substr(i);

    return longest(a) + longest(b);
}

int main() {
    ifstream fin  ("beads.in");
    ofstream fout ("beads.out");

    int n; fin >> n;
    string beads; fin >> beads;

    int res = 0;
    for (int i = 1; i < n * 2; i++) {
        res = max(res, solve(beads, i));
    }

    // cout << min(res, n) << endl;
    fout << min(res, n) << endl;
    return 0;
}