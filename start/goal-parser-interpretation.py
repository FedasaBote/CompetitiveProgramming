class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res =""


        for i in range(len(command)):

            if command[i] =="G":
                res+="G"
            elif command[i]==")" and command[i-1]=='(':
                res+='o'

            elif command[i]==')':
                res+='al'


        return res