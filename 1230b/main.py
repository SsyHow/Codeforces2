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
def do():
    n, k = MII()
    s = I()
    s = list(s)
    if n == 1 and k >= 1:
        print(0)
        return
    if k and s[0] != '1':
        s[0] = '1'
        k -= 1
    for i in range(1, n):
        if k == 0:
            break
        if s[i] != '0':
            s[i] = '0'
            k -= 1
    print(''.join(s))

do()