import math


def dynamic_coin_changing(C, k):
    n = len(C)
    inf = math.inf

    # create two-dimensional array with all zeros
    dp = [[0] * (k + 1) for i in range(n + 1)]  # is range different from xrange?

    dp[0] = [0] + [inf] * k
    print(dp)
    for i in range(1, n + 1):
        for j in range(C[i - 1]):
            dp[i][j] = dp[i - 1][j]
        for j in range(C[i - 1], k + 1):
            dp[i][j] = min(dp[i][j - C[i - 1]] + 1, dp[i - 1][j])
    return dp[n]


def dynamic_coin_changing_memory_save(C, k):
    n = len(C)
    inf = math.inf
    dp = [0] + [inf] * k
    for i in range(1, n + 1):
        for j in range(C[i - 1], k + 1):
            dp[j] = min(dp[j - C[i - 1]] + 1, dp[j])
    return dp


def greedy_algorithm(arr, j):
    count = 0
    denom = []
    while j > 0:
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] <= j:
                count += 1
                print("j:", j)
                denom += [arr[i]]
                j = j - arr[i]
                break
    return count


def greedy_coin_changing(m, k):
    n = len(m)
    result = []
    for i in range(n - 1, -1, -1):
        result += [(m[i], k // m[i])]
        k %= m[i]
    return result


def greedy_coin_changing2(m, k):
    n = len(m)
    result = []
    for i in range(n - 1, -1, -1):
        if k // m[i] > 0:  # see if I can use generator here
            result += [m[i]] * (k // m[i])
            k %= m[i]
    return result


print(dynamic_coin_changing([1, 3 , 4], 6))
print(dynamic_coin_changing_memory_save([1, 3, 4], 6))
print(greedy_algorithm([1, 3, 4], 6))
print(greedy_coin_changing([1, 3, 4], 6))
print(greedy_coin_changing2([1, 3, 4], 6))


