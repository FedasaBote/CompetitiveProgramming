func maxSubArray(nums []int) int {
    
    total := 0
    ans := int(math.Inf(-1))
    
    for i := 0; i< len(nums); i++{
        total += nums[i]
        ans = max(ans,total)
        
        if total < 0 {
            total = 0
        }
        
    }
    
    return ans
}

func max(a,b int) int{
    if a >b{
        return a
    }
    
    return b
}