from typing import Any
import queue
import collections

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        answer, q = [self._root], collections.deque()
        q.append(self._root)
        use = {self._root}
        while q:
            now = q[0]
            flag = True
            for nod in now.outbound:
                if nod not in use:
                    q.appendleft(nod)
                    answer.append(nod)
                    use.add(nod)
                    flag = False
                    break
            if flag:
                q.popleft()
        return answer

    def bfs(self) -> list[Node]:
        answer, q = [], queue.Queue()
        q.put(self._root)
        use = {self._root}
        while not q.empty():
            now = q.get()
            answer.append(now)
            for nod in now.outbound:
                if nod not in use:
                    q.put(nod)
                    use.add(nod)

        return answer


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(d)
a.point_to(c)
g = Graph(a)

print(g.dfs())
