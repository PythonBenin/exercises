from itertools import product


def coin_change(amount, coins):
    """Find a solution to an instance of the coin change problem.

    The coins should preferably be sorted in ascending order.
    Code adapted from an UCT course about dynamic programming.
    """
    inf = 10 ** 9
    counts = [inf for _ in range(amount + 1)]
    coin_used = [-1 for _ in range(amount + 1)]

    counts[0] = 0
    for value, coin in product(range(1, amount + 1), coins):
        j = value - coin
        if j >= 0 and counts[j] < counts[value]:
            counts[value] = counts[j] + 1
            coin_used[value] = coin

    ans = []
    if counts[amount] != inf:
        i = amount
        while i > 0:
            ans.append(coin_used[i])
            i -= coin_used[i]

    return ans


for _ in range(int(input())):
    _ = int(input())
    coins = [int(token) for token in input().split()]
    amount = int(input())
    ls = coin_change(amount, coins)
    print(len(ls) if len(ls) != 0 else -1)
