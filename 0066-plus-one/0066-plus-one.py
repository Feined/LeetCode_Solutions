class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Approach 1
        n = len(digits)
        l = 0
        for i in digits:
            l = l*10 + i
        res = []
        app = str(l+1)
        for i in app:
            res.append(int(i))
        return res