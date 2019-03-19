from random import randint
from random import *


def get_grid():
    ''' Return a random puzzle '''
    x = randint(1, 3)  
    
    puzzle_1 =  [1, 2, 3, 4, 5, 6, 7, 8, 9,
                 4, 5, 6, 7, 8, 9, 1, 2, 3,
                 7, 8, 9, 1, 2, 3, 4, 5, 6,

                 2, 3, 1, 5, 6, 4, 8, 9, 7,
                 5, 6, 4, 8, 9, 7, 2, 3, 1,
                 8, 9, 7, 2, 3, 1, 5, 6, 4,

                 3, 1, 2, 6, 4, 5, 9, 7, 8,
                 6, 4, 5, 9, 7, 8, 3, 1, 2,
                 9, 7, 8, 3, 1, 2, 6, 4, 5]

    puzzle_2 =  [8, 2, 7, 1, 5, 4, 3, 9, 6,
                 9, 6, 5, 3, 2, 7, 1, 4, 8,
                 3, 4, 1, 6, 8, 9, 7, 5, 2,

                 5, 9, 3, 4, 6, 8, 2, 7, 1,
                 4, 7, 2, 5, 1, 3, 6, 8, 9,
                 6, 1, 8, 9, 7, 2, 4, 3, 5,

                 7, 8, 6, 2, 3, 5, 9, 1, 4,
                 1, 5, 4, 7, 9, 6, 8, 2, 3,
                 2, 3, 9, 8, 4, 1, 5, 6, 7]

    puzzle_3 =  [2, 4, 6, 8, 5, 7, 9, 1, 3,
                 1, 8, 9, 6, 4, 3, 2, 7, 5,
                 5, 7, 3, 2, 9, 1, 4, 8, 6,

                 4, 1, 8, 3, 2, 9, 5, 6, 7,
                 6, 3, 7, 4, 8, 5, 1, 2, 9,
                 9, 5, 2, 1, 7, 6, 3, 4, 8,

                 7, 6, 4, 5, 3, 2, 8, 9, 1,
                 3, 2, 1, 9, 6, 8, 7, 5, 4,
                 8, 9, 5, 7, 1, 4, 6, 3, 2]

    if x == 1:
        return puzzle_1
    if x == 2:
        return puzzle_2
    if x == 3:
        return puzzle_3


def helper_digits(lst):

    x = randint(1, 9)
    while x in lst:
        x = randint(1, 9)
    lst.append(x)

    return x


def get_random_puzzle():

    lst = get_grid()

    digits = []

    a = helper_digits(digits)
    b = helper_digits(digits)
    c = helper_digits(digits)
    d = helper_digits(digits)
    e = helper_digits(digits)
    f = helper_digits(digits)
    g = helper_digits(digits)
    h = helper_digits(digits)
    z = helper_digits(digits)

    i = 0

    while i < 81:

        if lst[i] == 1:
            lst[i] = a
        elif lst[i] == 2:
            lst[i] = b
        elif lst[i] == 3:
            lst[i] = c
        elif lst[i] == 4:
            lst[i] = d
        elif lst[i] == 5:
            lst[i] = e
        elif lst[i] == 6:
            lst[i] = f
        elif lst[i] == 7:
            lst[i] = g
        elif lst[i] == 8:
            lst[i] = h
        elif lst[i] == 9:
            lst[i] = z
        i += 1

    return lst
