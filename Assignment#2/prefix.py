# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 20:42:27 2023

@author: ZUHA NADEEM
"""

list_of_strings=[];
no_of_strings=int(input("How many strings do you want to enter:"));
iterator1=0;
while iterator1<no_of_strings:
    string=input("Enter string:");
    list_of_strings.append(string);
    iterator1+=1;
iterator2=0;
len_of_strings=[]
while iterator2<no_of_strings:
    len_of_strings.append(len(list_of_strings[iterator2]))
    iterator2+=1;
iterator3=0
min_len=min(len_of_strings)
common='';
iterator4=0
while iterator4<min_len-1:
    if list_of_strings[0][iterator4]== list_of_strings[1][iterator4]:
        common+=list_of_strings[0][iterator4]
    iterator4+=1
iterator5=0;
common_str=common;
while iterator5<no_of_strings-2:
    iterator6=0;
    while iterator6<len(common):
        if common[iterator6]==list_of_strings[iterator5+2][iterator6]:
            common_str=common
        else:
            common_str==""
        iterator6+=1
    iterator5+=1
if common==""  :
    print("There's no common prefix")
else:
    print("The common prefix is '"+ common+"'");
    
