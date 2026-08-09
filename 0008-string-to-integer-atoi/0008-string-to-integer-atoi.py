class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0]== '-':
            sign = -1
            i += 1
        elif s[0] == "+":
            i += 1
        
        num = 0

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        out =  sign * num
     
        if out < (-2**31): out = -2**31
        if out > (2**31) - 1 : out = (2**31) - 1
        return out
        
        
                    
