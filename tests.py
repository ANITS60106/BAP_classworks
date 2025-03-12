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


def max_research_value(n, m, items):
    # Initialize DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        w, v = items[i - 1]
        for j in range(m + 1):
            if j >= w:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            else:
                dp[i][j] = dp[i - 1][j]

    # Scenario 1: Special hold is used
    max_value = dp[n][m]

    # Scenario 2: Special hold is used for one item
    for i in range(n):
        w, v = items[i]
        # Remove the current item from the regular cargo hold
        # and add it to the special hold
        remaining_capacity = m
        # Calculate the value without the current item in the regular hold
        value_without_current = dp[n][remaining_capacity]
        # Add the value of the current item in the special hold
        total_value = value_without_current + v
        if total_value > max_value:
            max_value = total_value

    return max_value

n, m = 6, 10
items = [(2, 2), (2, 2), (2, 2), (3, 1), (3, 1), (6, 3)]
print(max_research_value(n, m, items))

