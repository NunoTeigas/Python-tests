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

game_images = [rock, paper, scissors]

# player choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number. Not cool and you lose!")
else:
  print(game_images[user_choice])

# computer choice
  print("Computer chose:")
  comp_choice = random.randint(0,2)
  print(game_images[comp_choice])

# #scissors_value < rock_value
# #rock_value < paper_value
# #paper_value < scissors_value


  if user_choice == 0 and comp_choice == 1:
    print("You lose.")
  elif user_choice == 1 and comp_choice == 2:
    print("You lose.")
  elif user_choice == 2 and comp_choice == 0:
    print("You lose.")
  elif user_choice == comp_choice:
    print("It's a draw.")
  else:
    print("You win!! Congratulations!")