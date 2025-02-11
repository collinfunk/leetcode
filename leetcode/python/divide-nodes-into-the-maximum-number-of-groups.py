#!/usr/bin/env python3

""" Leetcode problem 2493: Divide Nodes Into the Maximum Number of Groups. """

from collections import defaultdict, deque


class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def is_bipartite(start: int) -> bool:
            color = {}
            queue = deque([start])
            color[start] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in color:
                        if color[neighbor] == color[node]:
                            return False
                    else:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
            return True

        def max_groups(start: int) -> int:
            visited = set()
            queue = deque([(start, 1)])
            visited.add(start)
            max_level = 1
            while queue:
                node, level = queue.popleft()
                max_level = max(max_level, level)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
            return max_level

        visited = set()
        total_groups = 0
        for node in range(1, n + 1):
            if node not in visited:
                if not is_bipartite(node):
                    return -1
                component_nodes = set()
                queue = deque([node])
                component_nodes.add(node)
                while queue:
                    current = queue.popleft()
                    for neighbor in graph[current]:
                        if neighbor not in component_nodes:
                            component_nodes.add(neighbor)
                            queue.append(neighbor)
                max_component_groups = 0
                for start_node in component_nodes:
                    max_component_groups = max(
                        max_component_groups, max_groups(start_node))
                total_groups += max_component_groups
                visited.update(component_nodes)
        return total_groups


def main() -> None:
    pass


if __name__ == "__main__":
    main()
