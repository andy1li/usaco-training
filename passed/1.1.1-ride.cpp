/*
ID:   andy1li
PROG: ride
LANG: C++         
*/

#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int hash(const string &name) {
    int res = 1;

    for (int i = 0; i < name.size(); i++) {
        res *= (name[i] - 'A' + 1);
        res %= 47;
    }

    return res;
}

int main() {
    ifstream fin  ("ride.in");
    ofstream fout ("ride.out");

    string comet, group;
    fin >> comet;
    fin >> group;

    if (hash(comet) == hash(group)) {
        fout << "GO" << endl;
    } else {
        fout << "STAY" << endl;
    }

    return 0;
}