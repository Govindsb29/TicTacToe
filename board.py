class Board:
    def __init__(self): #board ki grid banane ke liye
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self): #board ka layout display hoga
        for row in self.grid:
            print("|".join(row))
            print("-----")

    def is_valid(self,row,col):
        if 0 <= row <=2 and 0 <= col <= 2:
            return self.grid[row][col] == " "
        return False 
    
    def make_move(self, row, column, symbol):
        if self.grid[row][column]==" ":
            self.grid[row][column] = symbol
            return True
        else:
           return False
        
    def check_winner(self,symbol):
        for row in self.grid:
            if row[0]==symbol and row[1]==symbol and row[2]==symbol:
                return True
            
        for col in range(3):
            if self.grid[0][col]==symbol and self.grid[1][col]==symbol and self.grid[2][col]==symbol:
                return True
            
        if self.grid[0][0]==symbol and self.grid[1][1]==symbol and self.grid[2][2]==symbol:
            return True
        
        if self.grid[0][2]==symbol and self.grid[1][1]==symbol and self.grid[2][0]==symbol:
            return True
        
        return False
    
    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == " ":
                    return False
        return True
