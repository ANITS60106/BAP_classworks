# A

# def solving(A, B):
#     if A == 0:
#         return B
#     elif A >= 2:
#         return A + 3 * B
#     else:
#         unique_sums = set()
#         for t in range(B + 1):
#             total = 1 + 3 * t
#             unique_sums.add(total)
#             if t > 0:
#                 unique_sums.add(3 * t)
#         return len(unique_sums)
#
# A = int(input())
# B = int(input())
# result = solving(A, B)
# print(result)



# B

# def diploma(n, bally):
#     sorted_bally = sorted(bally, reverse=True)
#     threshold = sorted_bally[n // 2 - 1]
#     if bally[0] >= threshold:
#         return "YES"
#     else:
#         return "NO"
#
# n = int(input())
# bally = [int(input()) for _ in range(n)]
# result = diploma(n, bally)
# print(result)


# c




# D

# def bank_accounting(card):
#     S = 0
#     for i, char in enumerate(card[:-2], start=1):
#         digit = int(char)
#         if i % 2 == 1:
#             S += digit
#         else:
#             S += 2 * digit
#     return S % 100
#
#
# def find_correct_card(n, card):
#     original_checksum = bank_accounting(card)
#     last_two_digits = int(card[-2:])
#     if original_checksum == last_two_digits:
#         return "YES", card
#
#     for i in range(n):
#         for new_digit in range(10):
#             if new_digit == int(card[i]):
#                 continue
#             new_card = card[:i] + str(new_digit) + card[i + 1:]
#             new_checksum = bank_accounting(new_card)
#             new_last_two_digits = int(new_card[-2:])
#             if new_checksum == new_last_two_digits:
#                 return "YES", new_card
#
#     return "NO", ""
#
# n = int(input())
# card = input().strip()
# result, correct_card = find_correct_card(n, card)
# print(result)
# if result == "YES":
#     print(correct_card)

# def collect_coins(n, grid):
#     alice_col, bob_col = 1, 3
#     moves = []
#
#     for i in range(1, n):
#         a_move, b_move = 'D', 'D'
#
#         if alice_col > 1 and grid[i][alice_col - 2] == 'C':
#             a_move = 'L'
#             alice_col -= 1
#         elif alice_col < 3 and grid[i][alice_col] == 'C':
#             a_move = 'R'
#             alice_col += 1
#
#         if bob_col < 3 and grid[i][bob_col] == 'C':
#             b_move = 'R'
#             bob_col += 1
#         elif bob_col > 1 and grid[i][bob_col - 2] == 'C':
#             b_move = 'L'
#             bob_col -= 1
#
#         if alice_col == bob_col:
#             if a_move == 'D':
#                 a_move = 'L' if alice_col > 1 else 'R'
#                 alice_col += -1 if a_move == 'L' else 1
#             else:
#                 b_move = 'L' if bob_col > 1 else 'R'
#                 bob_col += -1 if b_move == 'L' else 1
#
#         moves.append(a_move + b_move)
#
#     return moves
#
#
# n = int(input())
# grid = [input().strip() for _ in range(n)]
# result = collect_coins(n, grid)
# for move in result:
#     print(move)




# def timeforsmth(n, k, increase):
#     height = 0
#     bob_height = 0
#     time = 0
#
#     for i in range(n):
#         height += increase[i]
#         while bob_height < height:
#             bob_height += k
#             time += 1
#             if bob_height >= height:
#                 break
#
#     while bob_height < height:
#         bob_height += k
#         time += 1
#
#     return time
#
# n, k = map(int, input().split())
# increase = list(map(int, input().split()))
#
# print(timeforsmth(n, k, increase))


# def directions(n, s):
#     diri = ['N', 'E', 'S', 'W']
#     newing = 0
#
#     for start in diri:
#         current = start
#         newes = 0
#
#         for target in s:
#             idx = diri.index(current)
#             cw = diri[(idx + 1) % 4]
#             ccw = diri[(idx - 1) % 4]
#
#             if target == cw:
#                 current = cw
#             else:
#                 current = ccw
#
#             if current == target:
#                 newes += 1
#
#         newing = max(newing, newes)
#
#     return newing
#
# n = int(input())
# s = input().strip()
# print(directions(n,s))


# def binary_search_left(arr, target):
#     left, right = 0, len(arr)
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid
#     return left
#
# def binary_search_right(arr, target):
#     left, right = 0, len(arr)
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] <= target:
#             left = mid + 1
#         else:
#             right = mid
#     return left
#
# def mishki(n, q, ranges, queries):
#     starts = sorted(l for l, r in ranges)
#     ends = sorted(r for l, r in ranges)
#
#     results = []
#     for t in queries:
#         start_count = binary_search_right(starts, t)
#         end_count = binary_search_left(ends, t)
#         results.append(start_count - end_count)
#
#     return results
#
# def main():
#     n, q = map(int, input().split())
#     ranges = [tuple(map(int, input().split())) for _ in range(n)]
#     queries = [int(input()) for _ in range(q)]
#
#     results = mishki(n, q, ranges, queries)
#     print('\n'.join(map(str, results)))
#
# if __name__ == "__main__":
#     main()


# def solve():
#     n, m = map(int, input().split())
#     r, g = [], []
#     for _ in range(n):
#         ri, gi = map(int, input().split())
#         r.append(ri)
#         g.append(gi)
#
#     adj = [[] for _ in range(n)]
#     for _ in range(m):
#         u, vi, l = map(int, input().split())
#         u -= 1
#         vi -= 1
#         adj[u].append((vi, l))
#         adj[vi].append((u, l))
#
#     inf = float('inf')
#     dist = [inf] * n
#     dist[0] = 0
#     didntfinish = [(0, 0)]
#
#     while didntfinish:
#         didntfinish.sort()
#         current_time, u = didntfinish.pop(0)
#
#         if current_time > dist[u]:
#             continue
#
#         for v, length in adj[u]:
#             new_time = current_time + length
#             cycle = r[v] + g[v]
#             time_in_cycle = new_time % cycle
#
#             if time_in_cycle < r[v]:
#                 wait_time = r[v] - time_in_cycle
#                 new_time += wait_time
#
#             if new_time < dist[v]:
#                 dist[v] = new_time
#                 didntfinish.append((new_time, v))
#
#
#     print(dist[n - 1])


# def dance(n , k, height):
#     max_length = 1
#     current_lenght = 1
#
#     for i in range (1, n):
#         if abs(height[i] - height[i - 1]) <= k:
#             current_lenght += 1
#             if current_lenght > max_length:
#                 max_length = current_lenght
#         else:
#             current_lenght = 1
#
#     return max_length
#
# n , k = map(int, input().split())
# height = list(map(int, input().split()))
#
# print(dance(n , k, height))


# MOD = 10**9 + 7
#
# def factorials(max_n, MOD):
#     factorial = [1] * (max_n + 1)
#     for i in range(1, max_n + 1):
#         factorial[i] = factorial[i - 1] * i % MOD
#     inv_fact = [1] * (max_n + 1)
#     inv_fact[max_n] = pow(factorial[max_n], MOD - 2, MOD)
#     for i in range(max_n - 1, -1, -1):
#         inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
#     return factorial, inv_fact
#
# def bi(n, k, factorial, inv_fact, MOD):
#     if k < 0 or k > n:
#         return 0
#     return factorial[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
#
# def main():
#     n, m = map(int, input().split())
#     k = list(map(int, input().split()))
#
#     max_k = max(k)
#     factorial, inv_fact = factorials(max_k, MOD)
#
#     dp = [0] * m
#     dp[0] = bi(k[0], n, factorial, inv_fact, MOD)
#
#     for i in range(1, m):
#         dp[i] = dp[i - 1] * bi(k[i], n, factorial, inv_fact, MOD) % MOD
#
#     print(dp[-1])
#
# if __name__ == "__main__":
#     main()


# def determine_lunar_phase(sx, sy, mx, my):
#     dot_product = mx * sx + my * sy
#     cross_product = mx * sy - my * sx
#
#     if dot_product > 0:
#         return "Full moon" if cross_product < 0 else "First quarter"
#     else:
#         return "New moon" if cross_product < 0 else "Third quarter"
#
# q = int(input())
# results = []
# for _ in range(q):
#     sx, sy, mx, my = map(int, input().split())
#     results.append(determine_lunar_phase(sx, sy, mx, my))
#
# print("\n".join(results))

# class SegmentTree:
#     def __init__(self, data):
#         self.n = len(data)
#         self.size = 1
#         while self.size < self.n:
#             self.size <<= 1
#         self.tree = [0] * (2 * self.size)
#         for i in range(self.n):
#             self.tree[self.size + i] = data[i]
#         for i in range(self.size - 1, 0, -1):
#             self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
#
#     def update(self, idx, value):
#         idx += self.size
#         self.tree[idx] = value
#         idx //= 2
#         while idx >= 1:
#             new_val = self.tree[2 * idx] + self.tree[2 * idx + 1]
#             if self.tree[idx] == new_val:
#                 break
#             self.tree[idx] = new_val
#             idx //= 2
#
#     def query(self, l, r):
#         l += self.size
#         r += self.size
#         res = 0
#         while l <= r:
#             if l % 2 == 1:
#                 res += self.tree[l]
#                 l += 1
#             if r % 2 == 0:
#                 res += self.tree[r]
#                 r -= 1
#             l //= 2
#             r //= 2
#         return res
#
# def main():
#     n, q = map(int, input().split())
#     a = list(map(int, input().split()))
#
#     diff = [0] * n
#     for i in range(1, n):
#         diff[i] = abs(a[i] - a[i - 1])
#
#     st = SegmentTree(diff)
#
#     for _ in range(q):
#         event = input().split()
#         if event[0] == '1':
#             p = int(event[1]) - 1
#             total = st.query(0, n - 1)
#             print(total)
#         else:
#             p = int(event[1]) - 1
#             x = int(event[2])
#             a[p] = x
#             if p > 0:
#                 st.update(p, abs(a[p] - a[p - 1]))
#             if p < n - 1:
#                 st.update(p + 1, abs(a[p + 1] - a[p]))
#
# if __name__ == "__main__":
#     main()

# import math
#
# def possible_scores(x1, y1, r1, x2, y2, r2):
#     def distance(x1, y1, x2, y2):
#         return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#
#     d = distance(x1, y1, x2, y2)
#
#     scores = {0}
#
#     if d > r1 + r2:
#         scores.add(1)
#         scores.add(2)
#     elif d + min(r1, r2) <= max(r1, r2):
#         if r2 > r1:
#             scores.add(2)
#         else:
#             scores.add(1)
#         scores.add(3)
#     else:
#
#         scores.add(1)
#         scores.add(2)
#         scores.add(3)
#
#     print(" ".join(map(str, sorted(scores))))
#
#
# x1, y1, r1 = map(int, input().split())
# x2, y2, r2 = map(int, input().split())
# possible_scores(x1, y1, r1, x2, y2, r2)

# def find_string(A, B):
#     n = B - A
#     if n <= 0 or n > 10 ** 5:
#         return "-1"
#
#     if A < 0 or A > 25 * n:
#         return "-1"
#
#     result = ['a'] * n
#     remaining = A
#
#     for i in range(n - 1, -1, -1):
#         add = min(remaining, 25)
#         result[i] = chr(ord('a') + add)
#         remaining -= add
#         if remaining == 0:
#             break
#
#     return ''.join(result)
#
# A = int(input())
# B = int(input())
# print(find_string(A, B))

# def main():
#     S, N, K, A, B = map(int, input().split())
#
#     min_balloons = N
#     min_cost = min_balloons * A
#     remaining_money = S - min_cost
#     max_candies = min(remaining_money // B, K)
#     remaining_money_after_candies = remaining_money - max_candies * B
#     additional_balloons = remaining_money_after_candies // A
#     total_balloons = min_balloons + additional_balloons
#     total_candies = max_candies
#     print(total_balloons, total_candies)
#
# if __name__ == "__main__":
#     main()


# import math
#
# def minimal_plate_radius(N):
#     min_diff = float('inf')
#     best_k = 1
#     for k in range(1, int(math.sqrt(N)) + 1):
#         if N % k == 0:
#             m = N // k
#             diff = abs(k - m)
#             if diff < min_diff:
#                 min_diff = diff
#                 best_k = k
#
#     a = N // best_k
#     b = best_k
#     diagonal = math.sqrt(a**2 + b**2)
#     R = math.ceil(diagonal / 2)
#     return R
#
# N = int(input())
# print(minimal_plate_radius(N))

from collections import deque


def min_days_to_heat(a, b, c, d):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    start = (0, 0)
    target1 = (a, b)
    target2 = (c, d)

    queue = deque([(0, 0)])  # Очередь с клетками, откуда распространяется отопление
    visited = {(0, 0)}  # Множество посещённых клеток
    days = 0

    while queue:
        next_queue = deque()  # Очередь для следующего дня

        while queue:
            x, y = queue.popleft()

            # Проверяем, дошли ли мы до обоих домов
            if target1 in visited and target2 in visited:
                return days

            # Добавляем всех возможных соседей в очередь
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    next_queue.append((nx, ny))

        queue = next_queue
        days += 1  # Увеличиваем количество дней

    return -1  # Теоретически этот случай невозможен


# Чтение входных данных
a, b = map(int, input().split())
c, d = map(int, input().split())

# Вывод результата
print(min_days_to_heat(a, b, c, d))
