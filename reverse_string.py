class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        return s[::-1]
do = Solution()
result = do.reverseString(["H","a","n","n","a","h"])
print(result)