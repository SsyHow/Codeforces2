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
n = II()
a = II()
b = II()

if n == 1:
    if a == b:
        print(1)
    else:
        print(0)
    print(f'{a}:{b}')
elif a + b < n:
    print(n - a - b)
    for _ in range(a):
        print('1:0')
    for _ in range(b):
        print('0:1')
    for _ in range(n-a-b):
        print('0:0')
elif a + b >= n and (a == 0 or b == 0):
    print(0)
    for _ in range(min(max(a, b), n) -1):
        if a > 0:
            print('1:0')
            a -= 1

        if b > 0:
            print('0:1')
            b -= 1
    if a > 0:
        print(f'{a}:0')
    if b > 0:
        print(f'0:{b}')
else:
    print(0)
    a1 = 1
    b1 = 1

    t = a - 1
    m = b - 1
    for _ in range(n-2):
        if t > 0:
            print('1:0')


            t -= 1
            continue

        if m > 0:
            print('0:1')
            m -= 1
    # print(a1, t)
    print(f'{a1 + t}:0')
    print(f'0:{b1 + m}')


