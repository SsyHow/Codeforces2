def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))
from math import gcd
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def sum_of_digits_in_base(a, base):
    total = 0
    while a > 0:
        total += a % base
        a //= base
    return total

k = II()
ls = 0
num = k - 2
for i in range(2, k):
    ls += (sum_of_digits_in_base(k, i))

print(ls //(gcd(ls, num)), '/', num // gcd(ls, num), sep = '')