def solve():
    n = int(input())
    s = list(input().strip())
    ans = 0

    for _ in range(25, 0, -1):
        tag = chr(_ + ord('a'))
        for __ in range(100):
            i = 0
            while i < len(s):
                if s[i] == tag and ((i > 0 and s[i - 1] == chr(ord(tag) - 1)) or (
                        i < len(s) - 1 and s[i + 1] == chr(ord(tag) - 1))):
                    del s[i]
                    ans += 1
                    i -= 1
                i += 1

    print(ans)


if __name__ == "__main__":
    T = 1
    for _ in range(T):
        solve()