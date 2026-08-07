class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r = len(mat)
        c = len(mat[0])

        d = [[] for _ in range(r+c-1)]
        for i in range(r):
            for j in range(c):
                d[i+j].append(mat[i][j])
        ans = []
        for i in range(len(d)):
            if i%2==0:
                d[i].reverse()
            ans.extend(d[i])
        return ans
