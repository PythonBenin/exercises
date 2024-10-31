# Editorial

The task is to compute the minimum number of coins needed to make an exact
amount $X$ using a given set of coin denominations. If it's not possible to
make the amount with the given denominations, the solution should return $-1$.

This problem is a classic example of the **minimum coin change problem**.
It can be solved using **dynamic programming** .

## Approach

Let's break down the solution into manageable steps.

- **Dynamic Programming State Definition**:
  - Define `dp[x]` as the minimum number of coins needed to make the amount `x`.
   
- **Base Case**:
  - `dp[0] = 0`, since zero coins are needed to make the amount `0`.

- **Recursive Relation**:
  - For each amount `x` from `1` to `X`, try using each coin `c` from the list
    of denominations.
  - If `x - c >= 0`, then check if `dp[x - c]` can be used to reach `x`.
    The recursive relation is:

    $$dp[x] = \min(dp[x], dp[x - c] + 1)$$

  - This means, to achieve amount `x`, we see if we can reduce it by `c`
    (the coin value) and use the result of `dp[x - c]`. If using   `dp[x - c]`
    provides a smaller number of coins, we update `dp[x]`.

- **Final State**:
  - After filling out the `dp` array up to `dp[X]`, if `dp[X]` is still at its
    initialized value (like infinity), it means `X` cannot be formed with the
    given coins, so we return `-1`.
  - Otherwise, `dp[X]` contains the minimum number of coins needed to make `X`.

### Note

Although not required by the problem, the solution provided allows to list to
list the coins used for an input value.

## Complexity Analysis

- **Time Complexity**: $O(N * X)$
  - The outer loop runs up to $X$ times, and for each amount, we try each of
    the $N$ coins.
- **Space Complexity**: $O(X)$
  - We need an array of size $X + 1$ to store the minimum coins for each amount.

## Edge Cases

- **Unreachable Target**: If $X$ can't be formed with the given coins,
  `dp[X]` should remain infinity, so return $-1$.
- **Single Coin Type**: If there's only one coin type, check if $X$ is
  divisible by it.
- **Large Value of X**: Ensure that the solution is efficient enough to
  handle large values of $X$, up to $10 000$, as specified.


##  Disclaimer

Editorial partially provided by ChatGPT. So, it's possible than you find parts
of it on random websites. :smile:
