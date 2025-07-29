class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping: # 右括號
                # 取出棧頂元素，如果棧為空，則使用一個佔位符（例如'#'）
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False, top_element
            else: #左括號
                stack.append(char)
        return True, stack


test = Solution()
result = test.isValid('[{]}')
print(result)