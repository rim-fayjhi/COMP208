from turtle import forward, circle, setpos, penup, pendown, done, speed #I am importing the turtle functions I'll be using later on

#Start of the elements copied from Question 1
print('') #For readability
print('Welcome to the population growth graphing program.') #Welcome message
print('')


population_year_zero = float(input('Enter the population for year 0: ')) #User inputs the values for P0, I, r, and years. 
rate = float(input('Enter the rate of growth in the following format, for 2% growth please input 0.02: ')) #The rate and p0 are transformed into floats because the input may contain decimals.
immigration_per_year = int(input('Enter the immigration per year: ')) #The user inputs an integer for I and years as people and years are whole numbers in this situation.
nbr_of_years = int(input('Enter the number of years you want to generate a table for: '))

def getGrowth(population_year_zero, rate, immigration_per_year, nbr_of_years): #Defining the function and the variable it uses.
    list_growth = [population_year_zero] #The first item on the list will be P0
    
    if nbr_of_years == 0: #This is an exception to the formula, if the number of years is 0, the result is the same as the initial population.
        list_growth = population_year_zero
        print("The following list represents the population in year 0:") #Printing the result for the user to see.
        print(list_growth)      
        
    else:       
    
        for years in range(1, nbr_of_years+1):  #The range function runs the following each time for year 1 up until 
            values = (1 + rate)*list_growth[years-1] + immigration_per_year  #This is the formula for estimating population for a given year.
            list_growth.append(values)  #Here, .append adds the value as an item in the list named list_growth.
        
        list_growth = list_growth[1:] #Here I am removing year 0 from the list using list slicing
            
        print('') #For readability
        print("The following list will be graphed and represents each year's population starting from year 1 up until year",nbr_of_years,':') #Printing the result for the user to see.
        print(list_growth)
    
    return list_growth

list_growth = getGrowth(population_year_zero, rate, immigration_per_year, nbr_of_years) #This is done so I can use my list from my previous function into my new function

#End of the elements copied from Question 1

def graphGrowth(list_growth): #I am defining the graphing function, it takes the population growth list as an argument.
    speed(10)
    for index in range(0, nbr_of_years): #The index of the list indicates the x coordinate, the index starts from 0 and continues until the number of year, it loops throught each one and excecutes the tasks written below
        penup() #The pen is lifted to avoid drawing a line when I am setting the correct X coordinate
        setpos((index*95),0) #The turtle moved in the positive x axis at 95*times the index
        pendown() #The pen is down to draw
        circle((list_growth[index])/70) #A circle is drawn with a radius of the year's population devided by 70
    done()

        

graphGrowth(list_growth)
     
    

    

