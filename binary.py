class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        c = int(a + b, 2) # int (, 2)表示轉換成十進位
        c = str(bin(c).lstrip('0b')) # 特別指明左邊的'0b'要去掉
        # change_a = []
        # change_b = []
        # for numbers in a:
        #     change_a.append(numbers)
        # for numbers in b:
        #     change_b.append(numbers)
        # ca = change_a[::-1] # 反轉清單
        # cb = change_b[::-1] # 反轉清單
        # count_a = None
        # count_b = None
        # for i, v in enumerate(ca):
        #     if count_a == None:
        #         count_a = str(int(v * (2 ** i)))
        #     else:
        #         count_a = str(count_a) + str(int(v * (2 ** i)))
        # for i, v in enumerate(cb):
        #     if count_b == None:
        #         count_b = str(int(v * (2 ** i)))
        #     else:
        #         count_b = str(count_b) + str(int(v * (2 ** i)))
        # c = count_a + count_b
        # binary = None
        # while c // 2 ==0:
        #     binary(str(c % 2))
        #     c = c // 2

        return c
test = Solution()
q_a = input('輸入: a = ')
q_b = input('輸入: b = ')
result = test.addBinary(q_a,q_b)
print(result)