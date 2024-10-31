from itertools import product


def coin_change(amount, coins):
    """Find a solution to an instance of the coin change problem.

    The coins should preferably be sorted in ascending order.
    Code adapted from University of Cape-Town course about dynamic programming.
    """
    inf = 10 ** 9
    dp = [inf for _ in range(amount + 1)]
    coin_used = [-1 for _ in range(amount + 1)]

    dp[0] = 0
    for value, coin in product(range(1, amount + 1), coins):
        j = value - coin
        if j >= 0 and dp[j] < dp[value]:
            dp[value] = dp[j] + 1
            coin_used[value] = coin

    ans = []
    if dp[amount] != inf:
        value = amount
        while value > 0:
            ans.append(coin_used[value])
            value -= coin_used[value]

    return ans


for _ in range(int(input())):
    _ = int(input())
    coins = [int(token) for token in input().split()]
    amount = int(input())
    ls = coin_change(amount, coins)
    print(len(ls) if len(ls) != 0 else -1)
