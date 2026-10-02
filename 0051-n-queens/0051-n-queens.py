class Solution:
    def issafe(self,board,row,n,column):
        # Check vertically upwards
        for i in range(row):
            if board[i][column]=='Q':
                return False
        # Check Diagonally left
        i = row-1
        j = column-1
        while i>=0 and j>=0:
            if board[i][j]=='Q':
                return False
            i-=1
            j-=1
        # Check Diagonally right
        i = row-1
        j = column+1
        while i>=0 and j<n:
            if board[i][j]=='Q':
                return False
            i-=1
            j+=1
        return True
    def nqueen(self,board,n,row):
        if row>=n:
            self.result.append([''.join(r) for r in board])
            return self.result
        for column in range(n):
            if self.issafe(board,row,n,column):
                board[row][column] = 'Q'
                self.nqueen(board,n,row+1)
                board[row][column] = '.'
            
    def solveNQueens(self, n: int) -> list[list[str]]:
        self.result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        row = 0
        self.nqueen(board,n,row)
        return self.result