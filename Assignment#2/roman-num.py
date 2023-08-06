# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 05:57:21 2023

@author: ZUHA NADEEM
"""

values_of_roman={'I':1,"V":5,"X":10,"C":100,'L':50,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900};
roman=input("Enter a roman number:").upper();
len_of_roman=len(roman);
iterator=0;
integer=0;
while iterator<len_of_roman:
      if iterator==len_of_roman-1:
          integer+=values_of_roman[roman[iterator]] 
          break
      elif values_of_roman[roman[iterator]]<values_of_roman[roman[iterator+1]]:
          if roman[iterator]=='I':
              if roman[iterator+1]=='V':
                  integer+=values_of_roman['IV'];
                  iterator+=2;
              elif roman[iterator+1]=='X':
                  integer+=values_of_roman['IX'];
                  iterator+=2;
          elif roman[iterator]=='X':
                if roman[iterator+1]=='L':
                    integer+=values_of_roman['XL'];
                    iterator+=2;
                elif roman[iterator+1]=='C':
                    integer+=values_of_roman['XC'];
                    iterator+=2;
          elif roman[iterator]=='C':
                if roman[iterator+1]=='D':
                    integer+=values_of_roman['CD'];
                    iterator+=2;
                elif roman[iterator+1]=='M':
                    integer+=values_of_roman['CM'];
                    iterator+=2;
      else:
            integer+=values_of_roman[roman[iterator]];
            iterator+=1
          
print(integer)