from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxx = max(nums)
        return gcd(mini,maxx)