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
from collections import defaultdict
import heapq
dic = defaultdict(list)

a, b = MII()
L1 = LII()
L2 = LII()
K = []
for i in range(a):
    dic[L1[i]].append(L2[i])

for i in range(1, b+1):
    dic[i].sort()
K = []
cnt = 0
ans = 0
for i in dic:
    if len(dic[i]) >= 2:
        for j in dic[i][:-1]:
            heapq.heappush(K, j)
    elif dic[i] == []:
        cnt += 1
while cnt > 0 :
    ans += heapq.heappop(K)
    cnt -= 1

print(ans)


