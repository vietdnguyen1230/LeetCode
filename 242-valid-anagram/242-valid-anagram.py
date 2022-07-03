class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#       compare the length of both strings
        if len(s) != len(t):
            return False
#       implement a hashmap for both strings
        countS, countT = {}, {}
#       adding to hashmap/count
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
#       compare both hashmap
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        
        return True
            
        
        