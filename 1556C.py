def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for i in range(0, n, 2):
        cnt = 0
        for j in range(i, n):
            if j % 2 == 0:
                cnt += a[j]
            else:
                r = cnt - 1
                l = cnt - a[j]
                r = min(r, a[i])
                l = max(0, l)
                ans += max(0, r - l + 1)
                cnt -= a[j]
                a[i] = min(a[i], cnt)
                if cnt < 0:
                    break

    print(ans)

def main():
    solve()

if __name__ == "__main__":
    main()