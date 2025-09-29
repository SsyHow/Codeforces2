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
dic = {'0': 6, '1': 2, '2': 5, '3' : 5, '4': 4, '5' :5, '6' : 6, '7': 3, '8' : 7, '9':6}
ans = 0
a, b = MII()
for i in range(a, b + 1):
    for j in str(i):
        ans += dic[j]
print(ans)