
def main():
    y = ""

    while y != 'q':
        y = int(input('enter a number between 20 and 100'))
        if y < 20 or y < 100:
            validate(y)
        else:
            print("wrong")




def validate(num):
    #validate the numbers

    divisByTwo(num)
    divisByThree(num)
    divisByFive(num)







def divisByTwo(num):
    out = num % 2

    if out == 0:
        print("This number is divisble by 2!")
    else:
        print("This number is NOT divisble by 2!")





def divisByThree(num):
    out = num % 3

    if out == 0:
        print("This number is divisble by 3!")
    else:
        print("This number is NOT divisble by 3!")





def divisByFive(num):
    out = num % 5

    if out == 0:
        print("This number is divisble by 5!")
    else:
        print("This number is NOT divisble by 5")



main()