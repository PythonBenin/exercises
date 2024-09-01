from random import randrange, randint, choice, shuffle
from string import ascii_lowercase
from itertools import islice

case_count = 100
lo, hi = -100, 100
signs = ['+', '-']
extended_signs = ['', '+', '-']


def build_eq_side(terms):
    tokens = []

    for term in islice(terms, len(terms) - 1):
        tokens.append(str(term))
        tokens.append(choice(signs))
    tokens.append(str(terms[-1]))

    return ' '.join(tokens)


for _ in range(case_count):
    lhs = [randrange(lo, hi) for _ in range(randint(1, 10))]
    rhs = [randrange(lo, hi) for _ in range(randint(1, 10))]

    var = choice(ascii_lowercase)
    var_side = lhs if randint(lo, hi) % 2 == 0 else rhs
    var_sign = choice(extended_signs)
    var_side.append(f'{var_sign}{var}')
    shuffle(var_side)

    left = build_eq_side(lhs)
    right = build_eq_side(rhs)
    print(f'{left} = {right}')
