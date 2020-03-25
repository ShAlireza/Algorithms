class QuickUnionImprovedUF:
    """
    improvement 1:
        Use weighted trees

        trees size as their weights
        while make unions from trees, attach smaller one to bigger one
        time complexities:
            connected: O(log(n))
            union: O(1)

    improvement 2:
        Path compression

        while finding roots of a node , set every node parent to its parent of parent

    worst-case time with M union-find operations on a set of N objects:
            Weighted quick_union: N + M log N
            Path compression quick_union: N + M log N
            Weighted path compression quick_union: N + M log* N

    """

    def __init__(self, size):
        self.ids = [_ for _ in range(size)]
        self.weights = [1 for _ in range(size)]

    def _root(self, i):
        while self.ids[i] != i:
            self.ids[i] = self.ids[self.ids[i]]  # Path compression code
            i = self.ids[i]
        return i

    def connected(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        p_root = self._root(p)
        q_root = self._root(q)
        if self.weights[p_root] < self.weights[q_root]:
            self.ids[p_root] = q_root
            self.weights[q_root] += self.weights[p_root]
        else:
            self.ids[q_root] = p_root
            self.weights[p_root] += self.weights[q_root]
