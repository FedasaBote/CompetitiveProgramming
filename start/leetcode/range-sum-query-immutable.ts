class NumArray {
    nums:number[]
    constructor(nums: number[]) {
        this.nums = nums
        
        for (let i=1;i<nums.length;i++){
            this.nums[i] += this.nums[i-1]
        }
    }

    sumRange(left: number, right: number): number {
       let dec =0
       if (left-1>=0){
           dec = this.nums[left-1]
       }
        return this.nums[right] -dec
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */