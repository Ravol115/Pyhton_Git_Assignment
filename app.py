print("Welcome to my Python Program!")
savings = input("How much money do you put in savings each month: ") #Requests an input from the user, how much money they put in savings per month
try:
    savings = float(savings) #Converts input to a float
except ValueError:
    print("Please enter a valid number.")
    exit() #Closes program and displays an error message if the user inputs and invalid response
yearly_savings = savings * 12 #Multiplies savings per month (input) by 12 to find the savings in a year
print("At this rate, you will have $", yearly_savings, "in your savings in 12 months") #Shows the user what they will have in savings after 1 year