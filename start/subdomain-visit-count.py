class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        ans =[]
        mp = {}
        
        for cpdomain in cpdomains:
            times,domains = cpdomain.split()

            domains = domains.split('.')[::-1]


            prev =""

            for i in domains:
                key = i + prev
                mp[key] = mp.get(key,0)+ int(times)
                prev="."+ i + prev
            
        for d in mp:
            ans.append(f"{mp[d]} {d}")
        return ans