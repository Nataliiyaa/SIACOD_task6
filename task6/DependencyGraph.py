from collections import defaultdict


class DependencyGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_dependency(self, parent, children):
        for child in children:
            self.graph[parent].append(child)

    def has_dependency(self, parent, child):
        if parent not in self.graph:
            return False
        return child in self.graph[parent]

    def clear(self):
        self.graph = defaultdict(list)

    def tarjan_algorithm(self):
        visited = set()
        recursion_stack = set()
        result = []

        def dfs(node):
            if node in recursion_stack:  # Если узел уже в текущем пути, это цикл
                raise Exception(f"Циклическая зависимость обнаружена: {node} уже в пути.")
            if node not in visited:
                visited.add(node)
                recursion_stack.add(node)

                for neighbor in self.graph.get(node, []):
                    dfs(neighbor)

                recursion_stack.remove(node)
                result.append(node)

        for node in self.graph:
            if node not in visited:
                dfs(node)

        return result
