def solve(x):
    max_b = x // 111
    for b in range(max_b + 1):
        remaining = x - 111 * b
        if remaining % 11 == 0:
            return True
    return False

t = int(input())
for _ in range(t):
    x = int(input())
    if solve(x):
        print("YES")
    else:
        print("NO")