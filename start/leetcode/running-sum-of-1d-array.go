func runningSum(nums []int) []int {
    ans := []int{}
    prev_sum := 0
    for i := 0; i < len(nums); i++ {
        curr := prev_sum + nums[i]
        ans = append(ans, curr)
        prev_sum = curr
    }
    return ans
}