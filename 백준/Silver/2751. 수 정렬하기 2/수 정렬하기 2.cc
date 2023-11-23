#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
    
  int n, m;
  vector<int> vt;
  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> m;
    vt.push_back(m);
  }
  sort(vt.begin(), vt.end());
  for (int a : vt)
    cout << a << "\n";
    
  return 0;
}
