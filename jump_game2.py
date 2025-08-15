class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = 1
        place = 2
        while place != len(nums):
            if nums[place-1] <= 0:
                return times            
            place += nums[place-1]
            times += 1
        return times

        
do = Solution()
print(do.jump([2, 3, 1, 1, 4]))