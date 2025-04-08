import sys
from collections import Counter

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        n = int(input[ptr])
        ptr += 1
        a_list = list(map(int, input[ptr:ptr + n]))
        ptr += n

        cnt = Counter(a_list)
        sorted_keys = sorted(cnt.keys())
        a = [cnt[k] for k in sorted_keys]
        n_a = len(a)

        if n_a == 0:
            print(0)
            continue

        INF = float('inf')
        dp = [INF] * (n_a + 1)
        dp[0] = 0

        for i in range(1, n_a + 1):
            current_a = a[i - 1]
            max_possible_k = i - (current_a - 1)
            max_k = min(i, max_possible_k)
            if max_k < 1:
                continue
            for k in range(max_k, 0, -1):
                new_value = dp[k - 1] + current_a
                if new_value <= i - k and new_value < dp[k]:
                    dp[k] = new_value

        ans = n_a
        while ans >= 0 and dp[ans] == INF:
            ans -= 1
        print(n_a - ans)


if __name__ == "__main__":
    main()