class QuickFindUF:

    def __init__(self, size):
        self.ids = [_ for _ in range(size)]

    def _root(self, i):
        while self.ids[i] != i:
            i = self.ids[i]
        return i

    def connected(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        p_root = self._root(p)
        q_root = self._root(q)
        self.ids[p_root] = q_root
