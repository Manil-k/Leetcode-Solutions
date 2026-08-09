class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        j = len(needle)
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            if haystack[i:(i+j)] == needle:
                return i

