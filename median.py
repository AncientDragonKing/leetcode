class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 確保 nums1 是較短的數組，這樣可以減少二分搜索的範圍
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            # 在 nums1 中的分割點
            partition1 = (left + right) // 2
            # 在 nums2 中的分割點，確保左半部分的總長度是 (m+n+1)//2
            partition2 = (m + n + 1) // 2 - partition1
            
            # 找到分割點左右兩側的元素
            # 如果分割點在邊界，使用負無窮大或正無窮大
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]
            
            # 檢查是否找到了正確的分割點
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # 找到了正確的分割點
                if (m + n) % 2 == 0:
                    # 總長度是偶數，中位數是中間兩個數的平均值
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
                else:
                    # 總長度是奇數，中位數是左半部分的最大值
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                # nums1 的左半部分太大，需要向左移動分割點
                right = partition1 - 1
            else:
                # nums1 的左半部分太小，需要向右移動分割點
                left = partition1 + 1
        
        # 理論上不會到達這裡，因為輸入保證是有效的
        return 0.0

if __name__ == '__main__':
    solution = Solution()
result = solution.findMedianSortedArrays([1, 2], [3, 4])
print(result)