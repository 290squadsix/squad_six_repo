from tkinter import *
import puzzles as all_puzzles
from random import randint
from PIL import Image, ImageTk

class SudokuGUI:
    
    def __init__(self, master):
        """ Create Sudoku application page to select from three difficulties (represented by buttons). """
        
        self.frame = Frame(master)
        self.rightFrame = Frame(master)
        
        self.currDifficulty = None
        self.puzzle = []
        self.puzzle_solution = all_puzzles.get_random_puzzle()
        self.game = None
        master.title("Sudoku")
        
        selectDifficulty = Label(self.frame, text="Select a Difficulty")
        
        image = Image.open("start_screen.jpeg")
        photo = ImageTk.PhotoImage(image)        
        label = Label(self.rightFrame, image=photo)
        label.image = photo

        easyButton = Button(self.frame, text="EASY", command=self.easyDifficulty, font=("Helvetica", 18))
        mediumButton = Button(self.frame, text="MEDIUM", command=self.mediumDifficulty, font=("Helvetica", 18))
        hardButton = Button(self.frame, text="HARD", command=self.hardDifficulty, font=("Helvetica", 18))
        
        label.pack()
        selectDifficulty.pack(pady=(20, 15))
        easyButton.pack()
        mediumButton.pack(pady=(5, 5))
        hardButton.pack()
        self.frame.pack(side=LEFT, padx=(25, 25), pady=(0, 40))
        self.rightFrame.pack(side=RIGHT)
        
    def createFrame(self):
        ''' Create the window and layout for the game. The left frame will be the sudoku board and right frame contains the necessary buttons. '''
        
        game = Tk() 
        game.title("Sudoku")
        
        rightFrame = Frame(game)
        leftFrame = Frame(game)

        rightFrame.pack(side=RIGHT, padx=(100, 100))
        leftFrame.pack(side=LEFT, pady=(80, 80), padx=(100, 20))


        submitButton = Button(rightFrame, text="Submit", command=self.submitPuzzle, font=("Helvetica", 16))
        clearButton = Button(rightFrame, text="Clear", command=self.clearPuzzle, font=("Helvetica", 16))
        randomizeButton = Button(rightFrame, text="Randomize", command=self.randomizePuzzle, font=("Helvetica", 16))
        quitButton = Button(rightFrame, text="Quit", command=game.quit, font=("Helvetica", 16))

        submitButton.pack()
        clearButton.pack(pady=(10, 10))
        randomizeButton.pack(pady=(0, 10))
        quitButton.pack()
        
        num_whitespaces = self.get_num_whitespaces()
        puzzle_pieces = self.get_puzzle_list(leftFrame)
        self.generate_game(leftFrame, num_whitespaces, puzzle_pieces)
        leftFrame = self.get_current_game()
        
        return leftFrame
    
    def get_num_whitespaces(self):
        ''' Return the number of whitespaces to add to the grid for the specified difficulty '''
        
        if self.currDifficulty == "easy":
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
        return self.puzzle[-1]
    
    def get_current_game(self):
        return self.game
    
    def get_solved_puzzle(self):
        return self.puzzle_solution

        
    def get_puzzle_list(self, game):
        ''' Return a list of Entry objects (for empty sudoku spaces), and Text objects (for filled sudoku spots). '''
        
        puzzle_pieces = []
        num_whitespaces = self.get_num_whitespaces()
        lst_holes = self.get_lst_holes(num_whitespaces)
        counter = 0
        while len(puzzle_pieces) != len(lst_holes):
            content = str(lst_holes[counter])
            if lst_holes[counter] != '_':
                spot_solution = Text(game, selectborderwidth=2, width=2, height=1, state=NORMAL)
                spot_solution.insert("1.0",content)
                spot_solution.config(state=DISABLED)
                puzzle_pieces.append(spot_solution)
            else:
                puzzle_pieces.append(Entry(game, selectborderwidth=2, width=2))
            counter += 1
            
        self.puzzle.append(puzzle_pieces)        
        return puzzle_pieces        
    
    def generate_game(self, game, num_whitespaces, puzzle_pieces):    
        ''' Create the puzzle grid '''            
        column_counter = 0
        row_counter = 0
        # display sudoku board in 9x9 format
        for piece in puzzle_pieces:
            piece.grid(row=row_counter//9, column=column_counter % 9)
            row_counter += 1
            column_counter += 1
        self.game = game    
        
    def easyDifficulty(self):
        self.currDifficulty = "easy"
        game = self.createFrame()
        game.mainloop()
    
    def mediumDifficulty(self):
        self.currDifficulty = "medium"
        game = self.createFrame()
        game.mainloop()
        
    def hardDifficulty(self):
        self.currDifficulty = "hard"
        game = self.createFrame()
        game.mainloop()

    def submitPuzzle(self):
        ''' Check whether user has won game or their solution was incorrect. ''' 
        
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
                correct_solution.grid(row=9, columnspan=9)
            else:
                incorrect_solution.grid(row=9, columnspan=9)
        except ValueError:
            invalid_input.grid(row=9, columnspan=9)
    
    def create_submitted_list(self):
        ''' Helper to create a list of the submitted puzzle '''
        
        null_entry = Entry()
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
        ''' Clear empty spaces in a puzzle '''
        
        num_whitespaces = self.get_num_whitespaces()
        counter = 0
        puzzle_pieces = self.get_recent_state()
        game = self.get_current_game()
        null_entry = Entry()
        
        for piece in puzzle_pieces:
            if type(null_entry) == type(piece):
                piece.delete(0,END)
        self.generate_game(game, num_whitespaces, puzzle_pieces)
     
    def randomizePuzzle(self):
        self.clearPuzzle()
        solved_puzzle = all_puzzles.get_random_puzzle()
        self.puzzle_solution = solved_puzzle
        num_whitespaces = self.get_num_whitespaces()
        game = self.get_current_game()
        
        whitespace_list = self.create_whitespaces(solved_puzzle, {}, num_whitespaces)
        new_puzzle = self.get_puzzle_list(game)
        
        self.generate_game(game, num_whitespaces, new_puzzle) #
        
    
    def create_whitespaces(self, input_lst, dic, difficulty):
        ''' Create a list containing the number of white spaces based on the given difficulty. '''

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
