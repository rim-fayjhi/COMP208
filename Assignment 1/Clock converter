print('Welcome to Comp 208 time converter.') #This is the title.

twentyfour=int(input('Please enter the time to convert (hours only without minutes): ')) 
#The variable twentyfour corresponds to the input in 24H format, it is transformed into an integer so mathematical operations can be done to it later.

if(twentyfour>23 or twentyfour<0):
    print('The number is invalid') #When the number input isn't in between 0 to 23, a message is printed to let the user know their number is invalid.
    
elif(twentyfour>0 and twentyfour<10):#elif is else if; if the previous condition wasn't true then try the following.
    twelve=('0'+ str(twentyfour)) #twelve represents the number in 12H format, when the number in 12H and 24H format is the same, and is 1 digit, a '0' is added to the left for aesthetics.
    
elif(twentyfour>9 and twentyfour<13):
    twelve=(twentyfour) #Between 10 and 12, the number in 12H and 24H format is the same.
    
elif(twentyfour==0): #Double = to check if true.
     twelve=12 #0 is an exception to the minus 12 rule.
     
else: #This is for the numbers that weren't covered by the previous conditions:
    twelve= twentyfour-12 #This is the general rule for converting the 24H format to 12H.
    
    if(twelve<10):
        twelve = ('0'+str(twelve)) #Adding the digit '0' to the left for all single digit numbers for looks.
        
    print('You have entered',twentyfour,'in 24h mode. The equivalent in 12h mode is:',twelve) #Announcing the result of the conversion.
