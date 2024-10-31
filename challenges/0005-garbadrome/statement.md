# Garbadrome

## Problem description

Kwaku is a cashier at a popular Ivorian restaurant known for its delicious
*garba*. Although Kwaku is quick with the orders, he struggles with providing
the right change using the minimum number of coins.

The restaurant uses a fixed set of coin denominations, and Kwaku must give
change using only these specific coins. Your task is to write a program that
will help Kwaku by calculating the minimum number of coins needed to make the
exact change for any given amount.

## Input

The first line of input contains an integer $T$, the number of testcases.

Each testcase consists of three lines, with the following items:

- $N$ — the number of different coin denominations ($1 \le N \le 100$).
- $C$ — a list of $N$ integers, where each integer represents the value of a coin denomination.
  Each denomination is unique and at least $1$.
- $X$ — the target amount of change Kwaku needs to provide ($1 \le X \le 10,000$).

## Output

For each testcase, print the minimum number of coins needed to make the exact
change for amount $X$. If it's not possible to make the exact change with the
given denominations, print $-1$.

## Sample input

```txt
3
3
1 3 4
6
3
2 5 10
3
4
1 2 5 10
27
```

## Sample output

```txt
2
-1
4
```

## Explanation

- To make 6, Kwaku can use two coins of value 3.
- It's impossible to make 3 with only coins of value 2, 5, and 10.
- Kwaku can make 27 using 10 + 10 + 5 + 2.

## Constraints

- All coin values are positive integers and sorted in ascending order.
- If a solution exists, assume it uses no more than 1,000 coins.

## Hints

Optimize your solution to run efficiently even when $X$ is large.
