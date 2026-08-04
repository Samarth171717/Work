# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum=float('-inf')
        def dfs(node):
            nonlocal maxPathSum
            if not node:
                return 0

            leftGain=dfs(node.left)
            rightGain=dfs(node.right)

            leftGain=max(leftGain,0)
            rightGain=max(rightGain,0)

            maxPathSum=max(maxPathSum,leftGain+node.val+rightGain)
            return node.val+max(leftGain,rightGain)
        dfs(root)
        return maxPathSum
            