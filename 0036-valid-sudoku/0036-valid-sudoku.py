class Solution:
    def isValidSudoku(self, grid: list[list[str]]) -> bool:
        # Validate Rows
        for row in range(9):
            st = set()
            for col in range(9):
                if grid[row][col]=='.':
                    continue
                elif grid[row][col] in st:
                    return False
                st.add(grid[row][col])
        # Validate Colmn
        for col in range(9):
            st = set()
            for row in range(9):
                if grid[row][col]=='.':
                    continue
                elif grid[row][col] in st:
                    return False
                st.add(grid[row][col])
        # Validate the boxes
        for srow in range(0,9,3):
            erow = srow+2
            for scol in range(0,9,3):
                ecol = scol+2
                st = set()
                for i in range(srow,erow+1):
                    for j in range(scol,ecol+1):
                        if grid[i][j]=='.':
                            continue
                        elif grid[i][j] in st:
                            return False
                        st.add(grid[i][j])
        return True