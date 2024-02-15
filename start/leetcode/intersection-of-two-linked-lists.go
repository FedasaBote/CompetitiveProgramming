/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    
    set := map[*ListNode]int{}
    
    for headA != nil {
        set[headA] = 1
        headA= headA.Next
    }
    
    for headB != nil{
        _,ok := set[headB]
        if ok {
            return headB
        }
        headB = headB.Next
    }
    
    return nil
}