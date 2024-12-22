def swap_first_n_chars(string1,strig2,n):
    new_string1=string2[:n]+string1[n:]
    new_string2=string1[:n]+string2[n:]
    print('string1:',new_string1)
    print("string2:",new_string2)
string1=input("enter first string:")
string2=input("enter second string:")
n=int(input("enter number of characters you want to swap;"))    

swap_first_n_chars(string1,string2,n)