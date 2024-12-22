def replace_character(string,old_char,new_char):
    modified_string=string.replace(old_char,new_char)
    print("original string:",string)
    print("modified_string:",modified_string)
string=input("enter the string:")
old_char=input("enter the character you want to change:")
new_char=input("enter the character in place of old character")

replace_character(string,old_char,new_char)
