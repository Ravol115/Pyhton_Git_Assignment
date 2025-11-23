print("Welcome to my Python Program!")
savings = input("How much money do you put in savings each month")
try:
    savings = float(savings)
except ValueError:
    print("Please enter a valid number.")
    exit()
yearly_savings = savings * 12
print("At this rate, you will have $", yearly_savings, "in your savings in 12 months")