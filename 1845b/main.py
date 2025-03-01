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
for i in range(II()):
    A = LII()
    B = LII()
    C = LII()
    print((abs(A[0] - B[0]) + abs(A[1]- B[1]) + abs(A[0] - C[0]) + abs(A[1]- C[1]) - (abs(C[0] - B[0]) + abs(C[1]- B[1])))//2 + 1)