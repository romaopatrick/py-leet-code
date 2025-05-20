
# 0. Clone Graph: https://leetcode.com/problems/clone-graph/description/
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []
    
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None

        visited = {}

        def copy(n):
            if n in visited:
                return visited[n]
            
            clone = Node(n.val)
            visited[n] = clone
            for neighbor in n.neighbors:
                clone.neighbors.append(copy(neighbor))
            return clone

        return copy(node)