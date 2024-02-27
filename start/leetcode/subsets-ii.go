// func subsetsWithDup(nums []int) [][]int {
    
// }
import (
    "sort"
)

func subsetsWithDup(nums []int) [][]int {
    sort.Ints(nums)
    ans := [][]int{}
    combo := []int{}
    helper(&ans, &combo, nums, 0)
    return ans
}

func helper(ans *[][]int, combo *[]int, nums []int, start int) {
    // Copy combo slice
    temp := make([]int, len(*combo))
    copy(temp, *combo)
    *ans = append(*ans, temp)

    for i := start; i < len(nums); i++ {
        if i > start && nums[i] == nums[i-1] {
            continue
        }
        *combo = append(*combo, nums[i])
        helper(ans, combo, nums, i+1)
        *combo = (*combo)[:len(*combo)-1]
    }
}
