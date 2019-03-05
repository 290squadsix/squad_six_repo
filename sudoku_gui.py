from tkinter import *
import puzzles as all_puzzles
from random import randint

class SudokuGUI:
    
    def __init__(self, master):
        """ Create Sudoku application page to select from three difficulties """
        
        self.frame = Frame(master)
        self.currDifficulty = None
        self.puzzle = []
        self.puzzle_solution = all_puzzles.get_random_puzzle()
        self.game = None
        master.title("Sudoku")
        
        # create label
        selectDifficulty = Label(root, text="Select a Difficulty")
        
        # create buttons
        easyButton = Button(self.frame, text="EASY", command=self.easyDifficulty)
        mediumButton = Button(self.frame, text="MEDIUM", command=self.mediumDifficulty)
        hardButton = Button(self.frame, text="HARD", command=self.hardDifficulty)        
              
        selectDifficulty.pack()
        easyButton.pack()
        mediumButton.pack()
        hardButton.pack()
        self.frame.pack()
        
    def createFrame(self):
        ''' Create the window and layout for the game '''
        
        game = Tk() #create new window for Sudoku game
        game.title("Sudoku")
        
        rightFrame = Frame(game) #create frames, assign sides to right and left
        leftFrame = Frame(game) # menu bar on right, sudoku game on left
        rightFrame.pack(side=RIGHT)
        leftFrame.pack(side=LEFT)
        
        submitButton = Button(rightFrame, text="SUBMIT", command=self.submitPuzzle)
        clearButton = Button(rightFrame, text="CLEAR", command=self.clearPuzzle)
        randomizeButton = Button(rightFrame, text="RANDOMIZE", command=self.randomizePuzzle)
        quitButton = Button(rightFrame, text="QUIT", command=game.quit)
        
        submitButton.pack() # display on frame
        clearButton.pack()
        randomizeButton.pack()
        quitButton.pack()
        
        num_whitespaces = self.get_num_whitespaces()
        puzzle_pieces = self.get_puzzle_list(leftFrame) # get list of text/entry boxes with puzzle values
        self.generate_game(leftFrame, num_whitespaces, puzzle_pieces) # method to display game
        leftFrame = self.get_current_game() # get current status of frame
        
        return leftFrame
    
    def get_num_whitespaces(self):
        ''' Return the number of whitespaces for current difficulty '''
        
        if self.currDifficulty == "easy": # get difficulty
            return 20
        elif self.currDifficulty == "medium":
            return 35
        elif self.currDifficulty == "hard":
            return 50
    
    def get_lst_holes(self, num_whitespaces):
        ''' Return a generated list of sudoku puzzle with '_' to represent empty slots '''
        
        num_whitespaces = self.get_num_whitespaces()
        solved_puzzle = self.get_solved_puzzle()
        lst_holes = self.create_whitespaces(solved_puzzle, {}, num_whitespaces)
        
        return lst_holes
    
    def get_recent_state(self):
        ''' Return the most recent version of puzzle_pieces list created by generate_game '''
        return self.puzzle[-1]
    
    def get_current_game(self):
        ''' Return the most current version of frame '''
        return self.game
    
    def get_solved_puzzle(self):
        ''' Return the solved puzzle '''
        return self.puzzle_solution
                
        
    def get_puzzle_list(self, game):
        ''' Returns a list of Entry objects for empty sudoku spaces and Text objects
            for filled sudoku spots '''
        
        puzzle_pieces = []
        num_whitespaces = self.get_num_whitespaces()
        # use a sudoku_game function to generate list with whitespaces
        lst_holes = self.get_lst_holes(num_whitespaces)
        counter = 0
        while len(puzzle_pieces) != len(lst_holes):
            content = str(lst_holes[counter])
            if lst_holes[counter] != '_':
                spot_solution = Text(game, selectborderwidth=2, width=2, height=1, state=NORMAL)
                spot_solution.insert("1.0",content)
                spot_solution.config(state=DISABLED) # make spot read only
                puzzle_pieces.append(spot_solution) # add to list of new puzzle
            else:
                puzzle_pieces.append(Entry(game, selectborderwidth=2, width=2))
            counter += 1
            
        self.puzzle.append(puzzle_pieces)        
        return puzzle_pieces        
    
    def generate_game(self, game, num_whitespaces, puzzle_pieces):    
        ''' Create the puzzle with entry boxes. '''
                  
        column_counter = 0
        index_counter = 0
        for piece in puzzle_pieces: # display sudoku board in 9x9 format
            if column_counter > 8:
                column_counter = 0
            
            if index_counter < 9:
                piece.grid(row=0, column=column_counter)   
                column_counter += 1
            elif index_counter < 18:
                piece.grid(row=1, column=column_counter)
                column_counter += 1
            elif index_counter < 27:
                piece.grid(row=2, column=column_counter)
                column_counter += 1
            elif index_counter < 36:
                piece.grid(row=3, column=column_counter)
                column_counter += 1
            elif index_counter < 45:
                piece.grid(row=4, column=column_counter)
                column_counter += 1
            elif index_counter < 54:
                piece.grid(row=5, column=column_counter)
                column_counter += 1
            elif index_counter < 63:
                piece.grid(row=6, column=column_counter)
                column_counter += 1
            elif index_counter < 72:
                piece.grid(row=7, column=column_counter)
                column_counter += 1
            elif index_counter < 81:
                piece.grid(row=8, column=column_counter)
                column_counter += 1  
            
            index_counter += 1 
        self.game = game    
        
    def easyDifficulty(self):
        """ Create a game with easy difficulty """
        
        self.currDifficulty = "easy"
        game = self.createFrame()
        game.mainloop()

    
    def mediumDifficulty(self):
        ''' Create a game with medium difficulty '''
        
        self.currDifficulty = "medium"
        game = self.createFrame()
        game.mainloop()
        
    def hardDifficulty(self):
        ''' Create a game with hard difficulty '''
        
        self.currDifficulty = "hard"
        game = self.createFrame()
        game.mainloop()

    def submitPuzzle(self):
        ''' Display whether user has won game or the solution was incorrect. ''' 
        
        puzzle_pieces = self.get_recent_state()
        game = self.get_current_game()
        submitted_lst = None
        
        invalid_input = Label(game, text="Invalid input. Please try again", foreground="red")
        correct_solution = Label(game, text="Congratulations! That is correct", foreground="green")
        incorrect_solution = Label(game, text="Your solution is incorrect", foreground="red")
        try:
            submitted_puzzle = self.create_submitted_list()
            solved_puzzle = self.get_solved_puzzle()
            if submitted_puzzle == solved_puzzle:
                correct_solution.grid(row=9, columnspan=9) # display correct statement
            else:
                incorrect_solution.grid(row=9, columnspan=9) # display incorrect statement
        except ValueError:
            invalid_input.grid(row=9, columnspan=9)
    
    def create_submitted_list(self):
        ''' Helper to create a list of submitted puzzle '''
        
        null_entry = Entry() # useless widgets for comparison
        null_text = Text()
        submitted_lst = []
        temp_solution = None
        puzzle_pieces = self.get_recent_state()
        game = self.get_current_game()
        

        for piece in puzzle_pieces:
            if type(piece) == type(null_text):
                temp_solution =  int(piece.get('1.0', 'end-1c'))
            elif type(piece) == type(null_entry):
                temp_solution = int(piece.get())
            else:
                print("there was an error")
            submitted_lst.append(temp_solution)

            
        return submitted_lst
        
    
    def clearPuzzle(self):
        ''' Function to clear empty spaces on a puzzle '''
        
        num_whitespaces = self.get_num_whitespaces()
        counter = 0
        puzzle_pieces = self.get_recent_state()
        game = self.get_current_game()
        null_entry = Entry()
        
        for piece in puzzle_pieces:
            if type(null_entry) == type(piece):
                piece.delete(0,END)
        self.generate_game(game, num_whitespaces, puzzle_pieces) # generate new grid with new 
        
    def randomizePuzzle(self):
        return None 
    
    def create_whitespaces(self, input_lst, dic, difficulty):
    # Takes in list and creates difficulty amount of whitespaces, and saves them in a dictionary, returns new list.

        lst_h = input_lst[:]
        counter = 0
        while counter < difficulty:
            i = randint(0, 80)
            if lst_h[i] != "_":
                dic[i] = lst_h[i]
                lst_h[i] = "_"
                counter += 1
        return lst_h
    
if __name__ == '__main__':
    root = Tk()
    myInstance = SudokuGUI(root)
    root.mainloop() 
