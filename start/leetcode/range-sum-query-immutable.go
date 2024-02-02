type NumArray struct {
    nums []int
}


func Constructor(nums []int) NumArray {
    for i:=1;i<len(nums);i++{
        nums[i]+=nums[i-1]
    }
    return NumArray{
        nums:nums,
    }   
}


func (this *NumArray) SumRange(left int, right int) int {
    left-=1
    dec := 0
    if left>=0{
        dec = this.nums[left]
    }
    
    return this.nums[right] -dec
}


/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.SumRange(left,right);
 */