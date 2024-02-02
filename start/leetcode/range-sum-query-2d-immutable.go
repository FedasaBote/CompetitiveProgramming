type NumMatrix struct {
    nums [][]int
}


func Constructor(nums [][]int) NumMatrix {
    for i:=0; i<len(nums); i++{
        for j:=0; j<len(nums[0]); j++{
            if(i==0 && j==0){
                continue
            }else if(i==0){
                nums[i][j]+=nums[i][j-1]
            }else if(j==0){
                nums[i][j]+=nums[i-1][j]
            }else{
                nums[i][j]+=(nums[i][j-1]+nums[i-1][j]-nums[i-1][j-1])
            }
            
        }
    }
    
    return NumMatrix{
        nums:nums,
    }
}


func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    dec1 :=0
    dec2 :=0
    inc := 0
    if(row1>0){
        dec1 = this.nums[row1-1][col2]
    }
    if(col1>0){
        dec2 = this.nums[row2][col1-1]
    }
    if(row1>0 && col1>0){
        inc = this.nums[row1-1][col1-1]
    }
    ans := this.nums[row2][col2] - dec1 -dec2 + inc
    
    return ans
}


/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */