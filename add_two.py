
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 創建一個虛擬頭節點，簡化邊界處理
        dummy = ListNode(0)
        current = dummy
        carry = 0  # 進位
        
        # 當 l1 或 l2 還有節點，或者還有進位時繼續
        while l1 or l2 or carry:
            # 獲取當前位的值（正確的條件判斷）
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # 計算總和
            total = val1 + val2 + carry
            
            # 計算當前位的值和新的進位
            carry = total // 10
            digit = total % 10
            
            # 創建新節點
            current.next = ListNode(digit)
            current = current.next
            
            # 移動到下一個節點（安全檢查）
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        # 返回結果（跳過虛擬頭節點）
        return dummy.next

l1 = ListNode(2, ListNode(4, ListNode(3)))  # 342
l2 = ListNode(5, ListNode(6, ListNode(4)))  # 465

result = Solution().addTwoNumbers(l1, l2)

# 印出結果
while result:
    print(result.val, end=" -> " if result.next else "\n")
    result = result.next