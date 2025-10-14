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
L = LII()

c = sum([1 for i in L if i > 0])
vis1 = set()
vis2 = set()
vis3 = set()
if c > 0:
    for i in L:
        if not vis1 and i < 0:
            vis1.add(i)
        elif not vis2 and i > 0:
            vis2.add(i)
        else:
            vis3.add(i)

else:
    for i in L:
        if not vis1 and i < 0:
            vis1.add(i)
        elif len(vis2) < 2 and i < 0:
            vis2.add(i)
        else:
            vis3.add(i)

print(len(vis1), *vis1)
print(len(vis2), *vis2)
print(len(vis3), *vis3)