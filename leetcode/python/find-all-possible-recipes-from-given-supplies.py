#!/usr/bin/env python3

""" Leetcode problem 2115: Find All Possible Recipes from Given Supplies. """

from collections import defaultdict, deque


class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        available = set(supplies)
        recipe_to_index = {recipe: i for i, recipe in enumerate(recipes)}
        dependencies = defaultdict(list)
        in_degree = [0] * len(recipes)
        for i, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                if ingredient not in available:
                    dependencies[ingredient].append(recipes[i])
                    in_degree[i] += 1
        queue = deque(i for i, count in enumerate(in_degree) if count == 0)
        result = []
        while queue:
            i = queue.popleft()
            recipe = recipes[i]
            result.append(recipe)
            for dependent in dependencies[recipe]:
                in_degree[recipe_to_index[dependent]] -= 1
                if in_degree[recipe_to_index[dependent]] == 0:
                    queue.append(recipe_to_index[dependent])
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
