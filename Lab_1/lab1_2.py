import sys
from functools import reduce
from operator import mul, add, truediv, sub

operations = {
    "add": add,
    "sub": sub,
    "truediv": truediv,
    "mul": mul,
}

def solve_conundrum(operation, digits):
    """[show the result of math problem]

    Args:
        operation ([str]): [math operation]
        digits ([list]): [list of numbers]
    """

    try:
        print(reduce(lambda a, b: operations[operation](int(a), int(b)), digits))
    except KeyError:
        print("wrong function")


solve_conundrum(sys.argv[1],sys.argv[2:] )