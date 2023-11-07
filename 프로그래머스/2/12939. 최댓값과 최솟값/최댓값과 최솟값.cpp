#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;

string solution(string s) {
  string answer = "";
  vector<int> vec;
  stringstream ss;
  int temp;

  ss.str(s);

  while (ss >> temp) {
    vec.push_back(temp);
  }

  answer += to_string(*min_element(vec.begin(), vec.end()));
  answer += " ";
  answer += to_string(*max_element(vec.begin(), vec.end()));

  cout << answer;
  return answer;
}