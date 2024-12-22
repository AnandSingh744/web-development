def remove_first_occurence(string,char):
    modified_string=string.replace(char,'',1)
    print("original string:",string)
    print("modified string:",modified_string)
string=input("enter a string:")
char=input("enter the character you want to remove:")

remove_first_occurence(string,char)