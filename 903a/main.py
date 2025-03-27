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

a = II()
for _ in range(a):
    b = II()
    if b % 3 == 0:
        print("YES")
    elif b % 7 == 0:
        print("YES")
    else:
        k = 1
        while k * 3 < b:
            if (b - k * 3) % 7 == 0:
                print("YES")
                break
            k += 1
        else:
            print("NO")