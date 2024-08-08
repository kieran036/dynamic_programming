# Write a function 'how_sum(target_sum, numbers),' that takes in a target_sum and an array of numbers as its argument.
# The function should return an array containing any combination of elements that add up to exactly the
# target_sum. If there is no combination that adds up to the target_sum, then return null.
# Assumes the target_sum and elements in numbers array are numeric.
# If there are multiple combinations possible, you may return any single one.

# Brute force version
def how_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers)
        if remainder_result is not None:
            # Spread operator eqv to iterable unpacking. Dictionary eqv is **
            # return [*remainder_result, num]
            return remainder_result + [num]
    return None


# Memoization version
def how_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    elif target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers, memo)
        if remainder_result is not None:
            # Spread operator eqv to iterable unpacking. Dictionary eqv is **
            memo[target_sum] = remainder_result + [num]
            # memo[target_sum] = [*remainder_result, num]
            # return memo[target_sum]
            return remainder_result + [num]
    memo[target_sum] = None
    return None


# Tabulation version
def how_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []
    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target_sum:
                    table[i + num] = [*table[i], num]
    return table[target_sum]


print(how_sum(7, [2, 3]))
