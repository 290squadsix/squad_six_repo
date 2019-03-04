from tkinter import *
import sudoku_game as myGame #can use functions from sudoku_game file

class SudokuGUI:
    
    def __init__(self, master):
        """ Create Sudoku application page to select from three difficulties """
        
        self.frame = Frame(master)
        self.currDifficulty = None
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
        
        leftFrame = self.generate_game(leftFrame) # helper to display game
        
        return leftFrame
    
    def get_num_whitespaces(self):
        ''' Return the number of whitespaces for current difficulty '''
        if self.currDifficulty == "easy": # get difficulty
            return 20
        elif self.currDifficulty == "medium":
            return 35
        elif self.currDifficulty == "hard":
            return 50
        
    def get_puzzle_list(self, game, num_whitespaces):
        ''' Returns a list of Entry objects for empty sudoku spaces and Text objects
            for filled sudoku spots '''
        
        puzzle_pieces = []
        # use a sudoku_game function to generate list with whitespaces
        lst_holes = myGame.create_whitespaces(myGame.generate_grid(), {}, num_whitespaces)
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
        
        return puzzle_pieces
        
    
    def generate_game(self, game):    
        ''' Create the puzzle with entry boxes. '''
        
        num_whitespaces = self.get_num_whitespaces()
        puzzle_pieces = self.get_puzzle_list(game, num_whitespaces) # get list of text/entry boxes with puzzle values

                    
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
    
        return game
    
        
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
        return None 
    
    def clearPuzzle(self):
        return None 
    
    def randomizePuzzle(self):
        return None 

root = Tk()
myInstance = SudokuGUI(root)
root.mainloop() 
