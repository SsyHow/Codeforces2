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
L = LII()
ans = [1]
k = L[0]
k1 = k // 2

x = (sum(L)) // 2
for i in range(1, a):
    if L[i] > k1:
        continue

    k += L[i]
    ans.append(i+1)
    if k > x:
        break
# print(k, x)
if k <= x:
    print(0)
else:
    print(len(ans))
    print(*ans)






