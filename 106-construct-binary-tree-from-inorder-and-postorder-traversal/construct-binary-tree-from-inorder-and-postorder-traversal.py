# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postindex=len(postorder)-1

        def build(inLeft,inRight):
            nonlocal postindex
            if inLeft>inRight:
                return None

            value=postorder[postindex]
            postindex-=1
            rootIndex=inorder.index(value)
            root=TreeNode(value)
            root.right=build(rootIndex+1,inRight)
            root.left=build(inLeft,rootIndex-1)
            return root
        return build(0,len(inorder)-1)