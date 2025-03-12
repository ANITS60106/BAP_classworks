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


import math

def konfety(k):
    total = k * (k + 1) // 2
    if total % 2 != 0:
        return False

    half = total // 2
    D = 1 + 8 * half
    sqrt_D = math.isqrt(D)
    if sqrt_D * sqrt_D != D:
        return False
    n = (-1 + sqrt_D) // 2
    return n * (n + 1) // 2 == half

t = int(input())
for _ in range(t):
    k = int(input())
    if konfety(k):
        print('yes')
    else:
        print('no')