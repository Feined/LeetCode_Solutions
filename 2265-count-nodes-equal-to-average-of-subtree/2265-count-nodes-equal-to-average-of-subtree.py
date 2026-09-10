class Solution:
    def findsum(self,root,cnt):
        if root is None:
            return 0
        cnt[0]+=1
        lsum = self.findsum(root.left,cnt)
        rsum = self.findsum(root.right,cnt)
        return lsum+rsum+root.val
    def solve(self,root):
        if root is None:
            return 0
        cnt = [0]
        sm = self.findsum(root,cnt)
        if root.val == sm//cnt[0]:
            self.res+=1
        self.solve(root.left)
        self.solve(root.right)
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res=0
        self.solve(root)
        return self.res
        
        