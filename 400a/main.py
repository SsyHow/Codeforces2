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
L = [1, 2, 3, 4, 6, 12]
for _ in range(a):
    s = I()
    ans = []
    for i in L:
        for x in range(12 // i):
            if all(s[x + y] == 'X' for y in range(0, 12, 12 // i)):
                ans.append(f'{i}x{12 // i}')
                break



    print(len(ans), ' '.join(ans))