class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def getEmptyCount(row):
            count = 0
            for i in row:
                if i == ".":
                    count += 1
            return count
        def isRowValid(rowNumber):
            row = board[rowNumber]
            return len(set(row)) == 10 - getEmptyCount(row)
        def isColumnValid(colNumber):
            column = []
            for x in board:
                column.append(x[colNumber])
            return len(set(column)) == 10 - getEmptyCount(column)
        def isCellValid(cell):
            return len(set(cell)) == 10 - getEmptyCount(cell)

        def get3by3(colNo, rowNo):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(board[3 * rowNo + i][3 * colNo + j])
            return block


        for i in range(0, len(board)):
            # print(f"isRowValid:{i} - ", isRowValid(i))
            if not isRowValid(i):
                return False

        for i in range(0, len(board)):
            if not isColumnValid(i):
                return False


        for i in range(3):
            for j in range(3):
                cell = get3by3(i, j)
                if not isCellValid(cell):
                    return False
        return True