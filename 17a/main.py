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
def eratosthenes_sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]  # 0 和 1 不是质数

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

n, k = MII()
L = eratosthenes_sieve(n)
K = set(eratosthenes_sieve(2 * n))
cnt = 0

for i in range(len(L) - 1):
    if L[i] + L[i + 1] + 1 in L:
        cnt += 1
print("YES" if cnt >= k else "NO")