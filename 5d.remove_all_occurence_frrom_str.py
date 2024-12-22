def remove_all_occurence(string,char):
    modified_string=string.replace(char,'')
    print("original string:",string)
    print("modified string:",modified_string)
string=input("enter a string:")
char=input("enter the character you want to  remove from string:")    

remove_all_occurence(string,char)