class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        '''
        APPROACH - 1
        
        m = len(matrix) # Row
        n = len(matrix[0]) # Columns
        pos = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    pos.append((i,j))
                    # setRow(matrix,m,n,i,j) # Ex: (1,1)
                    # setColumn(matrix,m,n,i,j)
        # for i in pos:
        #     setRow(matrix,m,n,i[0],i[1])
        #     setColumn(matrix,m,n,i[0],i[1])
        for row, col in pos:
            for j in range(n):
                matrix[row][j] = 0
            for i in range(m):
                matrix[i][col] = 0
        '''
        # APPROACH - 2
        m = len(matrix)
        n = len(matrix[0])
        zero_row = set()
        zero_col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zero_row.add(i)
                    zero_col.add(j)
        for i in zero_row:
            for j in range(n):
                matrix[i][j]=0
        for i in zero_col:
            for j in range(m):
                matrix[j][i]=0
        