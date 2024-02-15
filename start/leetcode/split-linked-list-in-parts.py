# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        res = [ListNode() for _ in range(k)]
        
        curr = head
        length = 0
        while curr:
            length +=1
            curr = curr.next
            
        qout = length //k
        rem = length % k
        if k> length:
            rem = 0
            qout = 1
        curr = head
        
        while curr:
            if not curr: break
            for node in res:
                if not curr: break
                newnode = node
                for i in range(qout):
                    if not curr: break
                    newnode.next = curr
                    curr = curr.next
                    newnode = newnode.next
                    newnode.next = None
                if rem:
                    newnode.next = curr
                    curr = curr.next
                    newnode = newnode.next
                    newnode.next = None
                    rem -= 1
        for idx,node in enumerate(res):
            res[idx] = node.next
            
        return res
        
                        
            
        