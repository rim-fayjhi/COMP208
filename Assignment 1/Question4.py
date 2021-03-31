print('Welcome to the password obfuscation program.') #This introduces the program.

name=input('Please enter your name: ') #The name of the user is a string, it is a variable because the program needs to remember it for later use.
password=input('Please enter a password: ') #The user enters their password here, it's remembered as a string.

print('Welcome',name)

password_length=len(password) #This counts the number of characters in the password.
print('Your password has',password_length,'letters') #Tells the user how many characters their pw has.

if password_length<8: #If the password is 7 characters or shorter, a warning message follows.
    print('Your password has less than 8 characters. We recommend at least 8') 
    print('characters for the safety of your account.')
    
print('This is your obfuscated password: ',password[0],(password_length-2)*'#',password[password_length-1],sep='') 
#This prints only the first and the last character of the password and puts ##s in between to represent the other hidden characters. sep=''is there in order to remove the space between the first and last letter and the ##s.
 