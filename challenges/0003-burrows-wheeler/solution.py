from sys import stdin


class Shift:
    def __init__(self, index, s):
        self.index = index
        self.string = s
        self.rank = (-1, -1)

    def __lt__(self, other):
        if not isinstance(other, Shift):
            raise Exception('Invalid argument for comparison with Shift')
        return self.rank < other.rank


def sorted_cyclic_shifts(s):
    """Sort all cyclic shifts of a string.

    Code from http://cp-algorithms.com/string/suffix-array.html.
    """
    n = len(s)
    shifts = [Shift(j, s) for j in range(n)]
    ranks = [ord(c) for c in s]
    length, limit = 1, 2 * n
    while length < limit:
        h = length // 2
        for shift in shifts:
            x = ranks[shift.index]
            y = ranks[(shift.index + h) % n]
            shift.rank = (x, y)
        shifts.sort()

        rank = 0
        ranks[shifts[0].index] = rank
        for j in range(1, n):
            previous, current = shifts[j-1], shifts[j]
            if previous.rank != current.rank:
                rank += 1
            ranks[current.index] = rank

        length *= 2

    return [shift.index for shift in shifts]


def bwt(s):
    """Burrows-Wheeler transform."""
    shifts = sorted_cyclic_shifts(s)
    t = "".join(s[j-1] for j in shifts)
    return t, shifts.index(0)


def inverse_bwt(t, k):
    """Inverse Burrows-Wheeler transform."""
    n = len(t)
    f = sorted((ch, j) for j, ch in enumerate(t))
    chars = []
    for _ in range(n):
        ch, j = f[k]
        chars.append(ch)
        k = j
    return "".join(chars)


print('\n'.join(map(lambda line: bwt(line[:-1])[0], stdin)))
