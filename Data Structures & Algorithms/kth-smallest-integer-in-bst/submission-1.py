# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int):
        res =root.val
        cnt=k
        def inorder(node):
            nonlocal cnt,res
            if node:
                inorder(node.left)     # Step 1: Go left
                cnt-=1
                if cnt==0:
                    res =node.val       # Step 2: Visit node
                    return
                inorder(node.right) 
        inorder(root)
        return res