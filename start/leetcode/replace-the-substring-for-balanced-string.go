func balancedString(s string) int {
    count := make([]int, 128)
    n := len(s)
    res := n
    k := n / 4
    i := 0

    for j := 0; j < n; j++ {
        count[s[j]]++
    }

    for j := 0; j < n; j++ {
        count[s[j]]--
        for i < n && count['Q'] <= k && count['W'] <= k && count['E'] <= k && count['R'] <= k {
            res = min(res, j-i+1)
            count[s[i]]++
            i++
        }
    }
    return res
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
