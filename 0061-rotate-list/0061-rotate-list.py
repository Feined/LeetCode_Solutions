# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = head
        ln = 0
        while tail.next:
            ln+=1
            tail = tail.next
        ln+=1
        k = k%ln
        dum = head
        for i in range(ln-k-1):
            dum = dum.next
        
        tail.next = head
        head = dum.next
        dum.next = None

        return head