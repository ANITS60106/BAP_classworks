def find(x, parent):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b, parent, size):
    ra = find(a, parent)
    rb = find(b, parent)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]


def main():
    n, m = map(int, input().split())
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    for _ in range(m):
        group = list(map(int, input().split()))[1:]
        if not group:
            continue
        first = group[0]
        for user in group[1:]:
            union(first, user, parent, size)

    result = [str(size[find(i, parent)]) for i in range(1, n + 1)]
    print(" ".join(result))


if __name__ == '__main__':
    main()