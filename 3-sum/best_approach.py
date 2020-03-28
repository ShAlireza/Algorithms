class Best3Sum:
    """
    Best approach:
        This only works on arrays with distinct elements

        time complexity:
            O(n^2)
    """

    def __init__(self, numbers):
        self.numbers = sorted(numbers)
        self._answer = self._3_sum_count()

    @property
    def answer(self):
        return self._answer

    def _3_sum_count(self):
        count = 0
        for i in range(len(self.numbers) - 2):
            left = i + 1
            right = len(self.numbers) - 1
            while left < right:
                if self.numbers[i] + self.numbers[left] + self.numbers[right] \
                        == 0:
                    count += 1
        return count
