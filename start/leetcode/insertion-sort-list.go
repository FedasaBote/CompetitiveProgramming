/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertionSortList(head *ListNode) *ListNode {
    
    
    curr := head
    
    for curr != nil{
        temp := head
        
        for temp != curr{
            if temp.Val > curr.Val{
                swap(temp,curr)
            }
            temp = temp.Next
        }
        
        curr = curr.Next
    }
    
    return head
}

func swap(node1, node *ListNode){
    temp := node1.Val
    node1.Val = node.Val
    node.Val = temp
}