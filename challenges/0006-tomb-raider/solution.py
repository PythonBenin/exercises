from sys import stdin, stdout
from itertools import product
from collections import namedtuple


Item = namedtuple('Item', ['weight', 'index', 'value'])


for _ in range(int(stdin.readline())):
    item_count, capacity = (int(token) for token in stdin.readline().split(None, 1))
    items = [Item(0, 0, 0)]
    for i in range(1, item_count + 1):
        w, v = (int(token) for token in stdin.readline().split(None, 1))
        items.append(Item(w, i, v))
    items.sort()

    dp = [[0] * (item_count + 1) for _ in range(capacity + 1)]
    for c, i in product(range(1, capacity + 1), range(1, item_count + 1)):
        item = items[i]
        dp[c][i] = dp[c][i - 1]
        if c >= item.weight:
            alt = dp[c - item.weight][i - 1] + item.value
            dp[c][i] = max(dp[c][i], alt)

    k, picked = capacity, []
    for i in range(item_count, 0, -1):
        if dp[k][i] != dp[k][i - 1]:
            picked.append(items[i].index)
            k -= items[i].weight

    answer = dp[-1][-1]
    picked_items = ' '.join(str(i) for i in sorted(picked))
    stdout.write(f'{answer}\n{picked_items}\n')
