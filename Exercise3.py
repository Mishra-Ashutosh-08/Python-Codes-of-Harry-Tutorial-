# n = 18
# A game to guess this number
# no of guesses 9
# print no of guesses left
# no of guesses he took to finish
# game over

n = 18
nog = 1
print("Number of guesses is limited to only 9 times and the number is in between 0 to 100")
while(nog <= 9):
    gn = int(input("Guess the number :\n"))
    if gn < 18:
        print("You entered a less number! Please input a greater number")
    elif gn > 18:
        print("You entered a greater number! Please input a less number")
    else:
        print("You won!\n")
        print(nog, "Number of guesses you took to finish")
        break
    print(9-nog, "Number of guesses left")
    nog = nog+1
if(nog > 9):
    print("Game over!")