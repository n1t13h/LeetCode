class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[''] * 3 for _ in range(3)]

        def check_winner(player):
            # Check rows and columns
            for i in range(3):
                if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                    return True

            # Check diagonals
            if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
                return True

            return False

        for i, move in enumerate(moves):
            player = 'A' if i % 2 == 0 else 'B'
            board[move[0]][move[1]] = player
            if check_winner(player):
                    return player

        return "Draw" if len(moves) == 9 else "Pending"