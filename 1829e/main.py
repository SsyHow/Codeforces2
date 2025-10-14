def I():
    return input()

def II():
    return int(input())

def MII():
    return map(int, input().split())

def LII():
    return list(map(int, input().split()))

# def dfs(i, j):
#     stack = [(i, j)]
#     count = 0
#     while stack:
#         x, y = stack.pop()
#         if x < 0 or x >= n or y < 0 or y >= m:
#             continue
#         if vis[x][y]:
#             continue
#         if L[x][y] == 0:
#             continue
#         vis[x][y] = True
#         count += L[x][y]
#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and L[nx][ny] > 0:
#                 stack.append((nx, ny))
#     return count
#
# T = II()
# for _ in range(T):
#     n, m = MII()
#     L = [LII() for _ in range(n)]
#     vis = [[False]*m for _ in range(n)]
#
#     ans = 0
#     for i in range(n):
#         for j in range(m):
#             if L[i][j] > 0 and not vis[i][j]:
#                 tmp = dfs(i, j)
#                 if tmp > ans:
#                     ans = tmp
#     print(ans)
k = 0
for i in range(II() + 2):
    L = LII()
    print(len(LII()))
    k += 1
print(k)
L = LII()