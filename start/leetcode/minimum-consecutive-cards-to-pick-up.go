func minimumCardPickup(cards []int) int {
    times := map[int]int{}
    ans := len(cards)+1
    for idx,value := range cards{
        val, ok := times[value]
        if ok{
            ans = min(ans,idx-val + 1)
            times[value] = idx
        }else{
            times[value] = idx
        }
    }
    
    if ans!=len(cards)+1{
        return ans
    }
    
    return -1
}

func min(a,b int) int{
    if a<b{
        return a
    }
    return b
}