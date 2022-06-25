class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         2 strategies: hash table or sort

        # return sorted(s) == sorted(t) - sorting solution
    
        if len(s) != len(t):
            return False
        
        
#         create hash table
        countS, countT = {}, {}
        
#         add characters to hashtable
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
#         compare both strings in hashtable
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        
        return True
            