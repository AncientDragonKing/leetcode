class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        # 使用滑動窗口法
        char_map = {}  # 記錄字符最後出現的位置
        left = 0  # 窗口左邊界
        max_length = 0  # 最長子串長度
        
        for right in range(len(s)):
            char = s[right]

            # 如果字符已經在當前窗口中出現過
            if char in char_map and char_map[char] >= left:
                # 移動左邊界到重複字符的下一個位置
                left = char_map[char] + 1
            
            # 更新字符的最新位置
            char_map[char] = right
            
            # 更新最大長度
            max_length = max(max_length, right - left + 1)
        
        return max_length


if __name__ == "__main__":
    solution = Solution()
result = solution.lengthOfLongestSubstring('abcabcbb')
print(result)