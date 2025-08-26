class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        numbers = digits.copy()
        numbers[-1] += 1
        numbers = numbers[::-1]
        for i, num in enumerate(numbers):
            if num == 10:
                if i+1 == len(numbers):
                    numbers.append(1)
                    numbers[i] = 0
                    break
                numbers[i+1] += 1
                numbers[i] = 0

        return numbers[::-1]


solution = Solution()
print(solution.plusOne([9, 9, 9]))