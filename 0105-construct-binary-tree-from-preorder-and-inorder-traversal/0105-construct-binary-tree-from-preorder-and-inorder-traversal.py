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
    def create(self,preorder,inorder,low,high,idx):
        if low>high:
            return None
        root = TreeNode(preorder[idx[0]])
        idx[0]+=1
        pos = self.findpos(root.val,inorder,low,high)
        root.left = self.create(preorder,inorder,low,pos-1,idx)
        root.right = self.create(preorder,inorder,pos+1,high,idx)
        return root
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        root = None
        idx = [0]
        low = 0
        n = len(preorder)
        high = n-1
        return self.create(preorder,inorder,low,high,idx)
        # self.post(root)
    