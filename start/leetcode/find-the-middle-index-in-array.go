func findMiddleIndex(nums []int) int {
    n := len(nums)
    prefix_sum := make([]int,n)
    suff_sum := make([]int,n)
    reversed_sum := 0
    sum := 0
    
    for i,v := range nums{
        prefix_sum[i] = sum
        suff_sum[n-1-i] = reversed_sum
        reversed_sum += nums[n-1-i]
        sum += v
    }
    
    index := n
    for i := 0; i<n ;i++ {
        if prefix_sum[i] == suff_sum[i]{
            index = i
            break
        }
    }
    
    if index ==n{
        return -1
    }
    
    return index
    
}