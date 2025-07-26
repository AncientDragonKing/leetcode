class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0 # 總和
        prev_value = 0
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        for char in reversed(s):
            """
            :char 字元
            :reverse() '字串'反轉 
            """

            current_value = roman_map[char] # current 目前的
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        return total

        
test = Solution()
result = test.romanToInt('IL')
print(result)
