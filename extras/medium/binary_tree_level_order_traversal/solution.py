class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []

        list = [[root.val]]

        def dfs(node: TreeNode, depth=1):
            if node is None:
                return

            vals = [n.val for n in [node.left, node.right] if n is not None]
            if depth == len(list) and len(vals) > 0:
                list.append([])

            if len(vals) > 0:
                list[depth] += vals

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root)

        return list
