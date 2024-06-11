import math


def main(x, y, z):
    n = len(x)
    return 4 * sum(
        [5 * (73 * x[n - math.ceil(i / 4)] + 47 * y[n - math.ceil(i / 3)] ** 3 + z[n - i] ** 2) for i in
         range(1, n + 1)])


def main(x):
    conditions = [
        [x[0], 2017, 1987, x[3], 'OPA'],
        [x[0], 2008, 1987, x[3], 'OPA'],
        [x[0], x[1], 2017, x[3], 'OPA'],
        [x[0], 2017, 2013, 'ANTLR', 'OPA'],
        [x[0], 2008, 2013, 'ANTLR', 'OPA'],
        ['MAX', x[1], 2013, 'OPA', 'OPA'],
        ['INI', x[1], 2013, 'OPA', 'OPA'],
        ['SAGE', x[1], 2013, 'OPA', 'OPA'],
        [x[0], x[1], 2013, 'ORG', 'OPA'],
        [x[0], x[1], x[2], x[3], 'PIC'],
        [x[0], x[1], x[2], x[3], 'LESS'],
    ]
    return conditions.index(x)
