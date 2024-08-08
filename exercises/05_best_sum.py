# Write a function 'howsum(target_sum, numbers),' that takes in a target_sum and an array of numbers as its argument.
# The function should return an array containing any combination of elements that add up to exactly the
# target_sum. If there is no combination that adds up to the target_sum, then return null.
# Assumes the target_sum and elements in numbers array are numeric.
# If there are multiple combinations possible, you may return any single one.

# Brute force version
def best_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = best_sum(remainder, numbers)
        if remainder_result is not None:
            # Spread operator eqv to iterable unpacking. Dictionary eqv is **
            combination = [*remainder_result, num]
            if (shortest_combination is None) or (len(combination) < len(shortest_combination)):
                shortest_combination = combination
    return shortest_combination


# Memoization version
def best_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    elif target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = best_sum(remainder, numbers, memo)
        if remainder_result is not None:
            combination = remainder_result + [num]
            if (shortest_combination is None) or (len(combination) < len(shortest_combination)):
                shortest_combination = combination
    memo[target_sum] = shortest_combination
    return shortest_combination


# Tabulation version
def best_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []
    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target_sum and ((table[i + num] is None) or (len(table[i + num]) > len(table[i]) + 1)):
                    table[i + num] = [*table[i], num]
    return table[target_sum]


best_sum(4, [2, 1])
best_sum(100, [1, 2, 5, 25])
