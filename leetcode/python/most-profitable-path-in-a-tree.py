#!/usr/bin/env python3

""" Leetcode problem 2467: Most Profitable Path in a Tree. """


class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        n = len(amount) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        bob_time = [n] * n

        def bob_path(node: int, prev: int, time: int) -> bool:
            if node == 0:
                bob_time[node] = time
                return True
            for next_node in graph[node]:
                if next_node != prev and bob_path(next_node, node, time + 1):
                    bob_time[node] = time
                    return True
            return False
        bob_path(bob, -1, 0)
        max_income = float('-inf')

        def alice_path(node: int, prev: int, time: int, income: int) -> None:
            if time < bob_time[node]:
                income += amount[node]
            elif time == bob_time[node]:
                income += amount[node] // 2
            if node != 0 and len(graph[node]) == 1:
                nonlocal max_income
                max_income = max(max_income, income)
                return
            for next_node in graph[node]:
                if next_node != prev:
                    alice_path(next_node, node, time + 1, income)
        alice_path(0, -1, 0, 0)
        return max_income


def main() -> None:
    pass


if __name__ == "__main__":
    main()
