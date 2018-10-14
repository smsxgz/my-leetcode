class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        if n == 0 or n == 1:
            return 0
        nodes = dict((i, 1 << i) for i in range(n))
        end = (1 << n) - 1

        states = set((i, nodes[i]) for i in range(n))
        queue = [(i, 0, nodes[i]) for i in range(n)]
        while queue:
            node, depth, visited = queue.pop(0)
            depth += 1
            for next_node in graph[node]:
                new_visited = visited | nodes[next_node]
                if new_visited == end:
                    return depth
                if (next_node, new_visited) not in states:
                    states.add((next_node, new_visited))
                    queue.append((next_node, depth, new_visited))


if __name__ == '__main__':
    s = Solution()
    s.shortestPathLength([[1, 2, 3], [0], [0], [0]])
    s.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]])
