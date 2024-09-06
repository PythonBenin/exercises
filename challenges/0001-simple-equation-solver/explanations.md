# Find x

We have to find the solution of an equation with one unknown.

$E(x): l_1 ± ... ± l_n = r_1 ± ... ± r_n$

To add a small difficulty, the variable can be located on any side of the
equation.

The equation can be rewritten as (the unknown is named $x$ for simplicity):

$l_1 ± ... ± x ± l_n ± r_1 ± ... ± r_n = 0$

As we were taught in school, when a term is move to from on side of the
equation to the other, its sign changes.

Let's denote by $S$ the sum of all terms except for $x$.

$S = l_1 ± ... ± l_n ± r_1 ± ... ± r_n$

The equation can be rewritten as:

$S ± x = 0 \Leftrightarrow x = ± S$

All we have to do is to compute the value of $S$ to solve the problem.

When we read an equation, we start by identifying each of its components.
A simple `split` operation based on whitespace is enough to achieve that.
Then we iterate over the items.

- If the item is an operator (`+` or `-`), it will have effect on
  the next term, so we store it in the variable `current_sign`.
- If the item is the equality operator `=`, we will need to flip the sign of
  each term that follows. We use a variable `current_side` to remember on
  which side of the equation we are.
- If the current item is a number, we add or substract its value from $S$ based
  on the operator that precedes it and the side we are currently at. In our
  solution, $S$ is represented by the `terms_sum` variable.
- The last case is the unkown. We need to store the letter used to represent it,
  its side (`left` or `right`), and its sign (`+` or `-`).

When we are done parsing the equation, we will have to update the value of
`term_sum`, based on the sign and side of the unknown.

## IMPORTANT

This is just one method to solve the problem, there are several others.
Feel free to share yours.
