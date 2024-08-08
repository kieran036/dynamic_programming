# Write a function count_construct(target, word_bank) that accepts a target string and an array of strings. The function
# should return the number of ways the 'target' can be constructed by concatenating elements of the 'word_bank' array.
# You may reuse elements of the 'word_bank' as many times as needed.

# Brute force version
def count_construct(target, word_bank):
    if target == '':
        return 1
    total = 0
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            num_ways = count_construct(suffix, word_bank)
            total += num_ways
    return total


# Memoization version
def count_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    total = 0
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            num_ways = count_construct(suffix, word_bank, memo)
            total += num_ways
    memo[target] = total
    return total


# Tabulation version
def count_construct(target, word_bank):
    table = [0] * (len(target) + 1)
    table[0] = 1
    for i in range(len(target) + 1):
        for word in word_bank:
            # If word matches the characters at position i
            if target[i: i + len(word)] == word:
                table[i + len(word)] += table[i]
    return table[len(target)]


# print(count_construct('abcdef', ['abc', 'def']))
# print(count_construct('abcdef', ['abcdef']))
# print(count_construct('abcdef', ['ab', 'abc', 'cd']))
count_construct('abcdef', ['abc', 'def', 'abcdef'])
