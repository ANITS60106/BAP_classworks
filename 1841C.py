def replace_char(s, i, c):
    return s[:i] + c + s[i + 1:]


def intelectual(c):
    return ord(c) - ord('A')


def solving(s):
    t = s[::-1]
    ans = 0
    max_id = -1
    for x in t:
        i = intelectual(x)
        if max_id > i:
            ans -= 10 ** i
        else:
            ans += 10 ** i
        max_id = max(max_id, i)
    return ans


t = int(input())
for i in range(t):
    s = input()
    candidates = []
    for x in ['A', 'B', 'C', 'D', 'E']:
        for y in ['A', 'B', 'C', 'D', 'E']:
            if not (x in s):
                continue
            candidates.append(replace_char(s, s.find(x), y))
            candidates.append(replace_char(s, s.rfind(x), y))
    print(max(map(solving, candidates)))