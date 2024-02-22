class Solution:
    def decodeString(self, s: str) -> str:

        def helper(idx,curr):
            tidx = idx
            if idx >= len(s) or s[idx] == "]":
                return curr,idx+1
            elif idx == len(s) -1:
                curr += s[idx]
                return curr,""
            elif s[idx] == "[":
                curr,tidx = helper(idx+1,curr)
            elif s[idx].isdigit():
                cn = s[idx]
                while s[idx+1].isdigit():
                    idx +=1
                    cn += s[idx]
                cidx = len(curr)
                curr,tidx = helper(idx+1,curr)
                pcurr = curr[:cidx]
                fcurr = curr[cidx:]*int(cn)
                curr,tidx = helper(tidx,pcurr+fcurr)
            else:
                curr = curr + s[idx]
                curr,tidx = helper(idx+1,curr)
            return curr,tidx

        return helper(0,"")[0]




        