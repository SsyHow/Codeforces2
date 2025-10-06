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

def check(a, b):
    if a == '?':
        a = b
    if b == '?':
        b = a
    # print(a, b, {'a', 'b', 'c'} - {a, b})
    return {'a', 'b', 'c'} - {a, b}

a = II()
for _ in range(a):
    s = I()
    ans = []
    n = len(s)
    if n != 1:

        for i in range(n):
            if i == 0:
                if s[i] == '?':
                    if n > 0 and s[i + 1] == 'a':
                        ans.append('b')
                    else:
                        ans.append('a')
                else:
                    ans.append(s[i])
            elif 0 < i < n - 1:
                if s[i] != '?':
                    ans.append(s[i])
                else:
                    k = check(ans[-1], s[i + 1])
                    ans.append(tuple(k)[0])
            else:
                if s[i] == '?':
                    k = check(ans[-1], '?')
                    ans.append(tuple(k)[0])
                else:
                    ans.append(s[i])
        prev = ans[0]
        for i in range(1, n):
            if ans[i - 1] == ans[i]:
                print(-1)
                break
        else:
            print(''.join(ans))
    else:
        if s == '?':
            print('a')
        else:
            print(s)