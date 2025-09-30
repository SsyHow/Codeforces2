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
a = I()
hr, mins = a.split(':')
if int(hr[::-1]) > int(mins) and int(hr[::-1]) < 60:
    print(str(hr), ':', str(hr)[::-1], sep='')
else:
    hr = (int(hr) + 1) % 24
    while int(str((hr)).zfill(2)[::-1]) >= 60:
        hr = (int(hr) + 1) % 24


    print(str(hr).zfill(2),':',str(hr).zfill(2)[::-1], sep = '')