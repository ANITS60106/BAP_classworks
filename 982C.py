def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    n = int(input())

    if n % 2 != 0:
        print(-1)
        return

    v = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        v[a].append(b)
        v[b].append(a)

    vis = [0] * (n + 1)
    parent = [-1] * (n + 1)
    evens = 0
    size = [1] * (n + 1)

    stack = [(1, -1)]
    while stack:
        u, p = stack.pop()
        if vis[u] == 0:
            vis[u] = 1
            stack.append((u, p))
            for nd in v[u]:
                if nd != p:
                    parent[nd] = u
                    stack.append((nd, u))
        elif vis[u] == 1:
            vis[u] = 2
            if p != -1:
                size[p] += size[u]
            if size[u] % 2 == 0:
                evens += 1

    print(evens - 1 if evens > 0 else 0)


if __name__ == "__main__":
    main()