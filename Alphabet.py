n= int(input("How many times do you want to check: "))

for i in range(n):
    ch = input("Please Enter a Character to Check: ")
    
    if((ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z')):
        print(ch, "is an Alphabet") 
        if (ch==A,a or ch==E,e or ch==I,i or ch==O,o or ch==U,u):
            print("It is an vowel")
        else:
            print("It is a Consonant")   
        
    elif(ch >= '0' and ch <= '9'):
       print(ch, "is a Digit")
    else:
       print(ch, "is a Special Character")
       
