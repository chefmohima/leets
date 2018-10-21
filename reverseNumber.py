#Solution after converting to string

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False        #flag for negative number
        string_num = str(x)
        if string_num == '0':
            return 0
        rev_string = string_num[::-1]
        if rev_string[-1] not in ['0','1','2','3','4','5','6','7','8','9']:
            negative = True
            #r = rev_string.pop()
            l = len(rev_string)
            rev_string = rev_string[:l-1]
        if string_num[0] == '0':
            rev_string = rev_string[1:]
        result = int(float(rev_string))
        if result < -2**31 or result > (2**31 - 1):
            return 0
        if negative :
            return -1 * result
        return result
        
        
#Solution without converting to string
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = True if x < 0 else False
        if x == 0:
            return 0
                 
        rev = 0
        n  = abs(x)
        while n > 0:
            remainder = n % 10
            rev = rev * 10 + remainder
            n  = n//10
        if rev < -2**31 or rev > (2**31 - 1):
            return 0
        return rev * -1 if negative else rev
        
        
        
        
