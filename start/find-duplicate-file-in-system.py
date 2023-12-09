class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        ans =[]
        mp = {}
        
        for path in paths:
            dr,*rest = path.split()
        
            for files in rest:
                file, content = files.split("(")
                content = content[:-1]
                
                if content in mp:
                    mp[content].append(dr+"/"+file)
                else:
                    mp[content]=[]
                    mp[content].append(dr+"/"+file)
                    
                
        for path in mp:
            if len(mp[path])>1:
                ans.append(mp[path])
                
        return ans
        