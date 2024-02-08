# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def reverse(head):
            if not head or not head.next:
                return head,head
            
            prev,first = reverse(head.next)
            prev.next = head
            head.next = None
            return head,first
        
        return reverse(head)[1]
        