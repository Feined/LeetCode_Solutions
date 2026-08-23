class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        lst = []
        # Missing Numbers
        ms = []
        s = set(nums)
        for i in range(lower,upper+1):
            if i not in s:
                ms.append(i)
        
        l = 0
        while l<len(ms):
            r = l
            while r+1<len(ms) and ms[r+1]==ms[r]+1:
                r+=1
            lst.append([ms[l],ms[r]])
            l=r+1
        return lst