class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        sign = 1
        if x[0] == ('-'): x, sign = x[1:], -1
        if x[0] == '+' : x = x[1:]
        reverse = x[::-1]
        ans = int(reverse)
        if ans < (-2**31): ans = 0
        elif ans > (2**31)-1 : ans = 0
        return ans*sign
        