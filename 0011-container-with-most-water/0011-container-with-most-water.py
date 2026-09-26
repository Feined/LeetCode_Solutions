class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        
        sm = 0
        l = 0
        r = n-1
        while l<r:
            hght = min(height[l],height[r])
            width = r-l
            sm = max(sm,hght*width)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return sm


