class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = sorted(list(set([x for x in nums if x > 0])))
        
        if not new or new[0] != 1:
            return 1
          
        for i in range(1, len(new)):
            if (new[i] - new[i-1]) != 1:
                return new[i-1] + 1
      
        return new[-1] + 1