func combine(n int, k int) [][]int {
    combo := []int{}
    ans := [][]int{}

    helper(1, &combo, &ans, k, n)
    return ans
}

func helper(idx int, combo *[]int, ans *[][]int, k, n int) {
    if len(*combo) == k {
        temp := make([]int, len(*combo))
        copy(temp, *combo)
        *ans = append(*ans, temp)
        return
    }

    for i := idx; i <= n; i++ {
        *combo = append(*combo, i)
        helper(i+1, combo, ans, k, n)
        *combo = (*combo)[:len(*combo)-1]
    }
}