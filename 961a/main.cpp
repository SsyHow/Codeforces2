#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    vector<int> L(a, 0);
    int k;
    for (int i = 0; i < b; i++) {
        cin >> k;
        L[k-1] ++;
    };
    int m;
    m = *min_element(L.begin(), L.end());

    cout << m << '\n';
    return 0;
}
