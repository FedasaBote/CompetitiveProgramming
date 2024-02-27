func permute(nums []int) [][]int {
    
    used := make([]bool,len(nums))
    ans := [][]int{}
    combo := []int{}

    helper(&used,&ans,&combo,nums)
    return ans
}

func helper(used *[]bool,ans *[][]int,combo *[]int,nums []int){
    n := len(nums)
    if len(*combo) == n {
        temp := make([]int, len(*combo))
        copy(temp, *combo)
        *ans = append(*ans,temp)
        return
    }
    for i:=0; i<n; i++ {
        if !(*used)[i] {
            (*used)[i] = true
            *combo = append(*combo,nums[i])
            helper(used,ans,combo,nums)
            (*used)[i] = false
            *combo = (*combo)[:len(*combo)-1]
        }
    }
}