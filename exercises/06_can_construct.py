# Write a function can_construct(target, word_bank) that accepts a target string and an array of strings. The function
# should return a boolean indicating whether or not the 'target' can be constructed by concatenating elements of the
# 'word_bank' array. You may reuse elements of the 'word_bank' as many times as needed.

# Brute force version
def can_construct(target, word_bank):
    # if type(target) != str or not bool([element for element in word_bank if(type(element) == str)]):
    #    return
    if target == '':
        return True
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if can_construct(suffix, word_bank):
                return True
    return False


# Memoization version
def can_construct(target, word_bank, memo={}):
    # if type(target) != str or not bool([element for element in word_bank if(type(element) == str)]):
    #    return
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False


# Tabulation version
def can_construct(target, word_bank):
    table = [False] * (len(target) + 1)
    table[0] = True
    for i in range(len(target) + 1):
        if table[i]:
            for word in word_bank:
                # If word matches the characters at position i
                if target[i: i + len(word)] == word:
                    table[i + len(word)] = True
    return table[len(target)]


# print(can_construct('abcdef', ['abc', 'def']))
# print(can_construct('abcdef', ['abcdef']))
# print(can_construct('abcdef', ['ab', 'abc', 'cd)
