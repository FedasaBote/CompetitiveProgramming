class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def product(arg1,arg2,arg3):
            if arg1=="+":
                return int(int(arg2)+int(arg3))
            elif arg1=="*":
                return int(int(arg2)*int(arg3))
            elif arg1=="/":
                return int(int(arg3)/int(arg2))
            elif arg1=="-":
                return int(int(arg3)-int(arg2))
        operations=["-","/","*","+"]
        ans=[]
        for i in range(len(tokens)):
            if tokens[i] in operations:
                arg1=ans.pop()
                arg2=ans.pop()
                val=product(tokens[i],arg1,arg2)
                ans.append(str(val))
            else:
                ans.append(tokens[i])
        return int(ans[0])