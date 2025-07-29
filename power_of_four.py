class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n <= 0:
        #     return False
        # if (n & (n - 1)) != 0:
        #     return False
        # return (n & 0x55555555) != 0
        return (n & n - 1) == 0 and (n - 1) % 3 == 0
        # return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
do = Solution()
result = do.isPowerOfFour(16)
print(result)