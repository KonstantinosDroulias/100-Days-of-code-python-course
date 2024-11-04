print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, 15? %"))
people = int(input("How many poeple to split the bill? "))
paying_each = (total_bill + (total_bill * (tip_percentage / 100)))/people
paying_each = round(paying_each, 2)
print(f"Each person should pay: ${paying_each}") 