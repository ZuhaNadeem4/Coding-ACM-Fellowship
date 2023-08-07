# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 05:57:21 2023

@author: ZUHA NADEEM
"""

values_of_s={'I':1,"V":5,"X":10,"C":100,'L':50,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900};
class Solution(object):
    def __init__(self,s):
        self.s=s
    def romanToInt(self, s):
        len_of_s=len(s);
        iterator=0;
        integer=0;
        while iterator<len_of_s:
              if iterator==len_of_s-1:
                  integer+=values_of_s[s[iterator]] 
                  break
              elif values_of_s[s[iterator]]<values_of_s[s[iterator+1]]:
                  if s[iterator]=='I':
                      if s[iterator+1]=='V':
                          integer+=values_of_s['IV'];
                          iterator+=2;
                      elif s[iterator+1]=='X':
                          integer+=values_of_s['IX'];
                          iterator+=2;
                  elif s[iterator]=='X':
                        if s[iterator+1]=='L':
                            integer+=values_of_s['XL'];
                            iterator+=2;
                        elif s[iterator+1]=='C':
                            integer+=values_of_s['XC'];
                            iterator+=2;
                  elif s[iterator]=='C':
                        if s[iterator+1]=='D':
                            integer+=values_of_s['CD'];
                            iterator+=2;
                        elif s[iterator+1]=='M':
                            integer+=values_of_s['CM'];
                            iterator+=2;
              else:
                    integer+=values_of_s[s[iterator]];
                    iterator+=1
        print(integer)
class object:
    pass
s=input("Enter a s number:").upper();
sol=Solution(s)
sol.romanToInt(s)