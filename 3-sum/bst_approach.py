class Bst3Sum:
    """
    BST approach:
            First sort numbers list in ascending order
            a + b + c = 0
            find third number -(a + b) with binary search
            algorithm.

            time complexity:
                O(n^2 * log n)
    """

    def __init__(self, numbers):
        self.numbers = sorted(numbers)
        self._answer = self._3_sum_count()

    @property
    def answer(self):
        return self._answer

    def _3_sum_count(self):
        count = 0
        for i in range(len(self.numbers) - 1):
            for j in range(i + 1, len(self.numbers)):
                if self._binary_search(self.numbers, key=-(i + j)):
                    count += 1
        return count

    @staticmethod
    def _binary_search(numbers, key, left=-1, right=-1):
        if left == -1:
            left = 0
        if right == -1:
            right = len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] < key:
                left = mid + 1
            elif numbers[mid] > key:
                right = mid - 1
            else:
                return True
        return False
