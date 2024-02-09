func minSubarray(nums []int, p int) int {
    totalSum := 0
    for _, num := range nums {
        totalSum += num
    }

    remainder := totalSum % p
    if remainder == 0 {
        return 0
    }

    result := len(nums)
    currentSum := 0
    seen := map[int]int{0: -1}

    for i, num := range nums {
        currentSum += num
        currentRemainder := currentSum % p
        targetRemainder := (currentSum - remainder + p) % p

        if idx, ok := seen[targetRemainder]; ok {
            result = min(result, i-idx)
        }

        seen[currentRemainder] = i
    }

    if result == len(nums) {
        return -1
    }
    return result
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}