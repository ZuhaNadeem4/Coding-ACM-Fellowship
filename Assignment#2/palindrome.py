input_str=input("Enter string:").lower();
len_str=len(input_str);
iterator=0;
filtered_str='';
while iterator<len_str:
    if ord(input_str[iterator])>=97 and ord(input_str[iterator])<=122:
          filtered_str+=input_str[iterator];
    iterator+=1;
reverse_str=filtered_str[::-1]
if reverse_str==filtered_str:
     print("'"+filtered_str+"' is a palindrome");
else:
    print("'"+filtered_str+"' is not a palindrome"); 
