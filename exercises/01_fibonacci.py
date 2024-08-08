# Calculating the Fibonacci sequence

# Brute force version
def fib(n):
    if isinstance(n, int):
        if n < 0:
            print("n must be a non -ve integer")
        elif n <= 2:
            total = 1
            return total
        else:
            total = fib(n - 1) + fib(n - 2)
            return total
    else:
        print("n must be an integer")


# Memoization version
def fib(n, memo={}):
    if isinstance(n, int):
        if n <= 0:
            memo[n] = 0
            return memo[n]
        # If n is in meo the return the memo value
        elif n in memo:
            return memo[n]
        elif n <= 2:
            memo[n] = 1
            return memo[n]
        elif n > 2:
            # Add memo int o function arg to make sure the same memo is being used
            memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
            return memo[n]
        else:
            print("n must be a non -ve integer")
    else:
        print("n must be a non -ve integer")


# Tabulation version
def fib(n):
    table = [0] * (n + 2)
    table[1] = 1
    i = 0
    for i in range(0, n, 1):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
        i += 1
    # del table[-1]
    return table[n]
