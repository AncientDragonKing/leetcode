class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        order = nums1[:m] + nums2[:n]
        order.sort() # 排序 sorted(order)也是排序，但它不會取代原本的清單
        return order
do = Solution()
result = do.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print(result)