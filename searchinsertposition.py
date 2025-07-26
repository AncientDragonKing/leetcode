class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, k in enumerate(nums):
            if target == k or target < k:
                return i
        return i + 1


do = Solution()
result = do.searchInsert([1,3,5,6], 7)
print(result)