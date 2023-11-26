# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # 1) reach node at position "left"
        leftPrev, curr = dummy, head
        for i in range(left - 1):
            leftPrev, curr = curr, curr.next
            
        # Now curr="left", leftPrev="node before left"
        # 2) reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = curr.next
            curr.next = prev
            prev, curr = curr, tmpNext
            
        # 3) Update pointers 
        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummy.next