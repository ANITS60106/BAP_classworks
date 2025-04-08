from collections import deque

n, m, k, w = map(int, input().split())
grid = [[[None for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]
parent = [i for i in range(k + 1)]
rank = [1] * (k + 1)
wt = [[0] * (k + 1) for _ in range(k + 1)]
edges = []

for i in range(1, k + 1):
    for j in range(n):
        row = input()
        for l in range(m):
            grid[i][j][l] = row[l]

for i in range(1, k):
    for j in range(i + 1, k + 1):
        diff = 0
        for r in range(n):
            for c in range(m):
                if grid[i][r][c] != grid[j][r][c]:
                    diff += 1
        wt[i][j] = wt[j][i] = diff

def find(a):
    root = a
    while parent[root] != root:
        root = parent[root]
    while a != root:
        next_a = parent[a]
        parent[a] = root
        a = next_a
    return root

def merge(a, b):
    x, y = find(a), find(b)
    if x == y:
        return
    if rank[x] > rank[y]:
        x, y = y, x
    parent[x] = y
    rank[y] += rank[x]

for i in range(1, k):
    for j in range(i + 1, k + 1):
        cost = min(n * m, w * wt[i][j])
        edges.append((cost, i, j))

edges.sort()
ans = 0
final = deque()
used_root = [False] * (k + 1)
connected = [False] * (k + 1)

for cost, u, v in edges:
    if cost == n * m:
        break
    if find(u) != find(v):
        merge(u, v)
        final.append((u, v))
        ans += cost

for i in range(1, k + 1):
    root = find(i)
    if not used_root[root]:
        used_root[root] = True
        final.appendleft((root, 0))
        ans += n * m

print(ans)
connected[0] = True

while final:
    u, v = final.popleft()
    if not connected[v]:
        u, v = v, u
    if not connected[u] and not connected[v]:
        final.append((u, v))
        continue
    print(u, v)
    connected[u] = True
    connected[v] = True