#include <iostream>
#include <algorithm>

using namespace std;
 
int main() {
  int cnt;
  float s[1001];

  cin >> cnt;
  for (int i = 0; i < cnt; i++) {
    cin >> s[i];
  }

  sort(s, s + cnt);

  float answer = 0;
  for (int i = 0; i < cnt; i++) {
    answer += (s[i] * 100) / s[cnt - 1];
  }

  cout << answer / cnt << endl;
}