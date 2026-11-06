class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cand1 = cand2 = None
        cnt1 = 0
        cnt2 = 0
        for i in nums:
            if i==cand1:
                cnt1+=1
            elif i==cand2:
                cnt2+=1
            elif cnt1==0:
                cand1 = i
                cnt1 = 1
            elif cnt2==0:
                cand2 = i
                cnt2 = 1
            else:
                cnt1-=1
                cnt2-=1
        ans = []
        for cand in (cand1,cand2):
            if cand is not None and nums.count(cand)>len(nums)//3:
                if cand not in ans:
                    ans.append(cand)
        return ans