def check_character(char):
    if char.isalpha():
        print(char,"is a letter")
        if char.isupper():
            print(char,"is a an uppercase letter")
        else:
            print(char,"is a lowercase letter")
    elif char.isdigit():
        print(char,"is a digit")
        digit_names={'0':"zero",'1':"one",'2':"two",'3':"three",'4':"four",
                     '5':"five",'6':"six",'7':"seven",'8':"eight",'9':"nine"}
        print(char,"is witten in letter as ",digit_names[char])
    else:
        print(char,"is a special character")
char=input("enter a character: ")
check_character(char)        

                   