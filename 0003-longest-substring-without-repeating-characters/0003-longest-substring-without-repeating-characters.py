class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mxLen = 0
        left = 0
        res = ''
        st = set()
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left+=1
            st.add(s[right])
            mxLen = max(mxLen,right-left+1)
        return mxLen
