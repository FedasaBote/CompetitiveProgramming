function balancedString(s: string): number {
    const map = new Map<string,number>()
    map.set("Q", 0);
    map.set("W", 0);
    map.set("E", 0);
    map.set("R", 0);
    
    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        map.set(char,map.get(char)+1)
    }
    
    let left:number = 0;
    let result: number = s.length;
    let k:number = s.length / 4;
    
    for(let j=0; j<s.length; j++){
         let char = s[j];
         map.set(char,map.get(char)-1)
        
        while(left<s.length && map.get("Q")<=k && map.get("W")<=k && map.get("E")<=k && map.get("R")<=k){
            let chr = s[left]
            map.set(chr,map.get(chr)+1)
            result = Math.min(result,j-left+1)
            left++
        }
    }
    
    return result
    
};