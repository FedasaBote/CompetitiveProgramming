/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthSmallest(root *TreeNode, k int) int {
   _,v := helper(root,k)

   return v
}

func helper(root *TreeNode, k int) (int, int) {
    if root == nil {
        return 0, -1
    }

    cl, val := helper(root.Left, k)
    if val != -1 {
        return cl, val
    }
    if cl == k-1 {
        return cl, root.Val
    }

    cr, v := helper(root.Right, k-cl-1)
    return cl + cr + 1, v
}