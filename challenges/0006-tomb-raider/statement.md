# Tomb Raider

## Problem description

Deep in the scorching sands of the Egyptian desert lies a long-forgotten tomb,
rumored to hold treasures of immeasurable value. One moonlit night, an intrepid
adventurer discovers the hidden entrance to this tomb. Inside, they find
treasures that would make anyone's fortune — golden statues, ancient artifacts,
gemstone-encrusted jewelry, and relics from a bygone era.

However, the adventurer faces a problem: their backpack can only hold a limited
weight, and the tomb's winding corridors are treacherous. Each item has a
specific weight and value, and the adventurer must carefully choose which
treasures to carry out to maximize their haul.

Your task is to help the adventurer decide which items to take to achieve the
maximum total value without exceeding their backpack's weight limit.

The adventurer is in the tomb with $N$ items**, where each item is described by:
- weight $w_i$: the amount the item weighs (measured in kilograms),
- value $v_i$: the worth of the item in gold coins.

The adventurer's backpack has a **maximum weight capacity** $W$, and he cannot
carry more than $W$ kilograms in total.

Your job is to determine the maximum total value of the items the adventurer
can carry out of the tomb without exceeding the weight limit of their backpack.

## Input

The first line contains an integer $T$, the number of testcases in the file.

Each testcase starts with a line with two integers $N$ and $W$, the number
of items in the tomb ($1 \leq N \leq 100$) and the maximum weight capacity of
the adventurer's backpack ($1 \leq W \leq 1000$).

The next $N$ lines consist each two integers $w_i$ and $v_i$, the weight of the
$i$-th item ($1 \leq w_i \leq 1000$) and the value of the $i$-th item
($1 \leq v_i \leq 1000$).


## Output

For each testcase, output a single integer: the **maximum value** the adventurer
can carry in their backpack.

## Sample input

```txt
1
4 7
2 10
3 15
4 20
5 25
```

## Sample output

```txt
35
```

## Explanations

The adventurer has four items to choose from, with weights and values as follows:

- Item 1: weight = $2$, value = $10$.
- Item 2: weight = $3$, value = $15$.
- Item 3: weight = $4$, value = $20$.
- Item 4: weight = $5$, value = $25$.

The backpack’s maximum capacity is $7$.

- If the adventurer chooses items 2 and 3, with a total weight of $7$, they can
carry a total value of $10 + 15 = 35$.
- He can also choose items 1 and 4, for the same result.
- Any other combination would result in a lower total value.

Thus, the maximum value is $35$.

## Bonus Challenge

Extend your program to also output the list of items the adventurer should take
to achieve the maximum value. For example, given the input above, your program
should output something like:

```txt
35
Items: 1, 4
```

Items can be listed in any order.
