import random

class TicTacToe:
    def __init__(self, difficulty="medium"):
        self.board = [" " for _ in range(9)]
        self.difficulty = difficulty
        self.human = "X"
        self.ai = "O"
        self.game_over = False
    
    def print_board(self):
        print("\n")
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
        print("\n")
    
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
    
    def check_winner(self, player):
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(self.board[i] == player for i in combo) for combo in win_combos)
    
    def minimax(self, depth, is_maximizing):
        if self.check_winner(self.ai):
            return 10 - depth
        if self.check_winner(self.human):
            return depth - 10
        if not self.available_moves():
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for move in self.available_moves():
                self.board[move] = self.ai
                score = self.minimax(depth + 1, False)
                self.board[move] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.available_moves():
                self.board[move] = self.human
                score = self.minimax(depth + 1, True)
                self.board[move] = " "
                best_score = min(score, best_score)
            return best_score
    
    def ai_move(self):
        moves = self.available_moves()
        
        if self.difficulty == "easy":
            # Random move
            return random.choice(moves)
        
        elif self.difficulty == "medium":
            # 50% chance of best move, 50% random
            if random.random() < 0.5:
                return random.choice(moves)
            # Otherwise find best move
            best_score = float('-inf')
            best_move = moves[0]
            for move in moves:
                self.board[move] = self.ai
                score = self.minimax(0, False)
                self.board[move] = " "
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move
        
        else:  # hard
            # Always play optimally
            best_score = float('-inf')
            best_move = moves[0]
            for move in moves:
                self.board[move] = self.ai
                score = self.minimax(0, False)
                self.board[move] = " "
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move
    
    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        print(f"Difficulty: {self.difficulty.upper()}")
        print("Positions are numbered 0-8:")
        print("0 | 1 | 2")
        print("-----")
        print("3 | 4 | 5")
        print("-----")
        print("6 | 7 | 8\n")
        
        while not self.game_over:
            self.print_board()
            
            # Human move
            while True:
                try:
                    move = int(input("Your move (0-8): "))
                    if move in self.available_moves():
                        self.board[move] = self.human
                        break
                    else:
                        print("Invalid move! That position is taken or out of range.")
                except ValueError:
                    print("Please enter a number between 0 and 8.")
            
            if self.check_winner(self.human):
                self.print_board()
                print("You win! Congratulations!")
                self.game_over = True
                break
            
            if not self.available_moves():
                self.print_board()
                print("It's a tie!")
                self.game_over = True
                break
            
            # AI move
            print("AI is thinking...")
            ai_move = self.ai_move()
            self.board[ai_move] = self.ai
            print(f"AI played position {ai_move}")
            
            if self.check_winner(self.ai):
                self.print_board()
                print("AI wins! Better luck next time.")
                self.game_over = True
                break
            
            if not self.available_moves():
                self.print_board()
                print("It's a tie!")
                self.game_over = True
                break

def main():
    while True:
        print("\nSelect Difficulty:")
        print("1. Easy (AI plays randomly)")
        print("2. Medium (AI plays intelligently 50% of the time)")
        print("3. Hard (AI plays perfectly)")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            game = TicTacToe("easy")
        elif choice == "2":
            game = TicTacToe("medium")
        elif choice == "3":
            game = TicTacToe("hard")
        else:
            print("Invalid choice!")
            continue
        
        game.play()
        
        if input("\nPlay again? (y/n): ").lower() != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
