
func canJump(nums []int) bool {
	memo := make(map[int]bool)

	var helper func(int) bool
	helper = func(index int) bool {
		if index == len(nums)-1 {
			return true
		}
		if val, ok := memo[index]; ok {
			return val
		}
		for j := nums[index]; j > 0; j-- {
			if index+j > len(nums)-1 {
				continue
			}
			res := helper(index+j)
			memo[index+j] = res
			if res {
				return true
			}
		}
		memo[index] = false
		return false
	}

	return helper(0)
}

