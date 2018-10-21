class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

 #Alternate solution
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        return False
    
