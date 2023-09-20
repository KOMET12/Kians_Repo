age1 = int(input('how old are you?'))
retirement_age = int(input("what age you you want to retire?"))
income = float(input("what is your income?"))
savings_percentage = float(input("What percent of your income are you saving?"))
savings = float(input("how much is in your savings?"))

future_income = income
total_savings = savings
savings_cont = income * (savings_percentage / 100)


for i in range(age1, retirement_age + 1):
    total_savings = (total_savings * 0.06 + total_savings) +savings_cont
    print(f"{i}\t\t{future_income:,.0f}\t\t{savings_cont:,.0f}\t\t\t\t{total_savings:,.0f}")

    future_income = (future_income * 0.03 + future_income)
    savings_cont = future_income * (savings_percentage / 100)