def character_frequency(string,char):
    frequency=string.count(char)
    print("the charactr",char,"appears",frequency,"times in the string")
string=input("enter the string:")
char=input("enter the character to find its frequency:")

character_frequency(string,char)     