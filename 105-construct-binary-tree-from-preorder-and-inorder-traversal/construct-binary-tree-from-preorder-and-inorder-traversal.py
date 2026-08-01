# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIndex=0
        def build(inLeft,inRight):
            nonlocal preIndex
            if inLeft>inRight:
                return None 
            value=preorder[preIndex]
            preIndex+=1
            rootIndex=inorder.index(value)
            root=TreeNode(value)
          
            root.left=build(inLeft,rootIndex-1)
            root.right=build(rootIndex+1,inRight)
            return root
        return build(0, len(inorder)-1)