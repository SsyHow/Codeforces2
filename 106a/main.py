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


dic = {'6' :6, '7': 7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K': 13,'A':14}

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = I()
a1, a2 = I().split()

print("YES" if (a1[1] == s and a2[1] != s) or (a1[1] == a2[1] and  dic[a1[0]] > dic[a2[0]]) else "NO")

