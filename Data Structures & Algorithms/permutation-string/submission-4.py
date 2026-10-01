class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freqs = [0]*26

        for c in s1:
            i = ord(c) - ord('a')
            freqs[i] += 1
        
        freqs2 = [0]*26
        l = 0
        r = 0
        while r < len(s1):
            # print(r)
            freqs2[ord(s2[r])-ord('a')] +=  1
            r += 1
        # print(r)
        r-=1
        while l<len(s2)-len(s1)+1:
            # print(r)
            # print("___")
            # print(freqs)
            # print(freqs2)
            if freqs2 == freqs:
                return True
            else:
                freqs2[ord(s2[l])-ord('a')] -= 1
                l += 1
                
                if r<len(s2)-1:
                    r += 1
                    freqs2[ord(s2[r])-ord('a')] += 1
        return False



            
