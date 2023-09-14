
total = 0
count = 7

sunday = 0
monday = 0
tuesday = 0
wednesday = 0
thursday = 0
friday = 0
saturday = 0

sale1 = input("Sales for Sunday?")
sale2 = input("sales for monday?")
sale3 = input("sales for tuesday?")
sale4 = input("sales for wednesday?")
sale5 = input("sales for thursday?")
sale6 = input("sales for friday?")
sale7 = input("sales for saturday?")

total = int(sale1) + int(sale2) + int(sale3) + int(sale4) + int(sale5) + int(sale6) + int(sale7)
avg = (total/count)
print("the total amount is",total)
print("the average amount is", avg*.2)