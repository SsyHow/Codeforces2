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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def check(n, s):
    for i in s:
        if i == '1' or i == '4' or i == '6' or i == '8' or i == '9':
            print(1)
            print(i)
            return
    for i in range(n):
        for j in range(i + 1, n):

            if L[int(s[i]) * 10 + int(s[j])]  == False:
                print(2)
                print(s[i] + s[j])
                return


def eratosthenes_sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]  # 0 和 1 不是质数

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return is_prime
L = eratosthenes_sieve(100)
a = II()
for _ in range(a):
    b = II()
    s = I()
    check(b, s)
