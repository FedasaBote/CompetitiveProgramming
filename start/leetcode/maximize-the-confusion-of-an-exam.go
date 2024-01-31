func maxConsecutiveAnswers(answerKey string, k int) int {
    fals := findLongest(answerKey,"F",k)
    tru  := findLongest(answerKey,"T",k)
    
    if(fals>tru){
        return fals
    }
    
    return tru
    
}

func findLongest(answerKey,char string,k int) int{
    
    var left int =0
    maxlen := 0
    
    for r:=0; r<len(answerKey); r++{
        if string(answerKey[r])!=char{
            k--
        }
        if (k<0) {
            if string(answerKey[left])!=char{
                k++
            } 
            left++
        }
        
        if r-left+1>maxlen{
            maxlen = r-left+1
        }
    }
    
    return maxlen
}