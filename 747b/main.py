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
L = list(I())

dic = {"A" : 0, "G": 0, "C": 0, "T":0}

if a % 4 != 0:
    print("===")
else:
    k = a // 4
    f = True
    for i in L:
        if i != '?':
            dic[i] += 1
            if dic[i] > k:
                f = False
                break
    if not f:
        print("===")
    else:
        for i in range(a):
            if L[i] == '?':
                for j in dic:
                    if dic[j] < k:
                        L[i] = j
                        dic[j] +=1
                        break
        print(''.join(L))