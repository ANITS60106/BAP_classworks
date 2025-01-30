def minimumcost(n, m, k, roads, citykal):
    if k == 0 or k == n:
        return -1

    kalset = set(citykal)
    mincost = float('inf')

    for u, v, l in roads:
        if (u in kalset and v not in kalset) or (v in kalset and u not in kalset):
            mincost = min(mincost, l)

    return mincost if mincost != float('inf') else -1

n, m, k = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
citykal = list(map(int, input().split())) if k > 0 else []

print(minimumcost(n, m, k, roads, citykal))