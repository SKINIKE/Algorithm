#include <algorithm>
#include <bitset>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

int main() {
  int n;
  vector<int> vt;
  cin >> n;
  cin.ignore();

  for (int i = 0; i < n; i++) {
    int m;
    cin >> m;
    vt.push_back(m);
  }
  sort(vt.begin(), vt.end());
  for (int a : vt)
    cout << a << endl;
}
