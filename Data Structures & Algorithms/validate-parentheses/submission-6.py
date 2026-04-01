class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2 ==1):
            return False
        openedBrackets =[]
        
        for char in s:
            if char in ['(','{', '[']:
                openedBrackets.append(char)
                
            else:
                if(len(openedBrackets)==0):
                    return False
                lastOpened = openedBrackets.pop()
                if ( lastOpened =='{' and char !="}") or ( lastOpened=='(' and char !=")") or ( lastOpened=='[' and char !="]"):
                    return False
        return len(openedBrackets)==0



            
            
        