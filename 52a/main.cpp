#include <iostream>
using namespace std;

int main() {
    int a;
    int x;
    int K[3] = {0};
    cin >> a;
    for (int i = 0; i < a; i++){
        cin >> x;
        K[x - 1] ++;
    }
    cout << min( min(K[0] + K[1], K[1] + K[2]), K[0] + K[2] ) << "\n";
    return 0;
}
