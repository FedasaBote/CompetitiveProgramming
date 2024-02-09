/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    
    var ans *ListNode = &ListNode{}
    var head *ListNode = ans
    for list1 != nil && list2 != nil{
        if list1.Val < list2.Val{
           
                ans.Next = list1
                ans = ans.Next
            list1 = list1.Next
        }else{
         
                ans.Next = list2
                 ans = ans.Next
            list2 = list2.Next
        }
    }
    
    for list1 != nil{
        ans.Next = list1
        list1 = list1.Next
         ans = ans.Next
    }
    for list2 != nil{
        ans.Next = list2
        list2 = list2.Next
         ans = ans.Next
    }
    
    return head.Next
}