func minimumSteps(s string) int64 {
    
    var c int64 = 0
    var ones int64 = 0
    
    for i := 0 ;i < len(s);i++{
        if s[i] =='1'{
            ones += 1
        }
        if s[i] =='0'{
            c += ones
        }
    }
    
    return c
}