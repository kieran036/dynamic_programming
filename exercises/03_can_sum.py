# Write a function 'can_sum(target_sum, numbers),' that takes in a target_sum and an array of numbers as its argument.
# The function should return a boolean indicating whether or not it is possible to generate the target_sum using numbers
# from the array.
# You may use an element of the array as many times as needed and assume that all numbers are non-negative

# Brute force version
def can_sum(target_sum, numbers):
    if target_sum == 0:
        return True
    elif target_sum < 0:
        return False
    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers) is True:
            return True
    return False


# Memoization version
def can_sum(target_sum, numbers, memo={}):
    # As the numbers don't change with each call, we needn't put this in the key
    if target_sum in memo:
        return memo[target_sum]
    elif target_sum == 0:
        return True
    elif target_sum < 0:
        return False
    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers, memo) is True:
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


# Tabulation version
def can_sum(target_sum, numbers):
    table = [False] * (target_sum + 1)
    table[0] = True
    for i in range(target_sum + 1):
        if table[i]:
            for num in numbers:
                if i + num <= target_sum:
                    table[i + num] = True
    return table[target_sum]


can_sum(7, [2, 3])
