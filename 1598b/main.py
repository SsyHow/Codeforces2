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
    L = [0] * 5
    t = []
    ans = False
    for i in range(b):
        t.append(LII())
    for i in range(5):
        for j in range(5):
            if i != j:
                cnt1 = 0
                cnt2 = 0
                cntno = 0

                for z in range(b):
                    if t[z][i] == 1:
                        cnt1 += 1
                    if t[z][j] == 1:
                        cnt2 += 1
                    if t[z][j] == t[z][i] == 0:
                        cntno += 1
                if cnt1 >= b // 2 and cnt2 >= b // 2 and cntno == 0:
                    ans = True
    print("YES" if ans else "NO")