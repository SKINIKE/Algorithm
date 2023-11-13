#include <algorithm>
#include <bitset>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

vector<int> answer;

int main() {
  int n;
  cin >> n;
  cin.ignore();

  string s = "";

  for (int i = 0; i < n; i++) {
    getline(cin, s);
    if (s.substr(0, 4) == "push") {
      int num = stoi(s.substr(5, s.size()));
      answer.push_back(num);
    } else if (s.substr(0, 3) == "pop") {
      if (answer.size() > 0) {
        cout << answer[0] << endl;
        answer.erase(answer.begin());
      } else {
        cout << -1 << endl;
      }
    } else if (s.substr(0, 4) == "size") {
      cout << answer.size() << endl;
    } else if (s.substr(0, 5) == "empty") {
      answer.size() > 0 ? cout << 0 << endl : cout << 1 << endl;
    } else if (s.substr(0, 5) == "front") {
      answer.size() > 0 ? cout << answer[0] << endl : cout << -1 << endl;
    } else if (s.substr(0, 4) == "back") {
      answer.size() > 0 ? cout << answer[answer.size() - 1] << endl
                        : cout << -1 << endl;
    }
  }
}
