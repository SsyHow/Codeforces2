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
from collections import Counter
import sys
a = II()
L = LII()
c = Counter(L)
ans = 0
# print(c)
for key, count in c.items():
    if key == 0:
        continue
    if count > 2:  # 若某个非 0 的 ID 出现超过 2 次，数据有误
        print(-1)
        sys.exit()  # 终止程序
    if count == 2:  # 每个出现两次的 ID 代表一对秘书通话
        ans += 1

print(ans)

