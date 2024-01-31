func minimumRecolors(blocks string, k int) int {
 
    var white int = 0
    left := 0
    ans := len(blocks)
    
    for i:=0; i<len(blocks); i++ {
        if string(blocks[i])=="W"{
            white++
        }
        
        if i >= k -1{
            if white<ans{
                ans = white
            }
            if string(blocks[left])=="W"{
                white--
            }
            
            left++
        }
    }
    
    return ans
}