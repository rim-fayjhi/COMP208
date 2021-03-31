print('') #For readability
print('Welcome to the population growth estimation calculator.') #Welcome message
print('')

population_year_zero = float(input('Enter the population for year 0: ')) #User inputs the values for P0, I, r, and years. 
rate = float(input('Enter the rate of growth in the following format, for 2% growth please input 0.02: ')) #The rate and p0 are transformed into floats because the input may contain decimals.
immigration_per_year = int(input('Enter the immigration per year: ')) #The user inputs an integer for I and years as people and years are whole numbers in this situation.
nbr_of_years = int(input('Enter the year you want to know the population of: '))

def getGrowthRecursive(population_year_zero, rate, immigration_per_year, nbr_of_years): #Defining the function and the variable it uses.

    if nbr_of_years == 0: #This is an exception to the formula, if the number of years is 0, the result is the same as the initial population.
        return population_year_zero #This is my base case, when this is true, the calculation is done.
    else:
        return (1 + rate)*getGrowthRecursive(population_year_zero, rate, immigration_per_year, nbr_of_years-1) + immigration_per_year #This is the formula, my function is refered to where Pn-1 would be. It continues to call itself until P0 is reached.

print('')    #For readability
print('The population at year',nbr_of_years,'is:',getGrowthRecursive(population_year_zero, rate, immigration_per_year, nbr_of_years)) #Announcing the result
