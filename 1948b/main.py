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
for _ in range(a):
    b = II()
    L = LII()

    stack = []
    q = []
    prev = -1
    for i in L:
        if i >= prev:
            stack.append(i)
            prev = i
        else:
            y = i
            while stack and stack[-1] > y:
                x = stack.pop()
                for j in str(x)[::-1]:
                    q.append(int(j))
                y = q[-1]
            while q:
                stack.append(q.pop())

            stack.append(i)
            prev = i
        # print(stack)
    for i in range(len(stack) - 1):
        if stack[i] > stack[i + 1]:
            print("NO")
            break
    else:
        print("YES")