func minWindow(s string, t string) string {
    targetDict := make(map[byte]int)
    for i := 0; i < len(t); i++ {
        targetDict[t[i]]++
    }
    
    left, right := 0, 0
    currDict := make(map[byte]int)
    found := 0
    minWindow := ""
    minLen := int(^uint(0) >> 1) // equivalent to float("inf")
    
    for right < len(s) {
        currChar := s[right]
        currDict[currChar]++
        
        if count, ok := targetDict[currChar]; ok && currDict[currChar] <= count {
            found++
        }
        
        for found == len(t) {
            if right-left+1 < minLen {
                minLen = right - left + 1
                minWindow = s[left : right+1]
            }
            
            currDict[s[left]]--
            if count, ok := targetDict[s[left]]; ok && currDict[s[left]] < count {
                found--
            }
            
            left++
        }
        
        right++
    }
    
    return minWindow
}