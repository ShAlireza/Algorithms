class QuickFindUF:
    """
    Quick Find approach
        time complexities:
            connected: O(1)
            union: O(n)

        worst-case time with M union-find operations on a set of N objects:
            M N

    """

    def __init__(self, size):
        self.ids = [_ for _ in range(size)]

    def connected(self, p, q):
        return self.ids[p] == self.ids[q]

    def union(self, p, q):
        for index in self.ids:
            if self.ids[index] == self.ids[p]:
                self.ids[index] = self.ids[q]
