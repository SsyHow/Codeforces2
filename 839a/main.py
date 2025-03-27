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
a, b = MII()
L = LII()
ka = kb = 0
if b > a * 8:
    print(-1)
else:
    for i in range(a):
        ka += L[i]
        x = min(8, ka)
        kb += x
        ka -= x
        if kb >= b:
            print(i+1)
            break
    else:
        print(-1)