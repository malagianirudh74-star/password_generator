#import the random module
import random

#import string module 
import string 

#create an empty string which will store the generated password 
password = ""

#input the no of characters that the password shall contain
length = int(input("Enter the Password length: "))

#If the password length is less than three characters it is not eligible to be a password 
#A password must contains minimum three characters
if length < 3:
    print("Invalid Password Length : specify length more than or equal to 3")
    
else:
    
    #within a atring called characters include: 
    #1. All the uppercase characters (A-Z)
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    i=1
    while i<=length :
        password = password + random.choice(characters)
        i = i+1
    print("Your generated Password is: ",password)    


