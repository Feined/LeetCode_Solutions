class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        hour_current = int(current[:2])*60 + int(current[3:])
        hour_correct = int(correct[:2])*60 + int(correct[3:])
        diff = hour_correct-hour_current
        res = 0
        for i in [60,15,5,1]:
            res+=diff//i
            diff%=i
        return res