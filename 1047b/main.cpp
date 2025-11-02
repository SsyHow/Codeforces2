#include <iostream>
#include <math.h>

int main() {
    int t;
    std::cin >> t;
    int x, y;
    int k = 0;
    for (int i = 0; i < t; i++){
        std::cin >> x >> y;
        k = fmax(k, x + y);
    }
    std::cout <<  k << "\n";
    return 0;
}
