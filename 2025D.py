def read():
    n, m = map(int, input().split())
    rs = list(map(int, input().split()))
    return n, m, rs

class LazySum:
    def __init__(self, n):
        self.ps = [0] * (n + 1)

    def add(self, l, r, val):
        if l > r:
            return
        self.ps[l] += val
        if r + 1 < len(self.ps):
            self.ps[r + 1] -= val

    def pushToAndClear(self, d):
        sum_ = 0
        for i in range(len(self.ps) - 1):
            sum_ += self.ps[i]
            self.ps[i] = 0
            if i < len(d):
                d[i] += sum_

def solve():
    n, m, rs = read()
    ls = LazySum(m + 2)
    d = [-float('inf')] * (m + 1)
    d[0] = 0

    cntP = 0
    for r in rs:
        if r == 0:
            ls.pushToAndClear(d)
            max_d = -float('inf')
            for i in range(1, m + 1):
                d[i] = max(d[i], d[i - 1])
                max_d = max(max_d, d[i])
            cntP += 1
            continue
        if r > 0:
            ls.add(r, m, 1)
        else:
            ls.add(0, cntP + r, 1)

    ls.pushToAndClear(d)
    print(max(d))

if __name__ == '__main__':
    solve()
