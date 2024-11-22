# Editorial

The problem is a variation of the classic **0/1 Knapsack Problem**, where we are
given a set of items, each with a specific weight and value. The goal is to
select items such that the total weight does not exceed a given limit $W$,
while maximizing the total value.

Key points to consider:

- We cannot split an item; each item is either fully taken or left behind.
- A brute-force solution, which involves trying all possible subsets of items,
would have a time complexity of $O(2^N)$, which becomes infeasible for larger
$N$ (e.g., $N = 100$).

You will find articles on the knapsack problem on several websites, for example
[cp-algorithms.com](https://cp-algorithms.com/dynamic_programming/knapsack.html)
and [geeksforgeeks.org](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10).
