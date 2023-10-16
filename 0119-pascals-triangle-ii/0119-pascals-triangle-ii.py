class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arrays = [[1]]
        n = rowIndex
        for i in range(n):
            temp = [0] + arrays[-1] + [0]
            row = []
            for j in range(len(arrays[-1])+1):
                row.append(temp[j]+temp[j+1])
            arrays.append(row)
        return arrays[-1]