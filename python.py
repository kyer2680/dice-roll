print("Welcome to the dice roll game")
#create variables for the two dice
user = input("Please enter a number: ")
answer = ''

import random
min_value=1
max_value=6
if(random == user):
    print("you win")
elif( random != user):
    print("you lose")

roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    value1=random.randint(min_value, max_value)
    value2=random.randint(min_value, max_value)
    print(value1,value2)
    roll_again = input("Press 'y' or 'yes' to roll the dices again.")
print("Have a good day.")



