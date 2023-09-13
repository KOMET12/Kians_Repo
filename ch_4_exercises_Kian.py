"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
# TODO 4.2 A condition controlled loop
print("=" * 10, "Section 4.2 condition controlled loop", "=" * 10)
# write a loop that will change the variable in num by subtracting 1
# then print the variable. Keep looping until the num = 0: while num > 0
num = 10
# write your code here, the variable needs to exist before you start the loop
num = (10-1)
print(num)
num = 9-1
print(num-1)
num = 8-1
print(num-1)
num = 7-1
print(num-1)
num = 6-1
print(num-1)
num = 5-1
print(num-1)
num = 4-1
print(num-1)
num = 3-1
print(num-1)
num = 2-1
print(num-1)

# TODO 4.3 the For Loop
print("=" * 10, "Section 4.3 for loop", "=" * 10)


# TODO 4.3 the for loop - range function
print("=" * 10, "Section 4.3 using range() in a for loop", "=" * 10)
# use the range function to print the numbers from 1 to 10
x = range(10)
for n in x:
    print(n)

# TODO 4.4 a running total
print("=" * 10, "Section 4.4 running total", "=" * 10)
# Use a loop to have the user enter 5 numbers, provide a total at the end
# You will need to initialize your accumulator before entering the loop
# You can assume valid integers are entered
total = 0
for i in range(5):
    Num = input("enter a number")
    total += int(Num)
print("total", total)

# TODO 4.5 Sentinel Value
print("=" * 10, "Section 4.5 sentinel value", "=" * 10)
# Create a variable to store a total amount
# Create a variable to store a count of the numbers entered
# Use a loop to have the user enter test scores until a
# sentinel value of -1 is entered.
# After the loop, display the total, the count and the average (total / count)
Total = 0
Count = 0
Num2 = 0
while Num2 != "-1":
    Num2 = input("Enter test scores")
    Total += int(Num2)
    Count += 1
Avg = (Total/Count)
print(Total, Count, Avg)

# TODO 4.6 validating data
print("=" * 10, "Section 4.6 data validation loop", "=" * 10)
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# prompt until the user enters a valid number. Test with
# both valid and invalid data
repeat = 1
correctnumber = 0
while correctnumber !="5":
    correctnumber = input("Pick a number between 1 and 10(10 to end)")
    if correctnumber is "5":
        print("you are correct")
    else:
        repeat += 1
        print("you are incorrect")





