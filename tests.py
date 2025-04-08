# def starting(n, strands):
#     length = len(strands[0])
#     result = []
#
#     for i in range(length):
#         nucleotides = [s[i] for s in strands if s[i] != '.']
#
#         if nucleotides:
#             result.append(nucleotides[0])
#         else:
#             result.append('.')
#
#     return ''.join(result)
#
# n = int(input())
# strands = [input().strip() for _ in range(n)]
# output = starting(n, strands)
# print(output)


# def find_species(n, species_list):
#     for candidate in species_list:
#         is_ancestor = True
#         for other_species in species_list:
#             if not other_species.endswith(candidate):
#                 is_ancestor = False
#                 break
#         if is_ancestor:
#             return candidate
#     return "Not found"
#
# n = int(input())
# species_list = [input().strip() for _ in range(n)]
# result = find_species(n, species_list)
# print(result)


# def max_research_value(n, m, items):
#     # Initialize DP table
#     dp = [[0] * (m + 1) for _ in range(n + 1)]
#
#     # Fill DP table
#     for i in range(1, n + 1):
#         w, v = items[i - 1]
#         for j in range(m + 1):
#             if j >= w:
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
#             else:
#                 dp[i][j] = dp[i - 1][j]
#
#     # Scenario 1: Special hold is used
#     max_value = dp[n][m]
#
#     # Scenario 2: Special hold is used for one item
#     for i in range(n):
#         w, v = items[i]
#         # Remove the current item from the regular cargo hold
#         # and add it to the special hold
#         remaining_capacity = m
#         # Calculate the value without the current item in the regular hold
#         value_without_current = dp[n][remaining_capacity]
#         # Add the value of the current item in the special hold
#         total_value = value_without_current + v
#         if total_value > max_value:
#             max_value = total_value
#
#     return max_value
#
# n, m = 6, 10
# items = [(2, 2), (2, 2), (2, 2), (3, 1), (3, 1), (6, 3)]
# print(max_research_value(n, m, items))

# def main():
#     n, m, kv, kh = map(int, input().split())
#     grid = [input().strip() for _ in range(n)]
#     q = int(input())
#
#     grass = []
#     for i in range(n):
#         for j in range(m):
#             if grid[i][j] == '*':
#                 grass.append((i, j))
#
#     directions = [(-kv, 0), (kv, 0), (0, -kh), (0, kh)]
#
#     graph = {}
#     for cell in grass:
#         i, j = cell
#         graph[cell] = []
#         for di1, dj1 in directions:
#             ni1, nj1 = i + di1, j + dj1
#             if 0 <= ni1 < n and 0 <= nj1 < m and grid[ni1][nj1] == '*':
#                 for di2, dj2 in directions:
#                     ni2, nj2 = ni1 + di2, nj1 + dj2
#                     if 0 <= ni2 < n and 0 <= nj2 < m and grid[ni2][nj2] == '*':
#                         graph[cell].append((ni2, nj2))
#
#     reachable = {}
#     for start in grass:
#         visited = set()
#         queue = []
#         queue.append(start)
#         visited.add(start)
#         while queue:
#             current = queue.pop(0)
#             for neighbor in graph.get(current, []):
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     queue.append(neighbor)
#         reachable[start] = visited
#
#     openness = 0
#     for cell in grass:
#         openness += len(reachable[cell]) - 1
#
#     print(openness)
#
# if __name__ == "__main__":
#     main()


# def portal(X, Y, Z, A, B):
#     if (X <= A and Y <= B) or (X <= B and Y <= A):
#         print("YES")
#     elif (X <= A and Z <= B) or (X <= B and Z <= A):
#         print("YES")
#     elif (Y <= A and Z <= B) or (Y <= B and Z <= A):
#         print("YES")
#     else:
#         print("NO")
#
# X = int(input())
# Y = int(input())
# Z = int(input())
# A = int(input())
# B = int(input())
#
# portal(X, Y, Z, A, B)

#
# def check_victory(grid, row, col, player):
#     directions = [
#         (1, 0),
#         (0, 1),
#         (1, 1),
#         (1, -1)
#     ]
#
#     for dr, dc in directions:
#         count = 1
#
#         r, c = row + dr, col + dc
#         while 0 <= r < 6 and 0 <= c < 7 and grid[r][c] == player:
#             count += 1
#             r += dr
#             c += dc
#
#         r, c = row - dr, col - dc
#         while 0 <= r < 6 and 0 <= c < 7 and grid[r][c] == player:
#             count += 1
#             r -= dr
#             c -= dc
#
#         if count >= 4:
#             return True
#
#     return False
#
# def count_winning_moves(grid):
#     win_count = 0
#
#     for col in range(7):
#         row = -1
#         for r in range(5, -1, -1):
#             if grid[r][col] == ".":
#                 row = r
#                 break
#
#         if row == -1:
#             continue
#
#         grid[row][col] = "R"
#         if check_victory(grid, row, col, "R"):
#             win_count += 1
#         grid[row][col] = "."
#
#     return win_count
#
# grid = [list(input().strip()) for _ in range(6)]
# print(count_winning_moves(grid))


# def find_string(A, B):
#     # Находим длину строки
#     n = B - A
#
#     # Проверяем, существует ли такая строка
#     if n <= 0 or A < 0 or A > 25 * n:
#         return "-1"
#
#     result = []
#     remaining = A  # Остаток, который надо "набрать" буквами
#
#     for _ in range(n):
#         # Максимально возможное значение символа
#         value = min(25, remaining)
#         result.append(chr(ord('a') + value))
#         remaining -= value
#
#     return "".join(result)
#
# # Считываем входные данные
# A = int(input().strip())
# B = int(input().strip())
#
# # Выводим ответ
# print(find_string(A, B))

# def min_operations(n, s):
#     def count_operations(target):
#         operations = 0
#         current = list(s)
#         for i in range(n - 1):
#             if current[i] != target:
#                 operations += 1
#                 current[i + 1] = '1' if current[i + 1] == '0' else '0'
#         if current[-1] != target:
#             if n > 1:
#                 operations += 1
#             else:
#                 return float('inf')
#         return operations
#
#     operations_0 = count_operations('0')
#     operations_1 = count_operations('1')
#     return min(operations_0, operations_1)
#
# n = int(input().strip())
# s = input().strip()
# print(min_operations(n, s))

# def min_operations(n, s):
#     count_0 = s.count('0')
#     count_1 = s.count('1')
#     return abs(count_0 - count_1)
#
# n = int(input().strip())
# s = input().strip()
#
# print(min_operations(n, s))


# a, b = map(int, input().split())
# c, d = map(int, input().split())
#
# d1 = max(abs(a), abs(b))
# d2 = max(abs(c), abs(d))
#
# ans = max(d1, d2, (d1 + d2) // 2 + 1)
# print(ans)

def determine_winner(t, test_cases):
    results = []

    for x1, y1, x2, y2 in test_cases:
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        total = dx + dy

        if total % 2 == 1:
            results.append("Monke")
        else:
            results.append("Potato")

    return results

t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
for result in determine_winner(t, test_cases):
    print(result)

