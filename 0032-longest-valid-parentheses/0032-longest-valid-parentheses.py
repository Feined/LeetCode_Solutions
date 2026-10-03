class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = []
        cnt = 0
        opening = closing = 0
        
        # Left to Right
        for ch in s:
            if ch=='(': opening+=1
            else: closing+=1

            if closing>opening: 
                opening = closing = 0
            elif opening==closing:
                cnt = max(cnt,opening+closing)
        # Right to Left
        opening = closing = 0
        for ch in s[::-1]:
            if ch=='(': opening+=1
            else: closing+=1

            if opening>closing:
                opening = closing = 0
            elif opening==closing:
                cnt = max(cnt,opening+closing)
        return cnt