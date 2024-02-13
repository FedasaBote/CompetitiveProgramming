/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
    
    fast := head
    slow := head
    
    for {
        if fast==nil || fast.Next == nil || fast.Next.Next == nil{
            return nil
        }
        fast = fast.Next.Next
        slow = slow.Next
        
        if slow == fast{
            break
        }
    }
    
    slow = head
    
    for slow != fast {
        slow = slow.Next
        fast = fast.Next
    }
    
    return slow
}