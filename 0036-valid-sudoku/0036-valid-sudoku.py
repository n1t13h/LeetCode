class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_group(group):
            seen = set()
            for value in group:
                if value != '.':
                    if value in seen:
                        return False
                    seen.add(value)
            return True

        def get_3x3_block(row, col):
            block = []
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    block.append(board[i][j])
            return block

        for i in range(9):
            if not is_valid_group(board[i]):  # Check rows
                return False
            if not is_valid_group([board[j][i] for j in range(9)]):  # Check columns
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not is_valid_group(get_3x3_block(i, j)):  # Check 3x3 blocks
                    return False

        return True
