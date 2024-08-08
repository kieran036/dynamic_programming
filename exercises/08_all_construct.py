# Write a function all_construct(target, word_bank) that accepts a target string and an array of strings. The function
# should return a 2D array containing all of the ways that the 'target' can be constructed by concatenating elements
# of the 'word_bank' array. Each element of the 2D array should represent one combination that constructs the 'target'.
# You may reuse elements of the 'word_bank' as many times as needed.

# Brute force version
def all_construct(target, word_bank):
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = list(map(lambda x: [word, *x], suffix_ways))
            result.extend(target_ways)
    return result


# Memoization version
def all_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = list(map(lambda ways: [word, *ways], suffix_ways))
            result.extend(target_ways)
    memo[target] = result
    return result


# Tabulation version
def all_construct(target, word_bank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]
    for i in range(len(target)):
        for word in word_bank:
            if target[i: i + len(word)] == word:
                x = table[i]
                new_combinations = [combination + [word] for combination in table[i]]
                # new_combinations = list(map(lambda combo: [[word], *combo], table[i]))
                table[i + len(word)].extend(new_combinations)
    return table[len(target)]


all_construct('abcdef', ['abc', 'def', 'abcdef'])
# all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])
# all_construct('abcdef', ['abc', 'def'])
# all_construct('abcdef', ['abcdef'])
# all_construct('abcdef', ['ab', 'abc', 'cd'])
