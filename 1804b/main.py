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
t = II()

for _ in range(t):
    n, k, d, w = MII()
    arr = LII()
    curr_min = arr[0]
    ans = 1
    nums_v = k
    for i in range(len(arr)):
        if nums_v == 0:
            # print(f'At time {arr[i]} the ans increased')
            ans += 1
            nums_v = k - 1
            curr_min = arr[i]
        else:
            if arr[i] - curr_min > d:
                if arr[i] - (curr_min + w) > d:
                    # print(f'At time {arr[i]} the ans increased')
                    ans += 1
                    nums_v = k - 1
                    curr_min = arr[i]
                else:
                    nums_v -= 1
            else:
                nums_v -= 1
        curr_min = min(curr_min, arr[i])

    print(ans)