func countCompleteSubarrays(nums []int) int {
    map_ := map[int]int{}
    
    for i := 0 ;i<len(nums);i++{
        map_[nums[i]] +=1
    }
    
    whole :=  len(map_)
    map_ = map[int]int{}
    l := 0
    c := 0
    
    for i := 0 ;i<len(nums);i++{
        map_[nums[i]]++
        
        for len(map_) == whole{
            map_[nums[l]]--
            
            if map_[nums[l]] == 0{
                delete(map_,nums[l])
            }
            
            l++
        }
        
        c+=l
    }
    
    return c
}