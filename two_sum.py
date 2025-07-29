class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype: list[int]
        """
        num_map = {} 

        for i, num in enumerate(nums): # enumerate() 用意是產生索引和值
            complement = target - num
            print(num_map)
            if complement in num_map:
                return [num_map[complement], i]
                print(num_map)
            num_map[num] = i
            print(num_map)
        return [] 


solver = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solver.twoSum(nums, target)
print(result)