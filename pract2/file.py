import os
from random import choice
from timeit import timeit

    
path = '/home/yaroslav/Programming/Python/python/oop_lections/Python-OOP/pract2/file.txt'


with open("file.txt", "a") as file:
    while os.path.getsize(path) < 50000000:
        file.write('1234567890\n')


k = """
with open("file.txt") as file:
    s = 0
    lines = file.readlines()
    for i in lines:
        if i.strip().isdigit():
            s+=int(i.strip())
"""            
print(timeit(k, number=5)/5)

k = """
with open("file.txt") as file:
    s = 0
    for line in file:
        if line.strip().isdigit():
            s+=int(line.strip())
"""
print(timeit(k, number=5)/5)
k = """
with open("file.txt") as file:
    s = sum(int(i.strip()) for i in file if i.strip().isdigit() )    

"""

print(timeit(k, number=5)/5)
