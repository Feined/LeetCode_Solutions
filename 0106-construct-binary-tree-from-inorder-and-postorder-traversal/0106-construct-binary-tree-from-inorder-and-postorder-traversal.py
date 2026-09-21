# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findpos(self,k,inorder,low,high):
        for i in range(low,high+1):
            if inorder[i]==k:
                return i
        return -1
    def create(self,inorder,postorder,low,high,idx):
        if low>high:
            return None
        root = TreeNode(postorder[idx[0]])
        idx[0]-=1
        pos = self.findpos(root.val,inorder,low,high)
        root.right = self.create(inorder,postorder,pos+1,high,idx)
        root.left = self.create(inorder,postorder,low,pos-1,idx)
        return root
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        n = len(postorder)
        idx = [n-1]
        return self.create(inorder,postorder,0,n-1,idx)
    