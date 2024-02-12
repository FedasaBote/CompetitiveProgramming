/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseBetween(head *ListNode, left int, right int) *ListNode {
    temp := &ListNode{}
    
    temp.Next = head
    prev := temp
    for i := 0; i < left - 1; i++ {
        prev = prev.Next
    }
    
    present  := prev.Next
    for i := 0; i < right - left; i++{
        then := present.Next
        present.Next = then.Next
        then.Next = prev.Next
        prev.Next = then
    }
    
    return temp.Next
    
}