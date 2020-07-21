# Game Development - Snake Water Gun

import random
list = ["s","w","g"]
chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0
print("Snake Water Gun Game")
print("s for Snake \nw for Water \ng for Gun\n")
while no_of_chance < chance:
    inp = input("Snake , Water , Gun : ")
    rand = random.choice(list)
    if inp == rand:
        print("Tie! 0 point to each")
    elif inp == "s" and rand == "g":
        computer_point = computer_point + 1
        print(f"Your guess is {inp} and computer guess is {rand}")
        print("Computer won the game")
        print(f"Your point is {human_point} and computer point is {computer_point}")
    elif inp == "s" and rand == "w":
        human_point = human_point + 1
        print(f"Your guess is {inp} and computer guess is {rand}")
        print("You won the game")
        print(f"Your point is {human_point} and computer point is {computer_point}")
    elif inp == "w" and rand == "s":
        computer_point = computer_point + 1
        print(f"Your guess is {inp} and computer guess is {rand}")
        print("Computer won the game")
        print(f"Your point is {human_point} and computer point is {computer_point}")
    elif inp == "w" and rand == "g":
        human_point = human_point + 1
        print(f"Your guess is {inp} and computer guess is {rand}")
        print("You won the game")
        print(f"Your point is {human_point} and computer point is {computer_point}")
    elif inp == "g" and rand == "s":
        human_point = human_point + 1
        print(f"Your guess is {inp} and computer guess is {rand}")
        print("you won the game")
        print(f"Your point is {human_point} and computer point is {computer_point}")
    elif inp == "g" and rand == "w":
        computer_point = computer_point + 1
        print(f"Your guess is {inp} and computer guess is {rand}")
        print("Computer won the game")
        print(f"Your point is {human_point} and computer point is {computer_point}")
    else:
        print("Your input is wrong")
    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")
print("Game Over")
if computer_point > human_point:
    print("You lost and Computer won")
elif computer_point < human_point:
    print("You won and Computer lost")
else:
    print("Tie")
print(f"Your point is {human_point} and Computer point is {computer_point} \n")