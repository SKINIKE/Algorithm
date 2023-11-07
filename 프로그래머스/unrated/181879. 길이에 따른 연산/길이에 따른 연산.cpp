#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> num_list) {
    
    int answer = 0;
    
    if((int)num_list.size() > 10){
        for(int a : num_list) answer += a;
    }
    else{
        answer = 1;
        for(int a : num_list) answer *=a;
    }
    return answer;
}