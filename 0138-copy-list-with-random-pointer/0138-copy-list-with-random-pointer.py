"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        1. Form a zig-zag pattern.
        2. Connect random to new LL.
        3. Seperate the links between both.
        '''
        temp = head
        while temp:
            chead = Node(temp.val)
            t = temp.next
            temp.next = chead
            chead.next = t
            temp = t
        temp = head
        ctemp = head.next
        while temp:
            if temp.random:
                ctemp.random = temp.random.next # .next = It must target copy list
            temp = temp.next.next
            if temp:
                ctemp = temp.next
        ans = head.next
        chead = ans
        while head:
            head.next = head.next.next
            head = head.next
            if chead.next:
                chead.next = chead.next.next  
                chead = chead.next
        return ans
        