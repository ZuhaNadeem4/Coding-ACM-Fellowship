braces_string=input("Enter string of braces:");
len_string=len(braces_string);
iterator=0;
while iterator<len_string:
    if braces_string[iterator]=='(' or braces_string[iterator]==')' or braces_string[iterator]=='{' or braces_string[iterator]=='}' or braces_string[iterator]=='[' or braces_string[iterator]==']':
        pass
    else:
        print("Enter valid string.")
        exit()
    iterator+=1
iterator2=0;
if len_string%2==0:
    while iterator2<len_string:
        if braces_string[iterator2]=='(':
            if braces_string[iterator2+1]==')':
                output='True'
                iterator2+=1
            else:
              output='False' 
        elif braces_string[iterator2]=='{':
            if braces_string[iterator2+1]=='}':
                output='True'
                iterator2+=1
            else:
              output='False'
        elif braces_string[iterator2]=='[':
            if braces_string[iterator2+1]==']':
                output='True'
                iterator2+=1
            else:
              output='False' 
        iterator2+=1
else:
    output='False'
print(output)
       
       