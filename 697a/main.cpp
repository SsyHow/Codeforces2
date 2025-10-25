#include <iostream>
using namespace std;

int main() {
    int a, b, c;

    cin >> a >> b >> c;
    int k, r;
    k = (c - a) / b;
    r = (c - a) % b;

    if ((r == 0 && k >= 0) || (r == 1 && k > 0)) {
        cout << "YES\n";
    }else {
        cout << "NO\n";
    }
    return 0;
}
