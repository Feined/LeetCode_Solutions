class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        space = [[1 for j in range(n)] for i in range(m)]
        for i in range(n):
            space[0][i] += 1
        for i in range(m):
            space[i][n-1] += 1
        res = [['' for j in range(n)] for i in range(m)]
        for i in range(n):
            for j in range(m):
                if space[j][i]>1:
                    res[j][i] = '.'
                else:
                    res[j][i] = '#'
        return [''.join(row) for row in res]