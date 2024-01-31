function minSubArrayLen(target: number, nums: number[]): number {
    
    let count:number = Infinity;
    let sum:number =0
    let left:number =0
    
    for(let right=0;right<nums.length;right++){
        sum+=nums[right];
        while(sum>=target){
            
            count = Math.min(right-left+1,count)
            sum-=nums[left];
            left+=1
        }
       
        
    }
    
    return count == Infinity ? 0:count
};