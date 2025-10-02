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
L = []
for _ in range(3):
    L.append(list(I()))
ans = 'ZZZ'
for r1 in range(3):
    for c1 in range(3):
        for r2 in range(3):
            for c2 in range(3):
                if r1 == r2 and c1 == c2:
                    continue

                if abs(r1 - r2) <= 1 and abs(c2 - c1) <= 1:

                    for r3 in range(3):
                        for c3 in range(3):
                            if (r1 == r3 and c1 == c3) or (r2 == r3 and c2 == c3):
                                continue

                            if abs(r2 - r3) <= 1 and abs(c2 - c3) <= 1:
                                ans = min(ans, ''.join([L[r1][c1], L[r2][c2], L[r3][c3]]))
print(ans)

