class Solution(object):
    def __init__(self,s):
        self.s=s
    def isValid(self, s):
        len_string=len(s);
        iterator=0;
        while iterator<len_string:
            if s[iterator]=='(' or s[iterator]==')' or s[iterator]=='{' or s[iterator]=='}' or s[iterator]=='[' or s[iterator]==']':
                pass
            else:
                print("Enter valid string.")
                exit()
            iterator+=1
        iterator2=0;
        if len_string%2==0:
            while iterator2<len_string:
                if s[iterator2]=='(':
                    if s[iterator2+1]==')':
                        output='True'
                        iterator2+=1
                    else:
                      output='False' 
                elif s[iterator2]=='{':
                    if s[iterator2+1]=='}':
                        output='True'
                        iterator2+=1
                    else:
                      output='False'
                elif s[iterator2]=='[':
                    if s[iterator2+1]==']':
                        output='True'
                        iterator2+=1
                    else:
                      output='False' 
                iterator2+=1
        else:
            output='False'
        print(output)
class object:
    pass
s=input("Enter string of braces:");  
sol=Solution(s)
sol.isValid(s)    
       