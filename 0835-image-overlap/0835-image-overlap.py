class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        mx = 0
        for i in range(-n+1,n): #Rows
            for j in range(-n+1,n): #Columns
                count = 0
                for k in range(n):
                    for l in range(n):
                        bi,bj = k+i,l+j
                        if bi<0 or bi>=n or bj<0 or bj>=n:
                            continue
                        if img1[k][l]==1 and img2[bi][bj]==1:
                            count+=1
                mx = max(mx,count)
        return mx