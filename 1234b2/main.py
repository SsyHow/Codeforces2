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
n, k = MII()
L = LII()
ans = []
dic = {}
idx = 0
for i in L:
    if i not in dic or idx - dic[i] > k:
        ans.append(i)
        # print(i, idx, dic)
        dic[i] = idx
        idx += 1
#
# print(ans)
print(len(ans[-k:]))
print(*ans[-k:][::-1])