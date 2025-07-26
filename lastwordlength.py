class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = []
        for line in s.split(' '):
            words.append(line)
        while words[-1] == '':
            del words[-1]
        return len(words[-1]) # [-1]最後一個
do = Solution()
result = do.lengthOfLastWord(' fly me to the moon ')
print(result)