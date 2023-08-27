Income = 0
Housing_expense = 0
Food_expense = 0
Transportation_expense = 0
Phone_expense = 0
Utilities_expense = 0
Clothing_expense = 0

Income = float(input("Enter your monthly income: "))
Housing_expense = float(input("Enter your Housing expenses: "))
Food_expense = float(input("Enter your Food expenses: "))
Transportation_expense = float(input("Enter your Transportation expenses: "))
Phone_expense = float(input("Enter your Phone expenses: "))
Utilities_expense = float(input("Enter your Utilities: "))
Clothing_expense = float(input("Enter your Clothing expenses: "))

Budget = Income - Housing_expense - Food_expense - Transportation_expense - Phone_expense - Utilities_expense - Clothing_expense

print(Housing_expense * .02, '%')
print(Food_expense * .02, '%')
print(Transportation_expense * .02, '%')
print(Phone_expense * .02, '%')
print(Utilities_expense * .02, '%')
print(Clothing_expense * .02, '%')

print("your balance is: $" + str(Budget))
