import sys
from ultrasplit import split_by_symbol


def get_express_result(expression, index=0):
    """ return if correct nat operations and its result. """

    signs = "+-*/"
    if expression[0] not in signs:
        expression = "+" + expression

    if not isinstance(expression, list):
        expression = split_by_symbol(expression)  # split by each symbol
    try:
        if expression[index] in signs:
            if (expression[index+1]).isdigit():
                # will be analize next two symbols
                return get_express_result(expression, index + 2)
            return (False, None)
        else:
            return (False, None)
    except IndexError:  # there was no any problem
        return (True, eval("".join(i for i in expression)))


expression = "".join(i for i in sys.argv[1:])
print(get_express_result(expression) if expression else (False, None))
