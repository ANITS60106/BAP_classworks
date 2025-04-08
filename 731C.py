from collections import defaultdict, deque

n, m, k = map(int, input().split())
c = [0] + list(map(int, input().split()))

v = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

def dfs_iterative(start, visited):
    stack = [start]
    visited[start] = True
    color_count = defaultdict(int)
    while stack:
        node = stack.pop()
        color_count[c[node]] += 1
        for neighbor in v[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    return color_count

visited = [False] * (n + 1)
ans = 0

for i in range(1, n + 1):
    if not visited[i]:
        color_count = dfs_iterative(i, visited)
        total = sum(color_count.values())
        mx = max(color_count.values())
        ans += total - mx

print(ans)