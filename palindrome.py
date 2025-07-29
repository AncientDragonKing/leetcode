class Solution(object):
    def isPalindromeStr(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numbers = []
        for char in str(x):
            numbers.append(char)
        if numbers == numbers[::-1]: # [::-1]把清單反轉
            return True
        else:
            return False


    def isPalindromeInt(self, x):
        """
        :type x: int
        :rtype: bool
        """
        palindrome = []
        number = x
        if x < 0 or (x != 0 and x // 10 == 0):
            return False
        half = 0
        while x > half:
            half = (half * 10) + (x % 10)
            x = x // 10
        return x == half or x == half // 10


test = Solution()
result = test.isPalindromeInt(12341)
print(result)