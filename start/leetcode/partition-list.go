/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func partition(head *ListNode, x int) *ListNode {
    less := &ListNode{}
    lessH := less
    great := &ListNode{}
    greatH := great
    
    curr := head
    for curr != nil{
        if curr.Val < x{
            less.Next = curr
            less = less.Next
        }else{
            great.Next = curr
            great = great.Next
        }
        curr = curr.Next
    }
    great.Next = nil
    less.Next = greatH.Next
    
    return lessH.Next
}