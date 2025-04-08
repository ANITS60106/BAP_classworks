# n, m, a = map(int, input().split())
# kartinka = [list(input()) for _ in range(m)]
# a = (a % 360 + 360) % 360
#
# def rotate_90(kartinka):
#     return [list(row) for row in zip(*kartinka[::-1])]
#
# povorot = a // 90
#
# for _ in range(povorot):
#     kartinka = rotate_90(kartinka)
#
# h = len(kartinka)
# w = len(kartinka[0])
# print(w, h)
#
# for row in kartinka:
#     print(''.join(row))





# v1, v2, n = map(int, input().split())
# chemodany = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     chemodany.append((a, b))
#
# dp = [[0] * (v2 + 1) for _ in range(v1 + 1)]
#
# for ob, cost in chemodany:
#     for i in range(v1, -1, -1):
#         for j in range(v2, -1, -1):
#             if i >= ob:
#                 dp[i][j] = max(dp[i][j], dp[i - ob][j] + cost)
#             if j >= ob:
#                 dp[i][j] = max(dp[i][j], dp[i][j - ob] + cost)
#
# print(dp[v1][v2])


# n = int(input())
# a = list(map(int, input().split()))
# left = sorted([x for x in a if x < 0], reverse=True)
# right = sorted([x for x in a if x > 0])
# best_cost = float('inf')
#
# for i in range(len(left) + 1):
#     left_part = left[:i]
#     right_part = right
#     order = left_part + right_part + left[i:]
#     pos = 0
#     total = 0
#     cost = 0
#
#     for x in order:
#         move = abs(x - pos)
#         cost += total + move
#         total += move
#         pos = x
#
#     best_cost = min(best_cost, cost)
#
# for i in range(len(right) + 1):
#     right_part = right[:i]
#     left_part = left
#     order = right_part + left_part + right[i:]
#     pos = 0
#     total = 0
#     cost = 0
#
#     for x in order:
#         move = abs(x - pos)
#         cost += total + move
#         total += move
#         pos = x
#
#     best_cost = min(best_cost, cost)
#
# print(best_cost)


# def solve():
#     import sys
#     input = sys.stdin.read().splitlines()
#     N, M = map(int, input[0].split())
#     order_list = input[1:N + 1]
#     order_dict = {word: idx for idx, word in enumerate(order_list)}
#     sentences = input[N + 1:N + 1 + M]
#
#     for sentence in sentences:
#         words = sentence.split()
#         in_order = []
#         not_in_order = []
#         for word in words:
#             if word in order_dict:
#                 in_order.append((order_dict[word], word))
#             else:
#                 not_in_order.append(word)
#         in_order_sorted = [word for (_, word) in sorted(in_order, key=lambda x: x[0])]
#         not_in_order_sorted = sorted(not_in_order, key=lambda x: (x, len(x)))
#         sorted_sentence = in_order_sorted + not_in_order_sorted
#         print(' '.join(sorted_sentence))
#
# solve()


# while True:
#     num = int(input("Введите число:"))
#     if num % 2 == 0:
#         print("Чётное")
#     else:
#         print("Нечётное")
#     again = input("Хотите проверить другое число? (да/нет): ").lower()
#     if again == "нет":
#         break






