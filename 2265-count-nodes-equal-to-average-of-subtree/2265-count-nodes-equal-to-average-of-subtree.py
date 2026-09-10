class Solution:
    ''' Approach - 1
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
    '''
    # Approach - 2
    def averageOfSubtree(self, root: TreeNode) -> int:
        # self.res=0
        # self.solve(root)
        # return self.res
        count = 0
        def dfs(root):
            nonlocal count
            if not root:
                return 0,0
            lsum,lcnt = dfs(root.left)
            rsum,rcnt = dfs(root.right)

            totalsum = lsum+rsum+root.val
            totalcnt = lcnt+rcnt+1

            if totalsum//totalcnt == root.val:
                count+=1
            return totalsum,totalcnt
        dfs(root)
        return count

        
        