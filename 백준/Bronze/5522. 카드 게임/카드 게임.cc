#include <iostream>

using namespace std;

int main(){
    int n = 0;
    int m = 0;
    
    for(int i=0; i<5; i++){
        cin >> n;
        m += n;
    }
    cout << m;
}