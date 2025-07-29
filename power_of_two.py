class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return (n & (n - 1)) == 0 


do = Solution()
result = do.isPowerOfTwo(1)
print(result)

# & (Bitwise AND)

#   0101  (5)
# & 0011  (3)
# ------
#   0001
  
#   1000  (8)
# & 0111  (7)
# ------
#   0000