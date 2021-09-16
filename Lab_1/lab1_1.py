import sys


def solve_expression(expression):
    """ return result of math expression. """

    try:

        return eval(expression)
    except NameError:
        return None

expresion = "".join(i for i in sys.argv[1:])
print(solve_expression(expresion))
