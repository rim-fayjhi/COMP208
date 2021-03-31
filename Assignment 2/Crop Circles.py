#Hello class, I hope that you are enjoying this class! :)
print('') #For readability
print('Welcome to the Text Analyser')
my_text=input('Please enter your text: ')#the user inputs their text here and is remembered as 'my_text'
print('')

is_lowercase = 'abcdefghijklmnopqrstuvwxyz' #my conditions to make sure my list element contains alphanumerical characters, thus making it a word
is_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
is_number = '0123456789'
alphanum = is_lowercase + is_number + is_uppercase

def wordCounter(my_text): #defining the function
    my_text = my_text.lower()
    word_list = my_text.split() #my_text.split turns each seperate word into an element of a list             
    word_count = 0 #We start counting from 0
    
    for word in word_list: #This for loop goes through every word in the list word_list
        
        for character in list(word):   #Every character of every word in the list is checked for the following conditions
            
            if character in (is_lowercase or is_number ):
                word_count += 1 #each time the condition is met, 1 is added to the variable word_count
                
                break #once a condition is met, the for loop breaks and goes onto the next word in the list

    if word_count > 1 :
        print('Your text has:',word_count,'words') #telling the user how many words they have
    else :
        print('Your text has:',word_count,'word') #telling the user they have one word


def repeatWords(my_text): #defining is the function 
    repeat = dict() #i just created an empty dictionnary
    my_text = my_text.lower()  #in order to well compare the words, i put everything in lowercase using .lower
    
    clean_text = "" #this defines my variable, i am starting with an empty text      
    for character in my_text: #this shuffles through each character from my_text
        

        
        if (character in alphanum) or (character == " "): #it goes to the next only if one of these conditions is met
            clean_text += character #this adds each character that satisfied the above condition and becomes my text clean of alphanumerical characters    
    
    word = 0 #this defines my variable, i am start with a count of 0 word
    for word in clean_text.split(): # .split transforms my clean text into a list
        if (not word in repeat): # if the word isnt already in my dictionary, it is added for the first time
            repeat[word] = 1
        else:
            repeat[word] += 1   #when the word is already in the dictionary once, we add 1 to for each time it appears again
    
    for word in repeat:
        print(word,'is repeated',repeat[word], 'times') # word is the word concerned and repeat[word] is the number of times it reoccurs

def special(my_text):  #this function will count the special character, meaning any character that isn't a number or on the alphabet
    
    
    notspecial = 0 #defining the variables i'll be using, i won't need them later so i kept them inside of the function
    special = 0
    space = 0
    
    for C in range(len(my_text)): #C is the index of each character in my text and loops though all of them to check if the following conditions are true, if they are, the programs does +1 to the respective variable
        if (my_text[C] in alphanum) or (my_text[C] == " "):
            notspecial += 1
        else:
            special += 1 #this is the value we want, every character that is not a number, a space or a letter is a special character.

    
    word_list = my_text.split() 
    special_list = [] #this allows the characters to be added to the end of my list
    
    for word in word_list: #This for loop goes through every word in the list mytext
        
        for character in list(word):

            if character not in alphanum:
                special_list += character #the character that satisfies the conditions is added to a list
    
    special_characters = ' '.join(special_list) #This transforms my special characters list into a string delimited by a space
                
    if special == 0:
        print("Your text has 0 special characters.")    
    else:
        print('Your text has',special,'special characters:',special_characters) # this shouldnt be printed in list form, fix it!
    
def repeatLetters(my_text):  #this function will find the most repeated letter and how many times it repeats
    repeat = dict() #i just created an empty dictionnary
    my_text = my_text.lower()  #in order to well compare the words, i put everything in lowercase using .lower
    
    clean_text = "" #this defines my variable, i am starting with an empty text      
    for letter in my_text: #this shuffles through each character from my_text
        
        if letter in is_lowercase: #it goes to the next letter only if it meets a lowercase letter
            clean_text += letter #this adds each character that satisfied the above condition and makes my text clean of numerical characters    
    
    clean_text = list(clean_text) #I am transforming the characters into a list
    
    if len(clean_text) == 0: #If my cleaned text is empty it means i don't have any repeated letters
        print('The text you entered does not contain letters')
        
    else:
        letter = 0 #this defines my variable, i am start with a count of 0 letters
        
        for letter in clean_text: # .split transforms my clean text into a list
            
            if (not letter in repeat): # if the letter isnt already in my dictionary, it is added for the first time
                repeat[letter] = 1
            else:
                repeat[letter] += 1   #when the letter is already in the dictionary once, we add 1 to for each time it appears again
        
        inverted_dict = {} #Creating a new empty dictionary 
        
        #we want the number of repetions of each letter to be the keys of inverted_dict, so that we find letters with the same numbers of repetitions
        for key in repeat: #we look at each key in the repeat dictionnary, and replace its value in inverted_dict
            if not repeat[key] in inverted_dict: 
                inverted_dict[repeat[key]] = [key] 
            else:
                inverted_dict[repeat[key]].append(key)
                
        occurences = max(inverted_dict)
        most_repeated = inverted_dict[occurences]
        
        repeated_letters = ', '.join(most_repeated)  #Transforming the list into a string
                
        if len(repeated_letters) == 1:        
            print('The letter that is repeated the most is the letter:', repeated_letters ,', repeated', occurences ,'times')
        else:
            print('The most repeated letters are:', repeated_letters ,', each repeated',occurences,'times')


def textAnalyser(my_text):
    wordCounter(my_text)
    repeatWords(my_text)
    special(my_text)
    repeatLetters(my_text)

textAnalyser(my_text)
