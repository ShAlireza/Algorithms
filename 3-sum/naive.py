class Naive3Sum:
    """
    Naive approach:

        time complexity:
            O(n^3)
    """

    def __init__(self, numbers):
        self.numbers = numbers
        self._answer = self._3_sum_count()

    @property
    def answer(self):
        return self._answer

    def _3_sum_count(self):
        count = 0
        for i in range(len(self.numbers) - 2):
            for j in range(i + 1, len(self.numbers) - 1):
                for k in range(j + 1, len(self.numbers)):
                    if self.numbers[i] + self.numbers[j] + self.numbers[k]:
                        count += 1
        return count
