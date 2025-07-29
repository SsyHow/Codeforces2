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
t = II()
for _ in range(t):
    b = II()
    L1 = LII()
    L2 = LII()

    tmp = 0
    f = True
    ff = True
    for i in range(b):
        if L1[i] > L2[i]:
            print("NO")
            break

        elif L1[i] < L2[i]:
            if f and tmp == 0:
                tmp = L2[i] - L1[i]
                f = False
            elif not ff and tmp != 0:
                print("NO")
                break
            elif not f and tmp != L2[i] - L1[i]:
                print("NO")
                break

        else:
            if not f and tmp != 0 :
                ff = False
    else:
        print("YES")

