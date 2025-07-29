import string
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]# 65, 91
        if columnNumber <= 26:
            return letters[columnNumber - 1]
        elif columnNumber > 26:
            return letters[columnNumber // 26 -1] + letters[columnNumber % 26 -1]
do = Solution()
result = do.convertToTitle(701)
print(result)