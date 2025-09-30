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
    s1 = I()
    s2 = I()
    if s1[0] == s2[0]:
        print("YES")
        print(s1[0] + '*')
        continue
    elif s1[-1] == s2[-1]:
        print("YES")
        print('*' + s1[-1])
        continue
    for i in range(len(s1) - 1):
        if s1[i: i + 2] in s2:
            print("YES")
            print("*" + s1[i] + s1[i+1] + '*')
            break
    else:
        print("NO")