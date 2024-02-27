class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = Counter(s)
        res = []

        i = 0
        b = {}
        prev = 0
        while i < len(s):
            if s[i] in b:
                mp[s[i]]-=1
                if mp[s[i]] == 0:
                    prev -= 1
                b[s[i]]+=1
            elif prev == 0 and len(b)>0:
                res.append(sum(b.values()))
                b = {}
                continue
            else:
                b[s[i]] = 1
                mp[s[i]] -=1
                if mp[s[i]] !=0:
                    prev += 1

            i+=1
        if len(b) >0:
            res.append(sum(b.values()))
        return res

        