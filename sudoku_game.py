from random import randint


def generate_grid():
    #create grid and return list of size 81

    generated_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                     4, 5, 6, 7, 8, 9, 1, 2, 3,
                     7, 8, 9, 1, 2, 3, 4, 5, 6,

                     2, 3, 1, 5, 6, 4, 8, 9, 7,
                     5, 6, 4, 8, 9, 7, 2, 3, 1,
                     8, 9, 7, 2, 3, 1, 5, 6, 4,

                     3, 1, 2, 6, 4, 5, 9, 7, 8,
                     6, 4, 5, 9, 7, 8, 3, 1, 2,
                     9, 7, 8, 3, 1, 2, 6, 4, 5]
    return generated_lst    

def print_grid(lst_of_ints):
    # Print the grid to console for now, void function.
    l = [str(i) for i in lst_of_ints]
    print("    1 2 3   4 5 6   7 8 9")
    print("  +-------+-------+-------+")
    print("A | "+l[0]+" "+l[1]+" "+l[2]+" | "+l[3]+" "+l[4]+" "+l[5]+" | "+l[6]+" "+l[7]+" "+l[8]+" |")
    print("B | "+l[9]+" "+l[10]+" "+l[11]+" | "+l[12]+" "+l[13]+" "+l[14]+" | "+l[15]+" "+l[16]+" "+l[17]+" |")
    print("C | "+l[18]+" "+l[19]+" "+l[20]+" | "+l[21]+" "+l[22]+" "+l[23]+" | "+l[24]+" "+l[25]+" "+l[26]+" |")
    print("  |-------|-------|-------|")
    print("D | "+l[27]+" "+l[28]+" "+l[29]+" | "+l[30]+" "+l[31]+" "+l[32]+" | "+l[33]+" "+l[34]+" "+l[35]+" |")
    print("E | "+l[36]+" "+l[37]+" "+l[38]+" | "+l[39]+" "+l[40]+" "+l[41]+" | "+l[42]+" "+l[43]+" "+l[44]+" |")
    print("F | "+l[45]+" "+l[46]+" "+l[47]+" | "+l[48]+" "+l[49]+" "+l[50]+" | "+l[51]+" "+l[52]+" "+l[53]+" |")
    print("  |-------|-------|-------|")
    print("G | "+l[54]+" "+l[55]+" "+l[56]+" | "+l[57]+" "+l[58]+" "+l[59]+" | "+l[60]+" "+l[61]+" "+l[62]+" |")
    print("H | "+l[63]+" "+l[64]+" "+l[65]+" | "+l[66]+" "+l[67]+" "+l[68]+" | "+l[69]+" "+l[70]+" "+l[71]+" |")
    print("I | "+l[72]+" "+l[73]+" "+l[74]+" | "+l[75]+" "+l[76]+" "+l[77]+" | "+l[78]+" "+l[79]+" "+l[80]+" |")
    print("  +-------+-------+-------+")    

def user_select_difficulty(list_selected_diff):
    # Prompt user to select difficulty, returns the corresponding integer.


def create_whitespaces(input_lst, dic, difficulty):
    # Takes in list and creates difficulty amount of whitespaces, and saves them in a dictionary, returns new list.


def helper_letter_coordinate(s):
    # Changes coordinates into integer, return 0-80 integer.


def check_can_modify_coord(dic, index1):
    # Acesses dictionary to check if coordinate selected by user is modifiable, return boolean answer.


def check_value_in_digit(lst_to_fill, index2):
    # Prompt user for digit they want to input at given index, check if it a digit, return the list with changes.


def check_solve(result_string, latest_input, lst1, lst2):
    # Check if user has won. Print the answer.


def play_game(difficulty_selected):
    # Play game. Loop through possibilities.

    result = "Something may have gone wrong."
    if difficulty_selected[0]:
        lst_holes = create_whitespaces(lst, dict_blanks, difficulty_selected[1])
        print_grid(lst_holes)
        next_input = input("Enter coordinates(letter/number) or Quit(Q): ")
        while (next_input != "S") and (next_input != "s"):
            # checks if valid input
            if (len(next_input) == 2) and (next_input[0] in "ABCDEFGHIabcdefghi") and (next_input[1] in "123456789"):
                x_coord = int(next_input[1])
                y_coord = helper_letter_coordinate(next_input[0])
                index = (y_coord * 9) + x_coord - 1
                can_modify_coord = check_can_modify_coord(dict_blanks, index)  # check if we're allowed to modify index
                if can_modify_coord:  # change value
                    lst_holes = check_value_in_digit(lst_holes, index)  # checks if input is 1-9
                else:
                    print("\nCoordinate you entered cannot be modified.\n")
                next_input = input("Enter coordinates, Quit(Q) or Submit(S): ")
            elif (len(next_input) == 1) and ((next_input == "Q") or (next_input == "q")):  # let user quit game
                result = "Quit"
                next_input = "S"
            else:  # incorrectly formatted commands
                print("Incorrect Coordinates/Command. Please try again.")
                next_input = input("Coordinates have one letter A-I followed by a number 1-9.\n\n"
                                   + "Enter coordinates, Quit(Q) or Submit(S): ")
    check_solve(result, next_input, lst, lst_holes)  # checks if user won


if __name__ == '__main__':
    # Generate, select diffuclty and play.

