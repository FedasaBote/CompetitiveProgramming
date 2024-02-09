func maxScore(s string) int {
	n := len(s)
	prefixSum := make([]int, n)
	suffixSum := make([]int, n)
	ones := 0
	zeros := 0

	for i := 0; i < n; i++ {
		if s[i] == '0' {
			zeros++
		}
        prefixSum[i] = zeros
        suffixSum[n-1-i] = ones
		if s[n-1-i] == '1' {
			ones++
		}
	}
    

	ans := 0
	for j := 0; j < n-1; j++ {
		if prefixSum[j]+suffixSum[j] > ans {
			ans = prefixSum[j] + suffixSum[j]
		}
	}

	return ans
}