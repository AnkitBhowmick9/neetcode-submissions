class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagram = {}
        for i in s:
            if i not in anagram:
                anagram[i] = 1
            else:
                anagram[i] += 1
        
        for j in t:
            if j in anagram:
                anagram[j] -= 1
            else:
                anagram[j] = -1
        
        for key, val in anagram.items():
            if val < 0:
                return False
        return True

            
            

        