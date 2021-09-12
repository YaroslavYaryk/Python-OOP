import sys


def solve_expression(expression):
    """ return result of math expression. """

    return eval(expression)


expresion = "".join(i for i in sys.argv[1:])
print(solve_expression(expresion))
