/*
ID:   andy1li
PROG: gift1
LANG: C++ 
*/

#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main() {
    ifstream fin  ("gift1.in");
    ofstream fout ("gift1.out");

    int n; fin >> n;

    vector<string> names(n);
    map<string, int> balance;
    for (int i = 0; i < n; i++) {
        string name; fin >> name;

        names[i] = name;
        balance[name] = 0;
    }

    for (int i = 0; i < n; i++) {
        string giver; fin >> giver;
        int amount, numReceivers; fin >> amount >> numReceivers;

        for (int i = 0; i < numReceivers; i++) {
            string receiver; fin >> receiver;

            balance[giver]    -= amount / numReceivers;
            balance[receiver] += amount / numReceivers;
        }
    }
    
    for (int i = 0; i < n; i++) {
        string name = names[i];
        // fout << name << ' ' << balance[name] << endl;
        cout << name << ' ' << balance[name] << endl;
    }

    return 0;
}