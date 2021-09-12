import sys
import re


def get_express_result(experssion, index=0):
    """ return if correct nat operations and its result. """

    signs = "+-*/"
    if expression and experssion[0] not in signs:
        experssion = "+" + experssion
    else:
        return (False, None)

    if not isinstance(experssion, list):
        experssion = re.findall(re.compile('(\d+|[^ 0-9])'), experssion) #split by each symbol
    try:
        if experssion[index] in signs:
            if (experssion[index+1]).isdigit():
                return get_express_result(experssion, index + 2) #will be analize next two symbols
            raise ValueError
        else:
            raise ValueError
    except ValueError:
        return (False, None)
    except IndexError: #there was no any problem
        return (True, eval("".join(i for i in experssion)))


expression = "".join(i for i in sys.argv[1:])
print(get_express_result(expression))
