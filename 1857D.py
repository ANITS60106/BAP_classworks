import sys
def solve():
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1

        a = list(map(int, data[index:index + n]))
        index += n

        b = list(map(int, data[index:index + n]))
        index += n
        d = [a[i] - b[i] for i in range(n)]
        max_d = max(d)

        strong_vertices = [i + 1 for i in range(n) if d[i] == max_d]

        results.append(f"{len(strong_vertices)}")
        results.append(" ".join(map(str, strong_vertices)))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()