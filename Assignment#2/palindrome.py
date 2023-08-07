class Solution(object):
    def __init__(self,s):
        self.s=s
    def isPalindrome(self, s):
        len_str=len(s);
        iterator=0;
        filtered_str='';
        while iterator<len_str:
            if ord(s[iterator])>=97 and ord(s[iterator])<=122:
                  filtered_str+=s[iterator];
            iterator+=1;
        reverse_str=filtered_str[::-1]
        if reverse_str==filtered_str:
             print("'"+filtered_str+"' is a palindrome");
        else:
            print("'"+filtered_str+"' is not a palindrome"); 
class object:
    pass

s=input("Enter string:").lower();
sol=Solution(s)
sol.isPalindrome(s)