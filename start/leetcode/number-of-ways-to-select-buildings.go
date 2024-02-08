func numberOfWays(s string) int64 {
    n := len(s)
    prezo := make([]int,n)
    preoz := make([]int,n)
    ones := 0
    zeros := 0
    
    for idx, char := range s {
        if char == '0'{
            zeros += 1
            preoz[idx] = ones
        }
        if char == '1'{
            ones += 1
            prezo[idx] = zeros
        }
    }
    
    for i := 1; i < n; i++ {
        preoz[i] += preoz[i-1]
        prezo[i] += prezo[i-1]
    }
    
    var res int64 = 0
    
    for idx ,char := range s{
        if char == '0'{
            res += int64(prezo[idx])
        }
        if char =='1'{
            res += int64(preoz[idx])
        }
    }
    
    return res
}