class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        total = 0

        count = {}
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1 #frequency of s[r] in current window
            maxf = max(maxf, count[s[r]]) #max frequency observed in the window

            while (r-l+1)-maxf > k: #window too wide
                count[s[l]] -= 1 #decrement count of char leaving the window
                l += 1 #move left side of window up
            total = max(total, r-l+1) # if window bigger than biggest weve seen, save it
        return total
