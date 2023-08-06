input_str=input("Enter string:");
spaces_out=input_str.split(" ");
len_input=len(spaces_out);
len_last_word=len(spaces_out[len_input-1]);
print(len_last_word)
