func subarraysDivByK(nums []int, k int) int {
    
    
    totalSum := 0
    ans := 0
    remap := map[int]int{0:1}
    
    for r := 0; r <len(nums); r++{
        totalSum += nums[r]
        rem := totalSum % k
        if rem < 0{
            rem+=k
        }
        val, ok := remap[rem]
        if ok{
            ans += val
        }
        
        remap[rem]+=1
        
    }
    
    return ans
}