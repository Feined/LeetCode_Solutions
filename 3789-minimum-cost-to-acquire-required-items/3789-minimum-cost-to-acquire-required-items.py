class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1==0 and need2==0:
            return 0
        pairs = min(need1,need2)
        cst = pairs*min(costBoth,cost1+cost2)
        rem1 = need1-min(need1,need2)
        rem2 = need2-min(need1,need2)
        cst1 = rem2*min(costBoth,cost2)+rem1*min(costBoth,cost1)
        return cst1+cst