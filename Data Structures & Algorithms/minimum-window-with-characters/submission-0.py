class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        freqT = {}
        freqWindow = {}
        have = 0
        
        res = [-1, -1]
        resLen = float("infinity")
        l = 0

        for c in t:
            freqT[c] = freqT.get(c, 0) + 1
        
        need = len(freqT)

        for r in range(len(s)):
            c = s[r]
            freqWindow[c] = freqWindow.get(c, 0) + 1

            if c in t and freqWindow[c] == freqT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                freqWindow[s[l]] -= 1
                if s[l] in freqT and freqWindow[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]: res[1]+1] if resLen != float("infinity") else ""

                



            