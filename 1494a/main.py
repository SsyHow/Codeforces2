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
    s = I()
    x = ord(s[0]) - ord('A')
    y = ord(s[-1]) - ord('A')
    if s[0] == s[-1]:
        print("NO")
        continue

    d = [0] * 3
    d[x] = 1
    d[y] = -1

    if s.count(chr(x + ord('A'))) == len(s) // 2:
        d[3^x^y] = -1
    else:
        d[3^x^y] = 1



    ans = 0
    for i in s:
        ans += d[ord(i) - ord('A')]
        if ans < 0 :
            print("NO")
            break
    else:
        print("YES" if ans == 0 else "NO")

