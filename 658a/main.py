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
L1 = LII()
L2 = LII()
ans1 = ans2 = 0
t1 = t2 = 0
for i in range(a):
    t1 += L2[i]
    t2 += L2[a -i -1]
    ans1 += max(0, L1[i] - b * t1)
    ans2 += max(0, L1[a-i-1] - b * t2 )
if ans1 == ans2:
    print("Tie")
else:
    print("Limak" if ans1 > ans2 else "Radewoosh")