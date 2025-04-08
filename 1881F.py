import sys

sys.setrecursionlimit(200000)

def dfs(u, p, d, adj):
    d[u] = d[p] + 1
    for v in adj[u]:
        if v != p:
            dfs(v, u, d, adj)
    return d[u]

def solve():
    n, k = map(int, sys.stdin.readline().split())
    mk = list(map(int, sys.stdin.readline().split()))

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = map(int, sys.stdin.readline().split())
        adj[x].append(y)
        adj[y].append(x)

    if k == 1:
        print(0)
        return

    d = [-1] * (n + 1)
    d[0] = -1
    dfs(mk[0], 0, d, adj)

    a = mk[0]
    for node in mk:
        if d[node] > d[a]:
            a = node

    d = [-1] * (n + 1)
    dfs(a, 0, d, adj)
    dis = max(d[node] for node in mk)
    print((dis + 1) // 2)

if __name__ == "__main__":
    TC = int(sys.stdin.readline())
    for _ in range(TC):
        solve()