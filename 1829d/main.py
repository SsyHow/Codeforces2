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



def solve():
    b, c = MII()
    def dfs(k):

        if k == c:
            return True
        if k % 3 != 0:
            return False
        return dfs(k//3) or dfs(k // 3 * 2)

    return "YES" if dfs(b) else "NO"




for _ in range(II()):
    print(solve())