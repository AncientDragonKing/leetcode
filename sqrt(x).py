class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 1
        if x <= 0:
            return
        while x != num * num:
            num += 1
            if num * num > x:
                return num - 1
        return num


solution = Solution()
print(solution.mySqrt(8))