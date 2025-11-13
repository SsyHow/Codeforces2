#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    int x, y, m, n;
    while (t--){
        cin >> x >> y;
        cin >> m >> n;
        bool flag = 0;
        if (x == m and y + n == x){
            flag = 1;
        };
        if (x == n and y + m == x){
            flag = 1;
        };
        if (y == m and x + n == y){
            flag = 1;
        };
        if (y == n and x + m == y){
            flag = 1;
        };
        cout << (flag ? "YES" : "NO") << "\n";
    };


    return 0;
}
