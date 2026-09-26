class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        l = 0
        r = n-1
        while l<r:
            sm = numbers[l]+numbers[r]
            if sm==target:
                return [l+1,r+1]
            elif sm<target:
                l+=1
            else:
                r-=1
        return 