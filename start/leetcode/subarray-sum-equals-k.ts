function subarraySum(nums: number[], k: number): number {
    
    const map = new Map<number,number>();
    let count: number = 0
    let sum: number = 0
    map.set(0,1)
    
    
    for(let i=0;i<nums.length;i++){
        sum+=nums[i]
        if(map.has(sum-k)){
            count+=map.get(sum-k)
        }
        
        map.set(sum,(map.get(sum) || 0)+1)
        
    }
    
    return count
    
};