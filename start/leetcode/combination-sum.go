func combinationSum(candidates []int, target int) [][]int {
    ans := [][]int{}
    combo := []int{}

    helper(&ans, &combo, candidates, 0, target)
    return ans
}

func helper(ans *[][]int, combo *[]int, candidates []int, idx, target int) {
    if sum(*combo) == target {
        temp := make([]int, len(*combo))
        copy(temp, *combo)
        *ans = append(*ans, temp)
        return 
    }
    if sum(*combo) > target || idx == len(candidates) {
        return 
    }
    *combo = append(*combo, candidates[idx])
    helper(ans, combo, candidates, idx, target)
    *combo = (*combo)[:len(*combo)-1]
    helper(ans, combo, candidates, idx+1, target)
}

func sum(combo []int) int {
    s := 0
    for _, v := range combo {
        s += v
    }
    return s
}
