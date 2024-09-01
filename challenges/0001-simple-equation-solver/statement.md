# Find X

## Problem description

Implement a simple equation solver to evaluate expressions consisting of
numbers, variables, addition, and subtraction operators.

## Input

Input consists of at most 100 equations, each on a line of its own.

Each equation contains one unknown identified by a lowercase letter. The
unknown will be located in either the right or left-hand side of the equation.

Terms of the equations are separated by spaces. If a term is signed, there
will be no space between the term and its sign.

The numbers that appear in the equations have an absolute value less than 100.

## Output

For each equation, ouput a line in the form:

```txt
<var> = <value>
```

where `<var>` is the name of the unknown in the equation, and `<value>` is the
solution to the equation.

## Sample input

```txt
+4 - +5 - x  = 2
-4 -  5 - y  = 2
+4 - -5 - z  = 2
-4 -  5 = -a + 2
+4 -  5 = +d + 2
```

## Sample output

```txt
x = -3
y = -11
z = 7
a = 11
d = -3
```

## Generate test cases

The script `generator.py` can be used to generate test data. Just run:

```bash
python generator.py > in.txt
```
