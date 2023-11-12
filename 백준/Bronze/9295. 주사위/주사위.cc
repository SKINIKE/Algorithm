#include <algorithm>
#include <bitset>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

int main() {
  int cnt, a, b;
  cin >> cnt;
  for (int i = 0; i < cnt; i++) {
    cin >> a >> b;
    cout << "Case " << i + 1 << ": " << a + b << endl;
  }
}
