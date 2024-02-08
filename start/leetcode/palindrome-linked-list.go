/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    if head == nil || head.Next == nil {
        return true
    }
    
    slow := head
    fast := head

    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }

    reversed := reverse(slow)
    copy := reversed

    for head != nil && reversed != nil {
        if head.Val != reversed.Val {
            return false
        }
         
        head = head.Next
        reversed = reversed.Next
    }

    reverse(copy)
    if head == nil || reversed == nil {
        return true
    }
       
    return false
}

func reverse(head *ListNode) *ListNode {
    var prev, next *ListNode
    curr := head
    
    for curr != nil {
        next = curr.Next
        curr.Next = prev
        prev = curr
        curr = next
    }
    
    return prev
}