#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;
    char L[a];
    int ans = 0;

    for (int i = 0; i < a; i ++){
        cin >> L[i];
        if (L[i] == '0') {
            cout << ans + 1 << '\n';
            return 0;
        };
        ans ++;

    };
    cout << ans << '\n';
    return 0;

}
