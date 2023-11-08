#include<string>
#include <iostream>
#include <algorithm>
#include <stack>


using namespace std;

bool solution(string s)
{
    stack<char> st;

    for (char c : s) {
        if (c == '(') {
            st.push(c);
        } else if (c == ')') {
            if (!st.empty() && st.top() == '(') {
                st.pop();
            } else {
                return false;
            }
        }
    }

    return st.empty();
}