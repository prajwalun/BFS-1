# The levelOrder method performs a level-order traversal of a binary tree using depth-first search (DFS).
# It returns a list of lists, where each inner list contains the values of nodes at a specific depth.

# Helper Function (dfs):
#   - Recursively traverses the tree, visiting nodes level by level.
#   - Parameters:
#       - 'node': The current node being processed.
#       - 'depth': The current depth of the traversal.
#   - Base Case:
#       - If the current node is None, return as there are no further nodes to process.
#   - If the current depth equals the length of 'res', append a new list to 'res' to store values for this depth.
#   - Add the current node's value to the list corresponding to its depth.
#   - Recursively call dfs on the left and right children, incrementing the depth by 1.

# Main Execution:
#   - Initialize 'res' as an empty list to store the result.
#   - Call the dfs function starting from the root at depth 0.
#   - Return 'res', which contains the values of nodes grouped by depth.

# TC: O(n) - Each node is visited once, making the time complexity linear with the number of nodes.
# SC: O(h) - The space complexity is proportional to the height of the tree due to the recursion stack.



from typing import Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res