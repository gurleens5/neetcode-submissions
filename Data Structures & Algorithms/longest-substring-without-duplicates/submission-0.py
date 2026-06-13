class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mx = 0
        substring = set()

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            mx = max(mx, r - l + 1)
        
        return mx
            
            