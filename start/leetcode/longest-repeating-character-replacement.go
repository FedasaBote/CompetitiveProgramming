func characterReplacement(s string, k int) int {
    map_ := map[byte]int{}
    maxCount := 0
    left := 0
    maxLength := 0
    
    for right := 0; right<len(s); right++{
        rightChar := s[right];
        map_[rightChar] ++;
        maxCount = max(maxCount,int(map_[rightChar]))
        
        for right - left + 1 - maxCount > k{
            leftChar := s[left]
            map_[leftChar] --
            
            if map_[leftChar] ==0{
                delete(map_,leftChar)
            }
            left++
        }
        
        maxLength = max(maxLength,right - left +1)
        
    }
    
    return maxLength
    
}

func max(a,b int) int {
    if a > b {
        return a
    }
    return b
}