#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    int n = 0;
    int m = 0;
    
    cin >> n;
    cin >> m;
    
    string a = to_string(n);
    string b = to_string(m);
    
    reverse(a.begin(), a.end());
    n = stoi(a);
   
    reverse(b.begin(), b.end());
    m = stoi(b);
    
    int result = (n > m) ? n : m;
    cout << result;
}