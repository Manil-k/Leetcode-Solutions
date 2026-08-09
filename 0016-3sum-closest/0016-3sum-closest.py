class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

            
        nums.sort()
        n = len(nums)
        
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                
                if abs(target - curr) < abs(target - closest):
                    closest = curr
                
                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    return curr   # exact match
        
        return closest
            