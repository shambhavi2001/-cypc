'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).'''

#Solution: 

class Solution:    
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return False
        pointer=0
        for letter in t:
            if letter==s[pointer]:
                pointer+=1
            if pointer==len(s):
                return True
        return False
                
        
