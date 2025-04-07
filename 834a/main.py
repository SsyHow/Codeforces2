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

dic = {'^' : 0, '>': 1, 'v': 2, '<': 3}
s1, s2 = I().split()
k = II() % 4

if k == 2 or k == 0:
    print("undefined")
elif k == (dic[s2] - dic[s1]) % 4:
    print("cw")
else:
    print("ccw")
