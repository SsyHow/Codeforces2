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

a, b = MII()
s = I()

if b > a//2:
    dir = 1
else:
    dir = -1

while b != a and b != 1:
    if dir == 1:
        print("RIGHT")
        b += 1
    else:
        print("LEFT")
        b -= 1

if b == 1:
    while b <= a:
        print(f"PRINT {s[b-1]}")
        b += 1
        if b <= a:
            print("RIGHT")

else:
    while b >= 1:
        print(f"PRINT {s[b-1]}")
        b -= 1
        if b >= 1:
            print("LEFT")



