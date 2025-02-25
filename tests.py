import sys

def can_partition(s, a, b, ab, ba):
    blocks = []
    i, n = 0, len(s)

    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        blocks.append(s[i:j])
        i = j

    single_a = 0
    single_b = 0
    ab_pairs = []
    ba_pairs = []

    for i in range(len(blocks) - 1):
        if blocks[i] == "A" and blocks[i + 1] == "B":
            ab_pairs.append(len(blocks[i]) + len(blocks[i + 1]))
        elif blocks[i] == "B" and blocks[i + 1] == "A":
            ba_pairs.append(len(blocks[i]) + len(blocks[i + 1]))

    for block in blocks:
        if block == "A":
            single_a += len(block)
        elif block == "B":
            single_b += len(block)

    if single_a > a or single_b > b:
        return "NO"

    ab_pairs.sort()
    ba_pairs.sort()

    ab_used = 0
    ba_used = 0

    for length in ab_pairs:
        if ab_used < ab:
            ab_used += 1
        else:
            break

    for length in ba_pairs:
        if ba_used < ba:
            ba_used += 1
        else:
            break

    if ab_used > ab or ba_used > ba:
        return "NO"

    return "YES"


def main():
    input = sys.stdin.read
    data = input().split("\n")

    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        s = data[index].strip()
        a, b, ab, ba = map(int, data[index + 1].split())
        results.append(can_partition(s, a, b, ab, ba))
        index += 2

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
