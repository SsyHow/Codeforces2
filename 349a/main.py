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
dic = {25: 0, 50: 0}

for i in L:
    if i == 25:
        dic[25] += 1
    elif i == 50:
        if dic[25] > 0:
            dic[25] -= 1
            dic[50] += 1
        else:
            print("NO")
            break
    else:
        if dic[50] > 0 and dic[25] > 0:
            dic[50] -= 1
            dic[25] -= 1
        elif dic[25] > 2:
            dic[25] -= 3
        else:
            print("NO")
            break
else:
    print("YES")