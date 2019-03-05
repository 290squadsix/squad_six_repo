from random import randint
def get_random_puzzle():
    ''' Return a random puzzle '''
    x = randint(1,1) # set second number to number of total puzzles

    puzzle_1 =  [1, 2, 3, 4, 5, 6, 7, 8, 9,
                 4, 5, 6, 7, 8, 9, 1, 2, 3,
                 7, 8, 9, 1, 2, 3, 4, 5, 6,
                 
                 2, 3, 1, 5, 6, 4, 8, 9, 7,
                 5, 6, 4, 8, 9, 7, 2, 3, 1,
                 8, 9, 7, 2, 3, 1, 5, 6, 4,

                 3, 1, 2, 6, 4, 5, 9, 7, 8,
                 6, 4, 5, 9, 7, 8, 3, 1, 2,
                 9, 7, 8, 3, 1, 2, 6, 4, 5]
    
    if x == 1:
        return puzzle_1
