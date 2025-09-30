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

def check(h, m):
    if str(h).zfill(2)[::-1] == str(m).zfill(2):
        return False
    return True
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
hr, mins = I().split(':')
if hr == mins[::-1]:
    print(0)
else:
    mins = int(mins)
    hr = int(hr)
    ans = 0
    while check(hr, mins):
        mins += 1
        if mins == 60:
            hr += 1
        mins %= 60

        hr %= 24
        ans += 1
    print(ans)


