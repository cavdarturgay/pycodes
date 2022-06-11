rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

enter = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
#print(enter)

comp = random.randint(0,2)
#print(comp)

# Your input
if enter == 0:
  print( "You type ROCK:")
  print(rock)
elif enter == 1:
  print( "You type PAPER:")
  print(paper)
elif enter == 2:
  print( "You type SCISSORS:")
  print(scissors)

# Computer input
if comp == 0:
  print( "Computer type ROCK:")
  print(rock)
elif comp == 1:
  print( "Computer type PAPER:")
  print(paper)
elif comp == 2:
  print( "Computer type SCISSORS:")
  print(scissors)

# Result
print("")
print("")
print("#####")
print("")
print("")
if enter == 0 and comp == 2:
  print("You win!!")
elif enter == 0 and comp == 0:
  print("Do that again, equal")
elif enter == 0 and comp == 1:
  print("You Lose :(")
elif enter >2 or enter <0:
  print("You typed wrong number!")

if enter == 1 and comp == 2:
  print("You Lose :(")
elif enter == 1 and comp == 1:
  print("Do that again, equal")
elif enter == 1 and comp == 0:
  print("You win !!!")


if enter == 2 and comp == 1:
  print("You win!!")
elif enter == 2 and comp == 2:
  print("Do that again, equal")
elif enter == 2 and comp == 0:
  print("You Lose :(")


print("")
print("")
print("")