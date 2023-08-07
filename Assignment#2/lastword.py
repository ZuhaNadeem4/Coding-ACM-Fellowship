class Solution(object):
    def __init__(self,s):
        self.s=s
    def lengthOfLastWord(self, s):
        spaces_out=s.split(" ");
        len_input=len(spaces_out);
        len_last_word=len(spaces_out[len_input-1]);
        print(len_last_word)
class object:
    pass

s=input("Enter string:");
sol=Solution(s)
sol.lengthOfLastWord(s)