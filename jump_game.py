class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        place = 2
        while place != len(nums):
            if nums[place-1] <= 0:
                return False            
            place += nums[place-1]
        return True

        
do = Solution()
print(do.canJump([3,2,1,0,4]))