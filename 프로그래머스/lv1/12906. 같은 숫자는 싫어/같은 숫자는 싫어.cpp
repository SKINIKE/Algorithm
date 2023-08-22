#include <vector>
#include <iostream>
#include <queue>

using namespace std;

vector<int> solution(vector<int> arr) 
{
  vector<int> answer;
  queue<int> temp;

  for (int i : arr) {
    temp.push(i);
  }
  for (int i; temp.size(); i++) {
    int a = temp.front();
    temp.pop();
    if(answer.size() != 0){
        if (a != answer.back()) {
          answer.push_back(a);
        }
    }
    else{
        answer.push_back(a);
    }
  }

  return answer;
}