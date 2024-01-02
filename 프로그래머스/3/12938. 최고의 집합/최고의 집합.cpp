#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int n, int s) {
    vector<int> answer;
    
    if(s / n < 1){
        answer.push_back(-1);
        return answer;
    }
    
    int a = s / n;
    int b = s % n;
    
    if(b == 0){
        for(int i = 0; i < n; i++){
            answer.push_back(a);
        }
    }else{
        for(int i = 0; i < n; i++){
            answer.push_back(a);
        }
        for(int i = 0; i < b; i++){
            answer[i] += 1;
        }
    }
    
    sort(answer.begin(), answer.end());
    
    return answer;
}