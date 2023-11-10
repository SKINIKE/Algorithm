#include <string>
#include <sstream>

using namespace std;

string solution(string s) {
  string answer = "";
  char pre;

  for (char a : s) {
    if (pre == ' ') {
      answer += toupper(a);
    } else {
      answer += tolower(a);
    }
    pre = a;
  }

  if (isalpha(answer[0]) != 0) {
    answer[0] = toupper(answer[0]);
  }
    
  return answer;
}