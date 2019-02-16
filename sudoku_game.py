from random import randint


def generate_grid():
    #create grid and return list of size 81


def print_grid(lst_of_ints):
    # Prints grid, returns void.


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

