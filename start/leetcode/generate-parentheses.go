func generateParenthesis(n int) []string {
    ans := []string{}
    stack := []string{}
    helper(&ans,&stack,n,0,0)
    return ans
}

func helper(ans *[]string, stack *[]string,n,open,close int){
    if open == n && close == n {
        *ans = append(*ans,strings.Join(*stack,""))
    }

    if  open < n {
        *stack = append(*stack,"(")
        helper(ans,stack,n,open+1,close)
        *stack = (*stack)[:len(*stack)-1]
    }

    if close < open {
        *stack = append(*stack,")")
        helper(ans,stack,n,open,close+1)
        *stack = (*stack)[:len(*stack)-1]
    }
}