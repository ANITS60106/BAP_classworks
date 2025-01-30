def solve():
    t = int(input())
    results = []

    for _ in range(t):
        n = int(input())
        daughters = []
        holastiki_krasavchiki = set(range(1, n + 1))
        holostici_daughters = set(range(1, n + 1))

        for i in range(1, n + 1):
            data = list(map(int, input().split()))
            k, preferences = data[0], data[1:]
            found = False

            for krasava in preferences:
                if krasava in holastiki_krasavchiki:
                    holastiki_krasavchiki.remove(krasava)
                    holostici_daughters.remove(i)
                    found = True
                    break

            if not found:
                daughters.append((i, preferences))

        if holostici_daughters:
            holostici_daughter = holostici_daughters.pop()
            holastiki_krasava = holastiki_krasavchiki.pop()
            results.append(f"IMPROVE\n{holostici_daughter} {holastiki_krasava}")
        else:
            results.append("OPTIMAL")

    print("\n".join(results))

solve()