# A program which take input from user till 100 and print if it exceed 100

while(True):
    num = int(input("Enter a number\n"))
    if num > 100:
        print("Congratualation! You have entered a number greater than 100")
        break
    else:
        print("Try again!\n")
        continue