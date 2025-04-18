from board import Board
from player import Player


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
    
    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
        
    
    def start(self):
        while True:
            self.board.display()
            print(self.current_player.name+"'s turn "+"("+self.current_player.symbol+")")

            row = int(input("Enter Row: "))
            col = int(input("Enter Col: "))

            if self.board.is_valid(row, col):
                self.board.make_move(row, col, self.current_player.symbol)

                if self.board.check_winner(self.current_player.symbol):
                    self.board.display()
                    print(self.current_player.name+" wins")
                    break

                elif self.board.is_full():
                    self.board.display()
                    print("Draw!")
                    break

                self.switch_player()

            else:
                print("Invalid Move")


if __name__ == "__main__":

    name1 = input("Enter Player 1 name: ")
    name2 = input("Enter Player 2 name: ")
    
    player1 = Player(name=name1, symbol="X")
    player2 = Player(name=name2, symbol="O")
    
    game = Game(player1, player2)
    

    game.start()