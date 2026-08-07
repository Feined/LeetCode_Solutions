# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        queue = [(root,0,0)]
        front = 0
        mp = {}
        while front<len(queue):
            node,row,col = queue[front]
            front+=1
            if col not in mp:
                mp[col]=[]
            mp[col].append((row,node.val))
            if node.left:
                queue.append((node.left,row+1,col-1))
            if node.right:
                queue.append((node.right,row+1,col+1))
        ans = []
        for i in sorted(mp):
            mp[i].sort()
            temp = []
            for row,value in mp[i]:
                temp.append(value)
            ans.append(temp)

        return ans

        