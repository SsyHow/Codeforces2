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
def check(i):
    if i in {'a', 'e', 'i', 'o', 'u'}:
        return True
    return False

def solve():
    s = I()
    t = I()
    if (n := len(s)) != len(t):
        print("NO")
        return

    for i in range(n):
        if check(s[i]) != check(t[i]):
            print("NO")
            return
    print("YES")

solve()